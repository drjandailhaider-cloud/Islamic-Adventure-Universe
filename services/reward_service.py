"""
Reward Service — Badge evaluation and XP calculation.
Embedded fallback in case badges.json is missing or empty.
"""
import json
from pathlib import Path

BADGES_FILE = Path("data/rewards/badges.json")

_FALLBACK_BADGES = [
    {"id": "b1", "name": "First Step",   "icon": "👣", "desc": "Completed your first mission",      "xpRequired": 0},
    {"id": "b2", "name": "Truth Seeker", "icon": "🔍", "desc": "Made 3 honest choices",             "xpRequired": 100},
    {"id": "b3", "name": "Desert Hero",  "icon": "🏆", "desc": "Completed Desert Journey world",    "xpRequired": 170},
    {"id": "b4", "name": "Kind Heart",   "icon": "💚", "desc": "Helped 5 characters in stories",    "xpRequired": 200},
    {"id": "b5", "name": "Scholar",      "icon": "📚", "desc": "Learned 10 Islamic values",         "xpRequired": 350},
    {"id": "b6", "name": "Guardian",     "icon": "🛡️", "desc": "Reached Level 5",                  "xpRequired": 500},
]


def _load_badges() -> list:
    """Load badges safely with fallback."""
    try:
        if BADGES_FILE.exists():
            content = BADGES_FILE.read_text(encoding="utf-8").strip()
            if content:
                return json.loads(content)
    except Exception:
        pass
    return _FALLBACK_BADGES


class RewardService:

    @staticmethod
    def evaluate_new_badges(current_xp: int, new_xp: int,
                            earned_badge_ids: list) -> list:
        """Return list of newly unlocked badge dicts."""
        badges = _load_badges()
        new_badges = []
        for badge in badges:
            already_earned = badge["id"] in earned_badge_ids
            now_qualifies  = new_xp >= badge["xpRequired"]
            not_previously = current_xp < badge["xpRequired"]
            if not already_earned and now_qualifies and not_previously:
                new_badges.append(badge)
        return new_badges

    @staticmethod
    def get_all_badges() -> list:
        return _load_badges()

    @staticmethod
    def get_earned_badges(badge_ids: list) -> list:
        return [b for b in _load_badges() if b["id"] in badge_ids]
