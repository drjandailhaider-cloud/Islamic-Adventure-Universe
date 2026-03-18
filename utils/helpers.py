"""Shared utility helpers."""
import streamlit as st
from datetime import datetime


def format_xp(xp: int) -> str:
    if xp >= 1000:
        return f"{xp/1000:.1f}k"
    return str(xp)


def time_greeting() -> str:
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"


def islamic_greeting() -> str:
    return "Assalamu Alaikum"


def render_divider(color: str = "#1A8F8C"):
    st.markdown(
        f'<hr style="border:none;border-top:2px solid {color};margin:20px 0;opacity:0.2;">',
        unsafe_allow_html=True,
    )


def render_section_header(title: str, subtitle: str = "", color: str = "#1A8F8C"):
    st.markdown(
        f'<h3 style="font-family:Fredoka One,cursive;color:{color};margin-bottom:4px;">{title}</h3>',
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f'<p style="color:#888;font-size:14px;margin-bottom:16px;">{subtitle}</p>',
            unsafe_allow_html=True,
        )
