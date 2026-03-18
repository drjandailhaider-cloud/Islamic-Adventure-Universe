"""Global CSS styles for Islamic Adventure Universe."""
import streamlit as st


def inject_global_styles():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;700;800;900&display=swap');

/* ── Reset & Base ── */
* { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Nunito', sans-serif !important;
    background: #FFF8EE !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }

/* ── Watermark ── */
.watermark {
    position: fixed;
    bottom: 16px; right: 20px;
    font-family: 'Fredoka One', cursive;
    font-size: 11px;
    color: rgba(26,143,140,0.3);
    letter-spacing: 1px;
    pointer-events: none;
    z-index: 9999;
    user-select: none;
}

/* ── Display font ── */
.font-display { font-family: 'Fredoka One', cursive !important; }

/* ── Teal card ── */
.card-teal {
    background: linear-gradient(135deg, #0A2540, #1A3A5C);
    border-radius: 20px;
    padding: 28px;
    color: white;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 16px;
}

/* ── Gold stat box ── */
.stat-box {
    background: rgba(245,200,66,0.12);
    border: 2px solid rgba(245,200,66,0.4);
    border-radius: 16px;
    padding: 16px;
    text-align: center;
}

/* ── Progress bar ── */
.xp-bar-wrap {
    background: rgba(255,255,255,0.15);
    border-radius: 50px;
    height: 14px;
    overflow: hidden;
    margin: 6px 0;
}
.xp-bar-fill {
    height: 100%;
    border-radius: 50px;
    background: linear-gradient(90deg, #1A8F8C, #F5C842);
    transition: width 0.8s ease;
}

/* ── World card ── */
.world-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 22px;
    cursor: pointer;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    color: white;
}
.world-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.25);
}

/* ── Mission card ── */
.mission-card {
    background: rgba(255,255,255,0.06);
    border: 2px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 18px 22px;
    cursor: pointer;
    color: white;
    margin-bottom: 12px;
    transition: transform 0.2s ease;
}
.mission-card:hover { transform: translateX(6px); }
.mission-card.completed { border-color: #2ECC71; background: rgba(46,204,113,0.12); }

/* ── Choice buttons ── */
.choice-btn {
    width: 100%;
    padding: 18px 22px;
    border-radius: 16px;
    border: 2px solid;
    cursor: pointer;
    font-family: 'Nunito', sans-serif;
    font-size: 16px;
    font-weight: 700;
    text-align: left;
    margin-bottom: 12px;
    transition: transform 0.15s ease;
}
.choice-btn:active { transform: scale(0.97); }
.choice-positive { background: rgba(46,204,113,0.15); border-color: #2ECC71; color: white; }
.choice-negative { background: rgba(255,107,107,0.1); border-color: rgba(255,107,107,0.5); color: white; }

/* ── Hero section ── */
.hero-bg {
    background: linear-gradient(160deg, #0A2540 0%, #1A3A5C 50%, #0D5C5C 100%);
    border-radius: 24px;
    padding: 48px 32px;
    text-align: center;
    color: white;
}

/* ── Badge card ── */
.badge-card {
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    transition: transform 0.2s ease;
}
.badge-card:hover { transform: scale(1.05); }
.badge-earned { background: rgba(245,200,66,0.15); border: 1px solid rgba(245,200,66,0.5); }
.badge-locked { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); opacity: 0.5; }

/* ── CTA button ── */
.cta-btn {
    display: inline-block;
    padding: 16px 48px;
    border-radius: 50px;
    background: linear-gradient(135deg, #F5C842, #D4A017);
    color: #0A2540;
    font-family: 'Fredoka One', cursive;
    font-size: 20px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(245,200,66,0.35);
    transition: transform 0.15s ease;
}
.cta-btn:hover { transform: translateY(-3px); }

/* ── Story box ── */
.story-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 26px;
    color: rgba(255,255,255,0.9);
    font-size: 17px;
    line-height: 1.75;
    margin-bottom: 20px;
}

/* ── AI Story box ── */
.ai-story-box {
    background: rgba(26,143,140,0.2);
    border: 1px solid rgba(26,143,140,0.5);
    border-radius: 16px;
    padding: 20px;
    color: rgba(255,255,255,0.88);
    font-size: 15px;
    line-height: 1.7;
    margin-top: 14px;
}

/* ── Streamlit button overrides ── */
div[data-testid="stButton"] > button {
    border-radius: 50px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    transition: transform 0.15s ease !important;
}
div[data-testid="stButton"] > button:hover { transform: translateY(-2px) !important; }
div[data-testid="stButton"] > button:active { transform: scale(0.97) !important; }

/* Primary buttons */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #1A8F8C, #0D5C5C) !important;
    border: none !important;
    color: white !important;
}

/* ── Input overrides ── */
div[data-testid="stTextInput"] input {
    border-radius: 12px !important;
    border: 2px solid rgba(26,143,140,0.4) !important;
    font-family: 'Nunito', sans-serif !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #1A8F8C !important;
    box-shadow: 0 0 0 3px rgba(26,143,140,0.2) !important;
}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] > div {
    border-radius: 12px !important;
    border: 2px solid rgba(26,143,140,0.4) !important;
}

/* ── Metric overrides ── */
div[data-testid="stMetric"] {
    background: rgba(26,143,140,0.1);
    border-radius: 14px;
    padding: 14px;
    border: 1px solid rgba(26,143,140,0.25);
}
</style>
""", unsafe_allow_html=True)
