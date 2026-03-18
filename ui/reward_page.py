"""Reward Page — Celebration screen after completing a mission."""
import streamlit as st


def render_reward(go, result, user):
    mission   = result["mission"]
    xp_gained = result["xp_gained"]
    new_badges = result["new_badges"]

    from services.user_service import UserService
    updated_user = UserService.update_progress(
        user["username"],
        mission["id"],
        xp_gained,
        [b["id"] for b in new_badges],
    )
    if updated_user:
        st.session_state.user = updated_user

    st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A4A1A,#0A2540);border-radius:24px;
            padding:48px;text-align:center;color:white;margin-bottom:24px;">
    <div style="font-size:80px;margin-bottom:8px;">🏆</div>
    <h1 style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:42px;margin:0 0 8px;">MashaAllah!</h1>
    <p style="color:rgba(255,255,255,0.8);font-size:18px;margin-bottom:28px;">
        You completed <strong style="color:#4ECDC4;">{mission['title']}</strong>
    </p>

    <div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;margin-bottom:28px;">
        <div style="background:rgba(245,200,66,0.15);border:2px solid rgba(245,200,66,0.6);
                    border-radius:20px;padding:20px 32px;">
            <div style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:36px;">+{xp_gained}</div>
            <div style="color:rgba(255,255,255,0.6);font-size:14px;">XP Earned</div>
        </div>
        <div style="background:rgba(26,143,140,0.15);border:2px solid rgba(26,143,140,0.5);
                    border-radius:20px;padding:20px 32px;">
            <div style="font-size:32px;">💚</div>
            <div style="color:#4ECDC4;font-size:14px;font-weight:700;">{mission['value']}</div>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

    # New badges
    if new_badges:
        st.markdown("<h3 style='font-family:Fredoka One,cursive;color:#F5C842;text-align:center;'>🎖 New Badge Unlocked!</h3>", unsafe_allow_html=True)
        badge_cols = st.columns(len(new_badges))
        for i, badge in enumerate(new_badges):
            with badge_cols[i]:
                st.markdown(f"""
<div style="background:rgba(245,200,66,0.12);border:2px solid rgba(245,200,66,0.5);
            border-radius:18px;padding:20px;text-align:center;color:white;">
    <div style="font-size:40px;margin-bottom:8px;">{badge['icon']}</div>
    <div style="font-weight:800;color:#F5C842;margin-bottom:4px;">{badge['name']}</div>
    <div style="font-size:12px;color:rgba(255,255,255,0.6);">{badge['desc']}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Hadith / encouragement
    hadiths = [
        '"The best of people are those most beneficial to others." — Prophet Muhammad ﷺ',
        '"Verily, with every hardship comes ease." — Quran 94:6',
        '"Allah loves those who purify themselves." — Quran 2:222',
        '"Be truthful, for truth leads to righteousness." — Bukhari',
    ]
    import random
    hadith = random.choice(hadiths)
    st.markdown(f"""
<div style="background:rgba(26,143,140,0.1);border-left:4px solid #1A8F8C;border-radius:12px;
            padding:16px 20px;text-align:center;color:#1A8F8C;font-style:italic;font-size:15px;margin-bottom:20px;">
    {hadith}
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Continue Adventure →", use_container_width=True, type="primary"):
            go("world_map", mission_result=None)
    with col2:
        if st.button("📊 View Dashboard", use_container_width=True):
            go("dashboard", mission_result=None)
