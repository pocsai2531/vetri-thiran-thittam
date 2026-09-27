import os
import json
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("comiccraft.gemini_flash")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

CANDIDATE_FLASH_MODELS = [
    "gemini-3.8-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-pro"
]

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        logger.warning(f"Could not configure genai: {e}")


def generate_fallback_outline(user_prompt: str) -> list:
    """Provides a coherent 5-panel outline when API key is missing or model fails."""
    hero = "Finn"
    p_lower = user_prompt.lower()
    if "main character is" in p_lower:
        try:
            hero = p_lower.split("main character is")[1].split(".")[0].strip().title()
        except Exception:
            pass

    return [
        {
            "panel": 1,
            "title": f"The Journey Begins: {hero}'s Call to Adventure",
            "scene_description": f"{hero} stands at the edge of the unknown world, gazing into the horizon with quiet courage and anticipation.",
            "image_prompt": f"Comic book style illustration, {hero} looking resolute at the threshold of a mysterious scenic landscape, golden atmospheric rim lighting, dramatic framing."
        },
        {
            "panel": 2,
            "title": "Into the Deep Wilds",
            "scene_description": f"{hero} navigates through dense, wondrous terrain where hidden bioluminescent signs and ancient whispers guide the way.",
            "image_prompt": f"Comic art, {hero} exploring a vibrant mystical path surrounded by towering ancient flora, soft glowing lanterns, cinematic shadows, detailed line art."
        },
        {
            "panel": 3,
            "title": "The Ancient Discovery",
            "scene_description": f"In a secluded clearing, {hero} uncovers an ancient carved monument pulsing with otherworldly arcane light.",
            "image_prompt": f"Vivid comic panel, {hero} marveling at a towering ancient stone monolith etched with glowing blue runes, magical floating dust, breathtaking perspective."
        },
        {
            "panel": 4,
            "title": "The Mysterious Guide",
            "scene_description": f"An ethereal guide appears from the branches above, sharing a cryptic secret about the ancient relic.",
            "image_prompt": f"Graphic novel style, a glowing celestial spirit animal perched gracefully on a branch speaking to {hero}, starlight effects, expressive comic composition."
        },
        {
            "panel": 5,
            "title": "A New Dawn Awakens",
            "scene_description": f"With newfound clarity and triumph, {hero} stands proudly at the summit as morning light illuminates the vast kingdom below.",
            "image_prompt": f"Epic comic finale panel, {hero} standing victoriously on a high cliff overlooking an expansive radiant valley at sunrise, vibrant warm colors, heroic pose."
        }
    ]


def generate_outline(user_prompt: str) -> list:
    """
    Generates a 5-panel comic layout based on the user's story idea using Gemini.

    Args:
        user_prompt (str): The user's comic idea prompt.

    Returns:
        list: A list of dictionaries, one for each panel.
    """
    prompt = f"""
You are a professional AI comic planner.

Your task is to generate a *strictly formatted* JSON array containing 5 panel descriptions for a comic based on the story idea below:

STORY: "{user_prompt}"

Each JSON object must include:
- "panel": (integer 1 to 5)
- "title": (string)
- "scene_description": (string)
- "image_prompt": (string describing the scene visually for image generation, including style, lighting, character details)

Respond ONLY in this valid JSON format, without any explanations or markdown:
[
  {{
    "panel": 1,
    "title": "Title here",
    "scene_description": "Scene description here",
    "image_prompt": "Image prompt for Stable Diffusion"
  }},
  {{
    "panel": 2,
    "title": "Title here",
    "scene_description": "Scene description here",
    "image_prompt": "Image prompt for Stable Diffusion"
  }},
  {{
    "panel": 3,
    "title": "Title here",
    "scene_description": "Scene description here",
    "image_prompt": "Image prompt for Stable Diffusion"
  }},
  {{
    "panel": 4,
    "title": "Title here",
    "scene_description": "Scene description here",
    "image_prompt": "Image prompt for Stable Diffusion"
  }},
  {{
    "panel": 5,
    "title": "Title here",
    "scene_description": "Scene description here",
    "image_prompt": "Image prompt for Stable Diffusion"
  }}
]
"""
    if not GEMINI_API_KEY:
        logger.info("Gemini API key not configured; using high quality fallback outline.")
        return generate_fallback_outline(user_prompt)

    output_text = None
    for m_name in CANDIDATE_FLASH_MODELS:
        try:
            m = genai.GenerativeModel(m_name)
            response = m.generate_content(prompt)
            output_text = response.text.strip()
            print(f"\n[OK] Generated outline with {m_name}")
            break
        except Exception as e:
            logger.warning(f"Flash model {m_name} failed: {e}")
            continue

    if not output_text:
        return generate_fallback_outline(user_prompt)

    try:
        if output_text.startswith("```json"):
            output_text = output_text.replace("```json", "", 1)
        if output_text.startswith("```"):
            output_text = output_text.replace("```", "", 1)
        if output_text.endswith("```"):
            output_text = output_text[:-3]
        output_text = output_text.strip()

        panel_data = json.loads(output_text)

        if not isinstance(panel_data, list):
            raise ValueError("Gemini response is not a list.")

        for panel in panel_data:
            if not isinstance(panel, dict) or not all(key in panel for key in ("panel", "title", "scene_description", "image_prompt")):
                raise ValueError(f"Invalid panel format or missing keys: {panel}")

        return panel_data

    except Exception as e:
        print("X Parse Error:", e)
        return generate_fallback_outline(user_prompt)
