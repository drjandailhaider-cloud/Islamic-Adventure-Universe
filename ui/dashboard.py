"""Parent Dashboard — Analytics, badges, emotional growth."""
import streamlit as st


def render_dashboard(go, user):
    from services.mission_service import MissionService
    from services.reward_service import RewardService
    import json
    from pathlib import Path

    level_info = MissionService.get_current_level(user["xp"])
    next_level  = MissionService.get_next_level(user["xp"])
    progress    = MissionService.get_level_progress(user["xp"])
    all_badges  = RewardService.get_all_badges()

    missions_all = []
    for world in MissionService.get_worlds():
        missions_all.extend(MissionService.get_missions(world["id"]))
    total_missions = len(missions_all)
    completed_count = len(user["completed_missions"])
    completion_rate = int((completed_count / total_missions * 100)) if total_missions else 0

    completed_mission_objs = [m for m in missions_all if m["id"] in user["completed_missions"]]
    learned_values = list(set(m["value"] for m in completed_mission_objs))

    # Header
    st.markdown("""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:20px;
            padding:24px;color:white;margin-bottom:20px;text-align:center;">
    <h2 style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:28px;margin:0 0 4px;">
        📊 Parent Dashboard
    </h2>
    <p style="color:rgba(255,255,255,0.6);margin:0;">Track your child's Islamic learning journey</p>
</div>""", unsafe_allow_html=True)

    # Hero profile card
    st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(26,143,140,0.2),rgba(245,200,66,0.08));
            border:1px solid rgba(245,200,66,0.25);border-radius:20px;padding:24px;margin-bottom:20px;">
    <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap;">
        <div style="font-size:64px;">{user['avatar']['emoji']}</div>
        <div style="flex:1;">
            <div style="font-family:'Fredoka One',cursive;font-size:24px;color:#0A2540;">{user['name']}</div>
            <div style="color:#1A8F8C;font-size:15px;margin-top:2px;">
                {level_info['icon']} {level_info['name']} · Level {level_info['level']} · Age {user['age_group']}
            </div>
            <div style="margin-top:10px;">
                <div style="display:flex;justify-content:space-between;font-size:12px;color:#666;margin-bottom:4px;">
                    <span>Level Progress</span><span style="color:#D4A017;font-weight:700;">{progress}%</span>
                </div>
                <div style="background:rgba(0,0,0,0.1);border-radius:50px;height:10px;">
                    <div style="height:100%;width:{progress}%;background:linear-gradient(90deg,#1A8F8C,#F5C842);border-radius:50px;"></div>
                </div>
                {'<div style="color:#aaa;font-size:11px;margin-top:4px;">'+str(next_level["xpNeeded"]-user["xp"])+' XP to '+next_level["name"]+'</div>' if next_level else ''}
            </div>
        </div>
        <div style="text-align:center;background:rgba(245,200,66,0.12);border-radius:16px;padding:16px 24px;">
            <div style="font-family:'Fredoka One',cursive;color:#D4A017;font-size:36px;">{user['xp']}</div>
            <div style="color:#666;font-size:12px;">Total XP</div>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

    # Key metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("✅ Missions Done", completed_count, f"of {total_missions}")
    with c2: st.metric("📚 Values Learned", len(learned_values))
    with c3: st.metric("🏅 Badges Earned", len([b for b in all_badges if user["xp"] >= b["xpRequired"]]))
    with c4: st.metric("📈 Completion", f"{completion_rate}%")

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 2])

    with col_left:
        # Values learned
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>💚 Islamic Values Learned</h3>", unsafe_allow_html=True)
        if learned_values:
            tags_html = " ".join([
                f'<span style="background:rgba(26,143,140,0.15);border:1px solid rgba(26,143,140,0.4);border-radius:20px;padding:6px 16px;color:#1A8F8C;font-size:14px;font-weight:700;display:inline-block;margin:4px;">✓ {v}</span>'
                for v in learned_values
            ])
            st.markdown(f'<div style="line-height:2.2;">{tags_html}</div>', unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:#aaa;font-style:italic;'>Complete missions to learn Islamic values!</p>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Emotional growth
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>💚 Emotional Growth Indicators</h3>", unsafe_allow_html=True)
        traits = [
            ("🔍", "Honesty",   min(100, completed_count * 25)),
            ("💚", "Kindness",  min(100, completed_count * 20)),
            ("⏳", "Patience",  min(100, completed_count * 18)),
            ("🦁", "Courage",   min(100, completed_count * 22)),
            ("📖", "Knowledge", min(100, completed_count * 15)),
        ]
        for icon, trait, score in traits:
            st.markdown(f"""
<div style="margin-bottom:12px;">
    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
        <span style="font-weight:700;font-size:14px;">{icon} {trait}</span>
        <span style="color:#2ECC71;font-weight:800;">{score}%</span>
    </div>
    <div style="background:#eee;border-radius:50px;height:10px;">
        <div style="height:100%;width:{score}%;background:linear-gradient(90deg,#2ECC71,#27AE60);border-radius:50px;"></div>
    </div>
</div>""", unsafe_allow_html=True)

        # Completed missions list
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>✅ Completed Missions</h3>", unsafe_allow_html=True)
        if completed_mission_objs:
            for m in completed_mission_objs:
                st.markdown(f"""
<div style="background:#f8f8f8;border-left:4px solid #2ECC71;border-radius:10px;
            padding:10px 16px;margin-bottom:8px;display:flex;align-items:center;gap:12px;">
    <span style="font-size:24px;">{m['icon']}</span>
    <div>
        <div style="font-weight:700;color:#1a1a1a;">{m['title']}</div>
        <div style="font-size:12px;color:#1A8F8C;">{m['value']} · +{m['xp']} XP</div>
    </div>
    <span style="margin-left:auto;color:#2ECC71;font-size:18px;">✅</span>
</div>""", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:#aaa;font-style:italic;'>No missions completed yet. Start your adventure!</p>", unsafe_allow_html=True)

    with col_right:
        # Badges
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#F5C842;'>🏅 Achievement Badges</h3>", unsafe_allow_html=True)
        for badge in all_badges:
            earned = user["xp"] >= badge["xpRequired"]
            st.markdown(f"""
<div style="background:{'rgba(245,200,66,0.12)' if earned else 'rgba(0,0,0,0.04)'};
            border:1px solid {'rgba(245,200,66,0.5)' if earned else 'rgba(0,0,0,0.08)'};
            border-radius:14px;padding:14px;margin-bottom:10px;
            opacity:{'1' if earned else '0.45'};display:flex;align-items:center;gap:12px;">
    <span style="font-size:30px;{'filter:grayscale(1)' if not earned else ''}">{badge['icon']}</span>
    <div>
        <div style="font-weight:700;color:{'#D4A017' if earned else '#aaa'};font-size:14px;">{badge['name']}</div>
        <div style="font-size:12px;color:#888;">{badge['desc']}</div>
        <div style="font-size:11px;color:{'#2ECC71' if earned else '#ccc'};">
            {'✅ Earned' if earned else f'Need {badge["xpRequired"]} XP'}
        </div>
    </div>
</div>""", unsafe_allow_html=True)

        # World progress
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#1A8F8C;'>🌍 World Progress</h3>", unsafe_allow_html=True)
        for world in MissionService.get_worlds():
            done, total = MissionService.count_world_completed(world["id"], user["completed_missions"])
            pct = int((done / total * 100)) if total else 0
            st.markdown(f"""
<div style="margin-bottom:12px;">
    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
        <span style="font-weight:700;font-size:14px;">{world['icon']} {world['name']}</span>
        <span style="color:{world['color']};font-weight:700;">{done}/{total}</span>
    </div>
    <div style="background:#eee;border-radius:50px;height:8px;">
        <div style="height:100%;width:{pct}%;background:{world['color']};border-radius:50px;"></div>
    </div>
</div>""", unsafe_allow_html=True)

        # Placeholder future features
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
<div style="background:rgba(26,143,140,0.06);border:1px dashed rgba(26,143,140,0.3);
            border-radius:16px;padding:16px;text-align:center;">
    <div style="font-size:24px;margin-bottom:6px;">🚀</div>
    <div style="font-weight:700;color:#1A8F8C;font-size:13px;margin-bottom:8px;">Coming Soon</div>
    <div style="color:#aaa;font-size:12px;line-height:1.8;">
        🎤 Voice Narration<br>👥 Multiplayer Mode<br>
        🥽 AR Mode<br>🏫 School Integration<br>📦 Premium Content Packs
    </div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Adventure", use_container_width=True, type="primary"):
        go("world_map")
