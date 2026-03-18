"""
Reward Service — Badge evaluation and XP calculation.
"""
import json
from pathlib import Path

BADGES_FILE = Path("data/rewards/badges.json")


def _load_badges():
    with open(BADGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


class RewardService:

    @staticmethod
    def evaluate_new_badges(current_xp: int, new_xp: int,
                            earned_badge_ids: list) -> list:
        """Return list of newly unlocked badge dicts."""
        badges = _load_badges()
        new_badges = []
        for badge in badges:
            already_earned = badge["id"] in earned_badge_ids
            now_qualifies = new_xp >= badge["xpRequired"]
            not_previously = current_xp < badge["xpRequired"]
            if not already_earned and now_qualifies and not_previously:
                new_badges.append(badge)
        return new_badges

    @staticmethod
    def get_all_badges() -> list:
        return _load_badges()

    @staticmethod
    def get_earned_badges(badge_ids: list) -> list:
        all_badges = _load_badges()
        return [b for b in all_badges if b["id"] in badge_ids]
