"""
╔══════════════════════════════════════════════════════════╗
║     ISLAMIC ADVENTURE UNIVERSE — MAIN APP ENTRY          ║
║     Version: 1.0.0  |  Streamlit + Claude AI             ║
╚══════════════════════════════════════════════════════════╝
"""

import streamlit as st

st.set_page_config(
    page_title="Islamic Adventure Universe",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://adventureuniverse.ai/help",
        "Report a bug": "https://adventureuniverse.ai/contact",
        "About": "# Islamic Adventure Universe\nGamified Islamic education for kids aged 5–15.",
    },
)

from services.user_service import UserService
from services.mission_service import MissionService
from services.ai_service import AIService
from services.reward_service import RewardService
from ui.landing_page import render_landing
from ui.auth_page import render_signup, render_login
from ui.world_map import render_world_map
from ui.mission_page import render_mission
from ui.reward_page import render_reward
from ui.dashboard import render_dashboard
from ui.styles import inject_global_styles

inject_global_styles()

DEFAULTS = {
    "page": "landing",
    "user": None,
    "selected_world": None,
    "selected_mission": None,
    "mission_result": None,
    "toast_msg": None,
}
for key, val in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = val

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg, icon="✨")
    st.session_state.toast_msg = None

def go(page: str, **kwargs):
    st.session_state.page = page
    for k, v in kwargs.items():
        st.session_state[k] = v
    st.rerun()

st.markdown('<div class="watermark">✦ Adventure Universe AI ✦</div>', unsafe_allow_html=True)

page = st.session_state.page

if page == "landing":
    render_landing(go)
elif page == "signup":
    render_signup(go, UserService)
elif page == "login":
    render_login(go, UserService)
elif page == "world_map":
    if not st.session_state.user:
        go("landing")
    else:
        render_world_map(go, st.session_state.user, MissionService)
elif page == "mission":
    if not st.session_state.user or not st.session_state.selected_mission:
        go("world_map")
    else:
        render_mission(go, st.session_state.user, st.session_state.selected_world,
                       st.session_state.selected_mission, AIService, RewardService)
elif page == "reward":
    if not st.session_state.mission_result:
        go("world_map")
    else:
        render_reward(go, st.session_state.mission_result, st.session_state.user)
elif page == "dashboard":
    if not st.session_state.user:
        go("landing")
    else:
        render_dashboard(go, st.session_state.user)
else:
    go("landing")
