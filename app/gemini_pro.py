import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("comiccraft.gemini_pro")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

CANDIDATE_PRO_MODELS = [
    "gemini-3.8-pro",
    "gemini-3.8-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-pro"
]

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        logger.warning(f"Could not configure genai for Pro: {e}")


def generate_fallback_story(outline: list) -> str:
    """Provides a polished narrative story when Gemini API is unavailable."""
    story_parts = []
    for idx, panel in enumerate(outline, start=1):
        title = panel.get("title", f"Panel {idx}")
        desc = panel.get("scene_description", "The journey unfolds before our hero.")
        part = f"""**Panel {idx}: {title}**
*Scene:* {desc}
**CAPTION:** Shadows stretched long across the terrain as destiny set its gears into motion.
**NARRATION:** With steadfast resolve, our hero took the decisive first steps, sensing the ancient mysteries lingering in the quiet air.
**DIALOGUE:** "Whatever answers lie waiting... I will uncover the truth!"
"""
        story_parts.append(part)
    return "\n\n".join(story_parts)


def generate_story(outline: list) -> str:
    """
    Generates a detailed comic story with narration and character dialogue
    from a list of comic panel outlines using Gemini models.

    Args:
        outline (list): A list of dictionaries representing each comic panel's idea.

    Returns:
        str: The generated comic story text or an error message.
    """
    formatted_outline_items = []
    for i, item in enumerate(outline):
        if isinstance(item, dict):
            panel_text = f"Panel {item.get('panel', i+1)}: {item.get('title', '')} - {item.get('scene_description', '')}"
        else:
            panel_text = str(item)
        formatted_outline_items.append(f"{i+1}. {panel_text}")

    formatted_outline = "\n".join(formatted_outline_items)

    prompt = f"""
You're a comic book writer.

Given the following panel breakdown, write a comic-style story with engaging narration and character dialogues for each panel.

Panel Outline:
{formatted_outline}

Guidelines:
- Use a fun and engaging tone, like an actual comic book.
- For EVERY panel, start strictly with a line in the exact format:
  **Panel [number]: [Panel Title]**
- Include:
  **CAPTION:** (ambient atmosphere or setting mood)
  **NARRATION:** (detailed narration of character's thoughts and actions)
  **DIALOGUE:** (clearly marked character lines with quotes)
- Keep each panel self-contained but part of a cohesive 5-panel story arc.
"""

    if not GEMINI_API_KEY:
        logger.info("Gemini API key not configured; using default story generation.")
        return generate_fallback_story(outline)

    for m_name in CANDIDATE_PRO_MODELS:
        try:
            m = genai.GenerativeModel(m_name)
            response = m.generate_content(prompt)
            text = response.text.strip()
            if text and ("**Panel" in text or "Panel " in text):
                print(f"[OK] Generated story with {m_name}")
                return text
        except Exception as e:
            logger.warning(f"Pro model {m_name} failed: {e}")
            continue

    return generate_fallback_story(outline)
