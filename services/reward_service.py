"""
Reward Service — Uses embedded badge data from MissionService.
No JSON files required.
"""
from services.mission_service import MissionService


class RewardService:

    @staticmethod
    def evaluate_new_badges(current_xp: int, new_xp: int,
                            earned_badge_ids: list) -> list:
        new_badges = []
        for badge in MissionService.get_badges():
            already_earned = badge["id"] in earned_badge_ids
            now_qualifies  = new_xp >= badge["xpRequired"]
            not_previously = current_xp < badge["xpRequired"]
            if not already_earned and now_qualifies and not_previously:
                new_badges.append(badge)
        return new_badges

    @staticmethod
    def get_all_badges() -> list:
        return MissionService.get_badges()

    @staticmethod
    def get_earned_badges(badge_ids: list) -> list:
        return [b for b in MissionService.get_badges() if b["id"] in badge_ids]
