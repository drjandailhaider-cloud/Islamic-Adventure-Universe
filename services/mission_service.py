"""
Mission Service — All data embedded directly in Python.
No JSON files required. Works 100% on Streamlit Cloud.
"""


# ── All data hardcoded here — no JSON files needed ───────────────────────────

WORLDS = [
    {"id": "w1", "name": "Desert Journey", "arabic": "رحلة الصحراء", "icon": "🌅",
     "color": "#F4A460", "locked": False,
     "description": "Follow the caravan of wisdom across ancient sands", "xpReward": 170},
    {"id": "w2", "name": "Medina Quest", "arabic": "مدينة النور", "icon": "🕌",
     "color": "#4ECDC4", "locked": False,
     "description": "Walk the blessed city and learn the ways of kindness", "xpReward": 200},
    {"id": "w3", "name": "Ocean of Knowledge", "arabic": "بحر العلم", "icon": "🌊",
     "color": "#87CEEB", "locked": True,
     "description": "Dive deep into the ocean of Islamic scholarship", "xpReward": 250},
    {"id": "w4", "name": "Garden of Jannah", "arabic": "روضة الجنة", "icon": "🌸",
     "color": "#98FB98", "locked": True,
     "description": "Tend the garden of good deeds and virtuous habits", "xpReward": 300},
]

MISSIONS = {
    "w1": [
        {"id": "m1", "title": "The Lost Traveler", "icon": "🧭",
         "value": "Helping Others", "xp": 40,
         "story": "You cross the golden desert when you spot an old man struggling with heavy bags. The caravan is moving fast and you might fall behind...",
         "choices": [
             {"text": "Stop and help him carry his bags",
              "outcome": "You helped the traveler and he blessed you. The Prophet said: The best of people are those most beneficial to others.",
              "positive": True, "xp": 40},
             {"text": "Keep walking — the caravan cannot wait",
              "outcome": "You kept moving but felt uneasy. Sometimes slowing down is the right choice.",
              "positive": False, "xp": 5},
         ]},
        {"id": "m2", "title": "The Merchant Honesty", "icon": "⚖️",
         "value": "Truthfulness", "xp": 45,
         "story": "A merchant gives you extra change by mistake. You realize only after walking away. You have 10 extra coins that are not yours...",
         "choices": [
             {"text": "Return to the merchant and give back the coins",
              "outcome": "SubhanAllah! Your honesty made the merchant cry with joy. Be truthful for truth leads to righteousness.",
              "positive": True, "xp": 45},
             {"text": "Keep the coins — it was his mistake",
              "outcome": "The coins felt heavy in your pocket. Something did not feel right inside.",
              "positive": False, "xp": 5},
         ]},
        {"id": "m3", "title": "The Thirsty Camel", "icon": "🐪",
         "value": "Kindness to Animals", "xp": 35,
         "story": "Your camel is thirsty and there is water ahead, but a stray dog whimpers nearby with no one to care for it...",
         "choices": [
             {"text": "Share some water with the dog too",
              "outcome": "A woman was once forgiven all her sins for giving water to a thirsty dog. You earned great reward!",
              "positive": True, "xp": 35},
             {"text": "Use all water for your camel only",
              "outcome": "Your camel was satisfied, but you passed a chance to earn great reward.",
              "positive": False, "xp": 5},
         ]},
        {"id": "m4", "title": "Patience at Dawn", "icon": "🌅",
         "value": "Patience and Salah", "xp": 50,
         "story": "Fajr time arrives. You are exhausted from the long desert journey. Your blanket is warm and the sand is cold...",
         "choices": [
             {"text": "Wake up, make wudu, and pray Fajr",
              "outcome": "Allahu Akbar! Two rakats at Fajr are better than the world and all it contains. Your heart feels light.",
              "positive": True, "xp": 50},
             {"text": "Sleep a little more and pray later",
              "outcome": "You missed the blessing of Fajr time. Tomorrow try harder. Every dawn is a new chance.",
              "positive": False, "xp": 5},
         ]},
    ],
    "w2": [
        {"id": "m5", "title": "The Neighbor's Need", "icon": "🏠",
         "value": "Neighborly Kindness", "xp": 45,
         "story": "Your neighbor knocks. Her family has not eaten today. You have just enough food for your family...",
         "choices": [
             {"text": "Share half your food with her family",
              "outcome": "He is not a believer who eats his fill while his neighbor goes hungry. You chose the way of the Prophet.",
              "positive": True, "xp": 45},
             {"text": "Say you do not have enough and close the door",
              "outcome": "That night your meal did not taste as good as it should. Generosity multiplies blessings.",
              "positive": False, "xp": 5},
         ]},
        {"id": "m6", "title": "The Angry Friend", "icon": "😤",
         "value": "Controlling Anger", "xp": 40,
         "story": "Your best friend broke your favourite toy by accident. You feel very angry. What do you do?",
         "choices": [
             {"text": "Take a deep breath and forgive him",
              "outcome": "The Prophet said: The strong person is not the one who can wrestle but the one who controls themselves when angry.",
              "positive": True, "xp": 40},
             {"text": "Yell at him and walk away",
              "outcome": "Your friend cried. Anger rarely solves things and often breaks what we love most.",
              "positive": False, "xp": 5},
         ]},
    ],
    "w3": [],
    "w4": [],
}

LEVELS = [
    {"level": 1, "name": "Little Seeker",  "icon": "🌱", "xpNeeded": 0},
    {"level": 2, "name": "Young Learner",  "icon": "📖", "xpNeeded": 100},
    {"level": 3, "name": "Desert Walker",  "icon": "🚶", "xpNeeded": 250},
    {"level": 4, "name": "Brave Explorer", "icon": "🧭", "xpNeeded": 450},
    {"level": 5, "name": "Light Bearer",   "icon": "✨", "xpNeeded": 700},
    {"level": 6, "name": "Wisdom Keeper",  "icon": "📜", "xpNeeded": 1000},
    {"level": 7, "name": "Star Guardian",  "icon": "⭐", "xpNeeded": 1400},
    {"level": 8, "name": "Jannah Seeker",  "icon": "🌟", "xpNeeded": 2000},
]

BADGES = [
    {"id": "b1", "name": "First Step",   "icon": "👣", "desc": "Completed your first mission",   "xpRequired": 0},
    {"id": "b2", "name": "Truth Seeker", "icon": "🔍", "desc": "Made 3 honest choices",          "xpRequired": 100},
    {"id": "b3", "name": "Desert Hero",  "icon": "🏆", "desc": "Completed Desert Journey world", "xpRequired": 170},
    {"id": "b4", "name": "Kind Heart",   "icon": "💚", "desc": "Helped 5 characters in stories", "xpRequired": 200},
    {"id": "b5", "name": "Scholar",      "icon": "📚", "desc": "Learned 10 Islamic values",      "xpRequired": 350},
    {"id": "b6", "name": "Guardian",     "icon": "🛡️", "desc": "Reached Level 5",               "xpRequired": 500},
]


# ── Service class ─────────────────────────────────────────────────────────────

class MissionService:

    @staticmethod
    def get_worlds() -> list:
        return WORLDS

    @staticmethod
    def get_missions(world_id: str) -> list:
        return MISSIONS.get(world_id, [])

    @staticmethod
    def get_mission(world_id: str, mission_id: str) -> dict | None:
        return next((m for m in MissionService.get_missions(world_id) if m["id"] == mission_id), None)

    @staticmethod
    def get_levels() -> list:
        return LEVELS

    @staticmethod
    def get_badges() -> list:
        return BADGES

    @staticmethod
    def get_current_level(xp: int) -> dict:
        current = LEVELS[0]
        for lvl in LEVELS:
            if xp >= lvl["xpNeeded"]:
                current = lvl
        return current

    @staticmethod
    def get_next_level(xp: int) -> dict | None:
        for lvl in LEVELS:
            if xp < lvl["xpNeeded"]:
                return lvl
        return None

    @staticmethod
    def get_level_progress(xp: int) -> int:
        current_xp_needed = 0
        next_xp_needed = None
        for i, lvl in enumerate(LEVELS):
            if xp >= lvl["xpNeeded"]:
                current_xp_needed = lvl["xpNeeded"]
                if i + 1 < len(LEVELS):
                    next_xp_needed = LEVELS[i + 1]["xpNeeded"]
        if next_xp_needed is None:
            return 100
        span = next_xp_needed - current_xp_needed
        earned = xp - current_xp_needed
        return min(100, int((earned / span) * 100)) if span > 0 else 100

    @staticmethod
    def count_world_completed(world_id: str, completed_missions: list) -> tuple[int, int]:
        missions = MissionService.get_missions(world_id)
        total = len(missions)
        done = sum(1 for m in missions if m["id"] in completed_missions)
        return done, total
