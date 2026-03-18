"""
Mission Service — Loads worlds, missions, checks completion state.
"""
import json
from pathlib import Path

WORLDS_FILE  = Path("data/worlds.json")
MISSIONS_FILE = Path("data/missions/missions.json")
LEVELS_FILE  = Path("data/levels.json")


def _load_json(path: Path) -> any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class MissionService:

    @staticmethod
    def get_worlds() -> list:
        return _load_json(WORLDS_FILE)

    @staticmethod
    def get_missions(world_id: str) -> list:
        all_missions = _load_json(MISSIONS_FILE)
        return all_missions.get(world_id, [])

    @staticmethod
    def get_mission(world_id: str, mission_id: str) -> dict | None:
        missions = MissionService.get_missions(world_id)
        return next((m for m in missions if m["id"] == mission_id), None)

    @staticmethod
    def get_levels() -> list:
        return _load_json(LEVELS_FILE)

    @staticmethod
    def get_current_level(xp: int) -> dict:
        levels = MissionService.get_levels()
        current = levels[0]
        for lvl in levels:
            if xp >= lvl["xpNeeded"]:
                current = lvl
        return current

    @staticmethod
    def get_next_level(xp: int) -> dict | None:
        levels = MissionService.get_levels()
        for i, lvl in enumerate(levels):
            if xp < lvl["xpNeeded"]:
                return lvl
        return None

    @staticmethod
    def get_level_progress(xp: int) -> int:
        """Returns progress % to next level (0-100)."""
        levels = MissionService.get_levels()
        current_xp_needed = 0
        next_xp_needed = None
        for i, lvl in enumerate(levels):
            if xp >= lvl["xpNeeded"]:
                current_xp_needed = lvl["xpNeeded"]
                if i + 1 < len(levels):
                    next_xp_needed = levels[i + 1]["xpNeeded"]
        if next_xp_needed is None:
            return 100
        span = next_xp_needed - current_xp_needed
        earned = xp - current_xp_needed
        return min(100, int((earned / span) * 100)) if span > 0 else 100

    @staticmethod
    def count_world_completed(world_id: str, completed_missions: list) -> tuple[int, int]:
        """Returns (completed, total) for a world."""
        missions = MissionService.get_missions(world_id)
        total = len(missions)
        done = sum(1 for m in missions if m["id"] in completed_missions)
        return done, total
