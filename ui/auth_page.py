"""Auth Page — Sign up and Login."""
import streamlit as st


def render_signup(go, UserService):
    st.markdown("""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:24px;
            padding:36px;text-align:center;color:white;margin-bottom:24px;">
    <div style="font-size:56px;margin-bottom:10px;">✨</div>
    <h2 style="font-family:'Fredoka One',cursive;font-size:28px;margin:0 0 6px;">Create Your Hero!</h2>
    <p style="color:rgba(255,255,255,0.6);margin:0;">Every great adventure starts with a name</p>
</div>""", unsafe_allow_html=True)

    col_main, col_side = st.columns([2, 1])
    with col_main:
        with st.form("signup_form"):
            name = st.text_input("🌟 Your Name", placeholder="Enter your name...")
            username = st.text_input("👤 Username", placeholder="Pick a unique username...")
            password = st.text_input("🔒 Password", type="password", placeholder="Min 4 characters...")
            age_group = st.selectbox("📅 Age Group", ["5-7", "8-10", "11-13", "14-15"])

            st.markdown("#### 🦸 Choose Your Hero Avatar")
            avatars = UserService.get_all_avatars()
            avatar_cols = st.columns(4)
            selected_avatar = st.radio("Avatar", [a["id"] for a in avatars],
                                       format_func=lambda x: next(
                                           f"{a['emoji']} {a['name']}" for a in avatars if a["id"] == x),
                                       horizontal=True, label_visibility="collapsed")

            submitted = st.form_submit_button("🚀 Begin My Adventure!", use_container_width=True, type="primary")

            if submitted:
                if not name.strip() or not username.strip() or not password:
                    st.error("Please fill in all fields!")
                else:
                    ok, msg = UserService.register(name, age_group, selected_avatar, username, password)
                    if ok:
                        ok2, user = UserService.login(username, password)
                        if ok2:
                            go("world_map", user=user, toast_msg=f"Welcome, {name}! Your adventure begins! 🌟")
                    else:
                        st.error(msg)

    with col_side:
        st.markdown("""
<div style="background:rgba(26,143,140,0.1);border-radius:18px;padding:20px;border:1px solid rgba(26,143,140,0.3);">
    <h4 style="color:#1A8F8C;font-family:'Fredoka One',cursive;margin-bottom:12px;">🌟 What awaits you:</h4>
    <ul style="color:#444;font-size:14px;line-height:2;">
        <li>4 magical adventure worlds</li>
        <li>20+ Islamic missions</li>
        <li>AI-powered stories</li>
        <li>XP & level system</li>
        <li>Achievement badges</li>
        <li>Parent dashboard</li>
    </ul>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Home"):
        go("landing")
    st.caption("Already have an account? [Sign In](#)")
    if st.button("🔑 Go to Sign In"):
        go("login")


def render_login(go, UserService):
    st.markdown("""
<div style="background:linear-gradient(135deg,#0A2540,#1A3A5C);border-radius:24px;
            padding:36px;text-align:center;color:white;margin-bottom:24px;">
    <div style="font-size:56px;margin-bottom:10px;">🔑</div>
    <h2 style="font-family:'Fredoka One',cursive;font-size:28px;margin:0 0 6px;">Welcome Back!</h2>
    <p style="color:rgba(255,255,255,0.6);margin:0;">Continue your adventure where you left off</p>
</div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("👤 Username", placeholder="Your username...")
            password = st.text_input("🔒 Password", type="password", placeholder="Your password...")
            submitted = st.form_submit_button("🚀 Enter Adventure!", use_container_width=True, type="primary")

            if submitted:
                ok, result = UserService.login(username, password)
                if ok:
                    go("world_map", user=result, toast_msg=f"Assalamu Alaikum, {result['name']}! 👋")
                else:
                    st.error(result)

        if st.button("← Back to Home", use_container_width=True):
            go("landing")
        if st.button("📝 Create New Account", use_container_width=True):
            go("signup")
