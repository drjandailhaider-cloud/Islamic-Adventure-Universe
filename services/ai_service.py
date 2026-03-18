"""
AI Service — Claude API integration for dynamic story generation.
Falls back to rule-based stories when API key is unavailable.
"""
import os
from pathlib import Path

try:
    import anthropic
    _HAS_ANTHROPIC = True
except ImportError:
    _HAS_ANTHROPIC = False

_FALLBACK_STORIES = [
    "Your wise decision echoes through the adventure world. The desert winds carry your good deed across the golden dunes, and the stars above shine a little brighter tonight. Remember: every act of kindness plants a seed in the garden of your character. MashaAllah, brave explorer — continue your journey!",
    "The angels record your righteous choice in the Book of Deeds. As you walk forward, you notice the path ahead becomes clearer and more beautiful. Your heart feels lighter, filled with the warmth that only comes from doing what is right. Keep shining your light, young hero!",
    "SubhanAllah — your good action ripples outward like water in a still pond, touching lives you cannot even see. The Companions of the Prophet faced similar choices and chose the righteous path, just as you have. Walk forward with your head held high!",
]

_story_index = 0


class AIService:

    @staticmethod
    def generate_story(child_name: str, mission_title: str, world_name: str,
                       choice_text: str, islamic_value: str) -> str:
        """Generate a personalized story continuation using Claude API."""

        # Try Claude API first
        api_key = os.getenv("ANTHROPIC_API_KEY", "")
        if _HAS_ANTHROPIC and api_key and not api_key.startswith("sk-ant-YOUR"):
            try:
                client = anthropic.Anthropic(api_key=api_key)
                model = os.getenv("AI_MODEL", "claude-haiku-4-5-20251001")
                max_tokens = int(os.getenv("AI_MAX_TOKENS", "400"))

                prompt = f"""You are a kind Islamic storyteller for children aged 5-15.
Child named {child_name} completed mission "{mission_title}" in "{world_name}" adventure world.
They chose: "{choice_text}"
Islamic value learned: {islamic_value}

Write a SHORT (3-4 sentence) magical adventure continuation.
Rules:
- Simple beautiful language a child loves
- Mention one hadith/Quranic concept briefly (no full text)
- End with warm encouragement
- Feel like a real adventure continuing
- Purely educational and inspirational
- No inappropriate content whatsoever"""

                message = client.messages.create(
                    model=model,
                    max_tokens=max_tokens,
                    messages=[{"role": "user", "content": prompt}],
                )
                return message.content[0].text.strip()
            except Exception:
                pass  # Fall through to fallback

        # Rule-based fallback
        global _story_index
        story = _FALLBACK_STORIES[_story_index % len(_FALLBACK_STORIES)]
        _story_index += 1
        return story
