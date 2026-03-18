"""Mission List — Shows all missions inside a selected world."""
import streamlit as st


def render_mission_list(go, user, world, MissionService):
    missions = MissionService.get_missions(world["id"])

    st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:20px;
            padding:28px;color:white;margin-bottom:20px;text-align:center;">
    <div style="font-size:52px;">{world['icon']}</div>
    <h2 style="font-family:'Fredoka One',cursive;font-size:26px;margin:8px 0 4px;">{world['name']}</h2>
    <div style="color:rgba(255,255,255,0.45);font-size:14px;margin-bottom:8px;">{world['arabic']}</div>
    <p style="color:rgba(255,255,255,0.7);font-size:14px;margin:0;">{world['description']}</p>
</div>""", unsafe_allow_html=True)

    if st.button("← Back to World Map", use_container_width=False):
        go("world_map")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>⚡ Choose a Mission</h3>",
                unsafe_allow_html=True)

    if not missions:
        st.info("🌟 More missions coming soon for this world! Try another world for now.")
        return

    for mission in missions:
        is_done = mission["id"] in user["completed_missions"]
        border  = "#2ECC71" if is_done else "rgba(26,143,140,0.3)"
        bg      = "rgba(46,204,113,0.08)" if is_done else "rgba(26,143,140,0.06)"
        status  = "✅ Completed" if is_done else "▶ Play"

        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
<div style="background:{bg};border:2px solid {border};border-radius:16px;
            padding:16px 20px;margin-bottom:4px;">
    <div style="display:flex;align-items:center;gap:14px;">
        <span style="font-size:36px;">{'✅' if is_done else mission['icon']}</span>
        <div>
            <div style="font-weight:800;color:#0A2540;font-size:16px;">{mission['title']}</div>
            <div style="color:#1A8F8C;font-size:13px;margin-top:2px;">
                Islamic Value: <strong>{mission['value']}</strong>
            </div>
            <div style="color:#D4A017;font-size:13px;margin-top:2px;">⚡ {mission['xp']} XP reward</div>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

        with col2:
            btn_type = "secondary" if is_done else "primary"
            if st.button(status, key=f"play_{mission['id']}",
                         use_container_width=True, type=btn_type):
                # Reset mission phase state each time
                st.session_state.mission_phase = "story"
                st.session_state.chosen_choice = None
                st.session_state.ai_story_text = None
                go("mission", selected_mission=mission, selected_world=world)

        st.markdown("<div style='margin-bottom:8px;'></div>", unsafe_allow_html=True)
