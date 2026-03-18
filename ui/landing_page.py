"""Landing Page — Premium hero + features + testimonials."""
import streamlit as st


def render_landing(go):
    # Dark full-page wrapper
    st.markdown("""
<div style="background:linear-gradient(160deg,#0A2540 0%,#1A3A5C 45%,#0D5C5C 100%);
            border-radius:24px; padding:48px 32px; margin-bottom:24px; text-align:center; color:white;">
    <div style="font-size:80px; margin-bottom:12px;">🕌</div>
    <h1 style="font-family:'Fredoka One',cursive; font-size:clamp(36px,5vw,64px); margin:0 0 8px;">
        Islamic Adventure Universe
    </h1>
    <h2 style="font-family:'Fredoka One',cursive; font-size:clamp(18px,3vw,30px); margin:0 0 16px;
               background:linear-gradient(90deg,#F5C842,#FFD700); -webkit-background-clip:text;
               -webkit-text-fill-color:transparent; background-clip:text;">
        For Kids · Ages 5–15
    </h2>
    <p style="color:rgba(255,255,255,0.75); font-size:18px; max-width:520px; margin:0 auto 24px; line-height:1.65;">
        Where children explore <strong style="color:#F5C842">Islamic values</strong>,
        epic adventures, and build <strong style="color:#4ECDC4">character</strong>
        through AI-powered interactive stories.
    </p>
    <p style="color:rgba(255,255,255,0.4); font-size:14px; font-style:italic;">
        🌍 4 Adventure Worlds · 20+ Missions · AI-Personalized Stories · Parent Dashboard
    </p>
</div>
""", unsafe_allow_html=True)

    # CTA Buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🚀 Start Free Adventure!", use_container_width=True, type="primary"):
            go("signup")
    with col2:
        if st.button("🔑 Sign In", use_container_width=True):
            go("login")
    with col3:
        st.markdown("""<div style="text-align:center;padding:8px;color:rgba(26,143,140,0.7);font-size:13px;">
            ✦ No credit card required</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats strip
    st.markdown("""
<div style="display:flex;justify-content:center;gap:40px;flex-wrap:wrap;
            background:rgba(26,143,140,0.08);border-radius:16px;padding:20px;margin-bottom:28px;">
    <div style="text-align:center;">
        <div style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:30px;">10K+</div>
        <div style="color:#666;font-size:13px;">Young Explorers</div>
    </div>
    <div style="text-align:center;">
        <div style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:30px;">4</div>
        <div style="color:#666;font-size:13px;">Adventure Worlds</div>
    </div>
    <div style="text-align:center;">
        <div style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:30px;">20+</div>
        <div style="color:#666;font-size:13px;">Islamic Missions</div>
    </div>
    <div style="text-align:center;">
        <div style="font-family:'Fredoka One',cursive;color:#F5C842;font-size:30px;">98%</div>
        <div style="color:#666;font-size:13px;">Parent Approval</div>
    </div>
</div>
""", unsafe_allow_html=True)

    # Worlds Preview
    st.markdown("<h2 style='font-family:Fredoka One,cursive;color:#1A8F8C;text-align:center;'>✨ Explore 4 Magical Worlds</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#666;margin-bottom:20px;'>Each world teaches unique Islamic values through unforgettable adventures</p>", unsafe_allow_html=True)

    worlds = [
        ("🌅", "Desert Journey", "#F4A460", "Honesty · Patience · Helping Others"),
        ("🕌", "Medina Quest", "#4ECDC4", "Kindness · Generosity · Brotherhood"),
        ("🌊", "Ocean of Knowledge", "#87CEEB", "Seeking Knowledge · Wisdom 🔒"),
        ("🌸", "Garden of Jannah", "#98FB98", "Good Deeds · Gratitude 🔒"),
    ]
    cols = st.columns(4)
    for i, (icon, name, color, tags) in enumerate(worlds):
        with cols[i]:
            st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:18px;
            padding:22px;text-align:center;color:white;border:1px solid rgba(255,255,255,0.1);
            min-height:170px;">
    <div style="font-size:42px;margin-bottom:8px;">{icon}</div>
    <div style="font-family:'Fredoka One',cursive;color:{color};font-size:16px;margin-bottom:6px;">{name}</div>
    <div style="color:rgba(255,255,255,0.55);font-size:12px;">{tags}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Features
    st.markdown("<h2 style='font-family:Fredoka One,cursive;color:#1A8F8C;text-align:center;'>🌟 Why Families Love Us</h2>", unsafe_allow_html=True)
    features = [
        ("📖", "Quran & Sunnah Values", "Every story is rooted in authentic Islamic teachings"),
        ("🎮", "Gamified Learning", "XP, badges, levels — learning feels like play"),
        ("🤖", "AI-Powered Stories", "Dynamic narratives adapt to your child's journey"),
        ("👨‍👩‍👧", "Parent Dashboard", "Full visibility into progress and emotional growth"),
        ("🌍", "4 Adventure Worlds", "Desert, Medina, Ocean, Garden — endless exploration"),
        ("💚", "100% Safe & Halal", "Kid-safe, ad-free, values-driven experience"),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""
<div style="background:#f8f8f8;border-radius:16px;padding:20px;margin-bottom:14px;
            border-left:4px solid #1A8F8C;">
    <div style="font-size:32px;margin-bottom:8px;">{icon}</div>
    <div style="color:#1A8F8C;font-weight:800;font-size:15px;margin-bottom:4px;">{title}</div>
    <div style="color:#666;font-size:13px;line-height:1.5;">{desc}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Testimonials
    st.markdown("<h2 style='font-family:Fredoka One,cursive;color:#1A8F8C;text-align:center;'>💬 Parent Stories</h2>", unsafe_allow_html=True)
    testimonials = [
        ("👩", "Umm Ibrahim", "Mother of 3", "My children spend hours on this app and every session teaches them something beautiful about our Deen."),
        ("👨", "Ahmad Farouk", "Islamic School Teacher", "Finally an app that combines genuine Islamic values with the engagement children need."),
        ("👩‍🦱", "Sara Malik", "Parent", "My 7-year-old now talks about Islamic values daily. This app made our Deen feel like an exciting adventure!"),
    ]
    cols = st.columns(3)
    for i, (avatar, name, role, text) in enumerate(testimonials):
        with cols[i]:
            st.markdown(f"""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:18px;
            padding:22px;color:white;border:1px solid rgba(245,200,66,0.2);">
    <div style="color:#F5C842;font-size:16px;margin-bottom:10px;">★★★★★</div>
    <p style="color:rgba(255,255,255,0.8);font-size:14px;line-height:1.6;font-style:italic;margin-bottom:14px;">"{text}"</p>
    <div style="display:flex;align-items:center;gap:10px;">
        <span style="font-size:28px;">{avatar}</span>
        <div>
            <div style="font-weight:700;font-size:14px;">{name}</div>
            <div style="color:#4ECDC4;font-size:12px;">{role}</div>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Trust strip
    st.markdown("""
<div style="text-align:center;padding:16px;background:rgba(26,143,140,0.06);
            border-radius:16px;color:#666;font-size:14px;">
    🔒 100% Safe &amp; Halal &nbsp;·&nbsp; 📵 Zero Ads &nbsp;·&nbsp;
    👨‍👩‍👧 Parent Controls &nbsp;·&nbsp; 🌍 Available Worldwide
</div>""", unsafe_allow_html=True)

    # Footer
    st.markdown("""
<div style="text-align:center;margin-top:32px;padding-top:16px;
            border-top:1px solid rgba(26,143,140,0.2);color:#aaa;font-size:12px;">
    🕌 <strong style="font-family:'Fredoka One',cursive;color:#1A8F8C;">Adventure Universe AI</strong>
    &nbsp;·&nbsp; © 2026 Islamic Adventure Universe
    &nbsp;·&nbsp; Built with ❤️ for Muslim children worldwide
</div>""", unsafe_allow_html=True)
