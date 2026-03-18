"""World Map — Select adventure world."""
import streamlit as st


def render_world_map(go, user, MissionService):
    level_info = MissionService.get_current_level(user["xp"])
    next_level  = MissionService.get_next_level(user["xp"])
    progress    = MissionService.get_level_progress(user["xp"])

    # Header greeting
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:20px;
            padding:28px;color:white;margin-bottom:20px;text-align:center;">
    <div style="font-size:56px;">{user['avatar']['emoji']}</div>
    <h2 style="font-family:'Fredoka One',cursive;font-size:26px;margin:8px 0 4px;">
        Assalamu Alaikum, {user['name']}! 👋
    </h2>
    <p style="color:rgba(255,255,255,0.65);margin:0;">Choose your next adventure world, young explorer</p>
</div>""", unsafe_allow_html=True)

    # XP Level bar
    st.markdown(f"""
<div style="background:rgba(26,143,140,0.1);border:1px solid rgba(245,200,66,0.3);
            border-radius:16px;padding:16px 20px;margin-bottom:20px;">
    <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
        <span style="font-weight:800;color:#1A8F8C;">{level_info['icon']} {level_info['name']} · Level {level_info['level']}</span>
        <span style="color:#D4A017;font-weight:700;">{user['xp']} XP</span>
    </div>
    <div style="background:rgba(0,0,0,0.1);border-radius:50px;height:12px;overflow:hidden;">
        <div style="height:100%;width:{progress}%;background:linear-gradient(90deg,#1A8F8C,#F5C842);border-radius:50px;"></div>
    </div>
    {'<div style="color:#888;font-size:12px;margin-top:4px;">'+str(next_level["xpNeeded"]-user["xp"])+' XP to '+next_level["icon"]+' '+next_level["name"]+'</div>' if next_level else ''}
</div>""", unsafe_allow_html=True)

    # World cards
    st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>🌍 Choose Your World</h3>", unsafe_allow_html=True)
    worlds = MissionService.get_worlds()
    cols = st.columns(2)
    for i, world in enumerate(worlds):
        done, total = MissionService.count_world_completed(world["id"], user["completed_missions"])
        world_pct = int((done / total * 100)) if total > 0 else 0
        with cols[i % 2]:
            lock_badge = "🔒 Locked" if world["locked"] else f"✅ {done}/{total} done"
            st.markdown(f"""
<div style="background:{'rgba(60,60,60,0.5)' if world['locked'] else 'linear-gradient(135deg,#0A2540,#1A3A5C)'};
            border-radius:20px;padding:24px;color:white;margin-bottom:14px;
            border:1px solid rgba(255,255,255,{'0.06' if world['locked'] else '0.15'});
            opacity:{'0.55' if world['locked'] else '1'};">
    <div style="font-size:44px;margin-bottom:10px;">{world['icon']}</div>
    <div style="font-family:'Fredoka One',cursive;color:{world['color']};font-size:20px;">{world['name']}</div>
    <div style="color:rgba(255,255,255,0.45);font-size:13px;margin:4px 0 10px;">{world['arabic']}</div>
    <p style="color:rgba(255,255,255,0.7);font-size:13px;line-height:1.5;margin-bottom:14px;">{world['description']}</p>
    <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
        <span style="color:rgba(255,255,255,0.5);">{lock_badge}</span>
        <span style="color:{world['color']};font-weight:700;">⚡ {world['xpReward']} XP</span>
    </div>
    <div style="background:rgba(255,255,255,0.1);border-radius:50px;height:8px;">
        <div style="height:100%;width:{world_pct}%;background:linear-gradient(90deg,{world['color']},white);border-radius:50px;"></div>
    </div>
</div>""", unsafe_allow_html=True)

            if not world["locked"]:
                if st.button(f"Enter {world['name']} →", key=f"world_{world['id']}", use_container_width=True, type="primary"):
                    go("mission", selected_world=world)

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick stats
    st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>📊 Your Stats</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("✅ Missions", len(user["completed_missions"]))
    with c2: st.metric("🏅 Badges", len(user["badges"]))
    with c3: st.metric("⚡ Total XP", user["xp"])
    with c4: st.metric("🌍 Worlds", "2 active")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Parent Dashboard", use_container_width=True):
            go("dashboard")
    with col2:
        if st.button("🚪 Sign Out", use_container_width=True):
            go("landing", user=None)
