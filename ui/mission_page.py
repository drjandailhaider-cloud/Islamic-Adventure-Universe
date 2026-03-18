"""Mission Page — Story display, choices, AI story generation."""
import streamlit as st


def render_mission(go, user, world, mission, AIService, RewardService):
    is_done = mission["id"] in user["completed_missions"]

    # Header
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:20px;
            padding:28px;color:white;margin-bottom:20px;text-align:center;">
    <div style="font-size:56px;">{mission['icon']}</div>
    <h2 style="font-family:'Fredoka One',cursive;font-size:26px;margin:8px 0 4px;">{mission['title']}</h2>
    <div style="display:inline-block;background:rgba(26,143,140,0.25);border:1px solid rgba(26,143,140,0.6);
                border-radius:20px;padding:6px 18px;font-size:14px;color:#4ECDC4;font-weight:700;">
        ⚡ Value: {mission['value']} &nbsp;|&nbsp; {mission['xp']} XP Reward
    </div>
    {('<div style="margin-top:12px;background:rgba(46,204,113,0.2);border:1px solid #2ECC71;border-radius:12px;padding:8px 16px;display:inline-block;color:#2ECC71;font-weight:700;">✅ Already Completed — Replay Available</div>' if is_done else '')}
</div>""", unsafe_allow_html=True)

    # Session state for this mission flow
    if "mission_phase" not in st.session_state:
        st.session_state.mission_phase = "story"
    if "chosen_choice" not in st.session_state:
        st.session_state.chosen_choice = None
    if "ai_story_text" not in st.session_state:
        st.session_state.ai_story_text = None

    # ── PHASE: STORY ──────────────────────────────────────────
    if st.session_state.mission_phase == "story":
        st.markdown(f"""
<div style="background:rgba(26,143,140,0.08);border:1px solid rgba(26,143,140,0.25);
            border-radius:20px;padding:26px;margin-bottom:20px;">
    <div style="color:#888;font-size:13px;font-style:italic;margin-bottom:12px;">📖 The Story Begins...</div>
    <p style="color:#1a1a1a;font-size:17px;line-height:1.75;margin:0;">{mission['story']}</p>
</div>""", unsafe_allow_html=True)

        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("⚡ What will you do? →", use_container_width=True, type="primary"):
                st.session_state.mission_phase = "choice"
                st.rerun()
        with col2:
            if st.button("← Back", use_container_width=True):
                st.session_state.mission_phase = "story"
                st.session_state.chosen_choice = None
                st.session_state.ai_story_text = None
                go("mission", selected_world=world, selected_mission=None)

    # ── PHASE: CHOICE ─────────────────────────────────────────
    elif st.session_state.mission_phase == "choice":
        st.markdown(f"""
<div style="background:rgba(26,143,140,0.06);border:1px solid rgba(26,143,140,0.2);
            border-radius:16px;padding:20px;margin-bottom:20px;color:#444;font-size:15px;line-height:1.7;">
    {mission['story']}
</div>""", unsafe_allow_html=True)

        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;text-align:center;'>🤔 What do you choose?</h3>", unsafe_allow_html=True)

        for i, choice in enumerate(mission["choices"]):
            icon = "✅" if i == 0 else "❌"
            bg = "rgba(46,204,113,0.1)" if i == 0 else "rgba(255,107,107,0.08)"
            border = "#2ECC71" if i == 0 else "rgba(255,107,107,0.5)"
            if st.button(f"{icon}  {choice['text']}", key=f"choice_{i}", use_container_width=True):
                st.session_state.chosen_choice = choice
                st.session_state.mission_phase = "outcome"
                if choice["positive"]:
                    with st.spinner("✨ Generating your story continuation..."):
                        story = AIService.generate_story(
                            user["name"], mission["title"],
                            world["name"], choice["text"], mission["value"]
                        )
                        st.session_state.ai_story_text = story
                st.rerun()

        if st.button("← Go Back to Story"):
            st.session_state.mission_phase = "story"
            st.rerun()

    # ── PHASE: OUTCOME ────────────────────────────────────────
    elif st.session_state.mission_phase == "outcome":
        choice = st.session_state.chosen_choice
        if not choice:
            st.session_state.mission_phase = "story"
            st.rerun()

        is_positive = choice["positive"]
        header_color = "#2ECC71" if is_positive else "#FF6B6B"
        header_label = "🌟 Excellent Choice!" if is_positive else "💭 A Learning Moment..."

        st.markdown(f"""
<div style="background:rgba(26,143,140,0.08);border:2px solid {'rgba(245,200,66,0.4)' if is_positive else 'rgba(255,107,107,0.3)'};
            border-radius:20px;padding:26px;margin-bottom:18px;">
    <div style="font-size:18px;font-weight:800;color:{header_color};margin-bottom:12px;">{header_label}</div>
    <p style="color:#1a1a1a;font-size:16px;line-height:1.7;margin:0;">{choice['outcome']}</p>
</div>""", unsafe_allow_html=True)

        # AI story continuation
        if is_positive and st.session_state.ai_story_text:
            st.markdown(f"""
<div style="background:rgba(26,143,140,0.15);border:1px solid rgba(26,143,140,0.45);
            border-radius:16px;padding:20px;margin-bottom:18px;">
    <div style="color:#1A8F8C;font-weight:800;font-size:13px;margin-bottom:8px;">🤖 Your Story Continues (AI-Generated)...</div>
    <p style="color:#1a1a1a;font-size:15px;line-height:1.7;margin:0;">{st.session_state.ai_story_text}</p>
</div>""", unsafe_allow_html=True)

        # XP reward box
        if is_positive:
            st.markdown(f"""
<div style="background:rgba(245,200,66,0.12);border:2px solid rgba(245,200,66,0.5);
            border-radius:20px;padding:22px;text-align:center;margin-bottom:18px;">
    <div style="font-size:48px;">⚡</div>
    <div style="font-family:'Fredoka One',cursive;color:#D4A017;font-size:32px;">+{choice['xp']} XP Earned!</div>
    <div style="color:#666;font-size:15px;margin-top:4px;">MashaAllah, {user['name']}! You chose the right path.</div>
</div>""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if is_positive:
                if st.button("🏆 Claim Reward!", use_container_width=True, type="primary"):
                    # Evaluate badges
                    new_badges = RewardService.evaluate_new_badges(
                        user["xp"], user["xp"] + choice["xp"], user["badges"]
                    )
                    result = {
                        "mission": mission,
                        "xp_gained": choice["xp"],
                        "new_badges": new_badges,
                        "choice": choice,
                    }
                    # Reset mission session state
                    st.session_state.mission_phase = "story"
                    st.session_state.chosen_choice = None
                    st.session_state.ai_story_text = None
                    go("reward", mission_result=result)
            else:
                if st.button("↩ Try Again", use_container_width=True, type="primary"):
                    st.session_state.mission_phase = "choice"
                    st.session_state.chosen_choice = None
                    st.rerun()
        with col2:
            if st.button("← Back to Missions", use_container_width=True):
                st.session_state.mission_phase = "story"
                st.session_state.chosen_choice = None
                st.session_state.ai_story_text = None
                go("mission", selected_world=world, selected_mission=None)
