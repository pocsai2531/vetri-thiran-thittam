import logging

logger = logging.getLogger("comiccraft.layout_builder")


def build_comic_layout(image_paths: list, full_story: str, outline: list) -> list:
    """
    Organizes the generated images and full comic story into a structured layout.

    Args:
        image_paths (list): List of paths to generated panel images.
        full_story (str): Complete narrative text generated for all panels.
        outline (list): 5-panel outline dictionaries containing title and scene_description.

    Returns:
        list: Structured list of panel dictionaries with metadata, image paths, and story narration.
    """
    # Split the full story into individual panel segments
    story_panels = []
    if "**Panel" in full_story:
        raw_panels = full_story.split("**Panel")
        story_panels = [f"**Panel{p}" for p in raw_panels if p.strip()]
    elif "Panel " in full_story:
        raw_panels = full_story.split("Panel ")
        story_panels = [f"Panel {p}" for p in raw_panels if p.strip()]

    # If story split didn't match the number of panels in the outline, distribute or fallback
    if len(story_panels) != len(outline):
        logger.warning(
            f"Split story count ({len(story_panels)}) does not match outline count ({len(outline)}). Distributing."
        )
        if len(story_panels) < len(outline):
            # Pad with default narration from outline descriptions
            while len(story_panels) < len(outline):
                i = len(story_panels)
                panel_info = outline[i] if i < len(outline) else {}
                title = panel_info.get("title", f"Panel {i+1}")
                desc = panel_info.get("scene_description", "")
                story_panels.append(
                    f"**Panel {i+1}: {title}**\n**CAPTION:** The journey continues...\n**NARRATION:** {desc}"
                )

    layout = []
    for idx, (image, text, panel_info) in enumerate(zip(image_paths, story_panels, outline), start=1):
        # Extract title and body text
        lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
        if lines and lines[0].lower().startswith(("**panel", "panel")):
            body_text = "\n".join(lines[1:]).strip()
        else:
            body_text = "\n".join(lines).strip()

        # Parse specific subfields for rich UI display if present
        caption = ""
        narration = ""
        dialogue = ""

        for line in lines:
            if line.upper().startswith("**CAPTION:**") or line.upper().startswith("CAPTION:"):
                caption = line.split(":", 1)[1].strip()
            elif line.upper().startswith("**NARRATION:**") or line.upper().startswith("NARRATION:"):
                narration = line.split(":", 1)[1].strip()
            elif line.upper().startswith("**DIALOGUE:**") or line.upper().startswith("DIALOGUE:"):
                dialogue = line.split(":", 1)[1].strip()

        # Default fallbacks if not explicitly marked
        if not narration and body_text:
            narration = body_text

        title = panel_info.get("title", f"Panel {idx}")
        # Clean title if it contains "Panel X:" prefix
        if title.lower().startswith(f"panel {idx}:"):
            title = title[len(f"panel {idx}:"):].strip()

        layout.append({
            "panel": idx,
            "title": title,
            "image_path": image,
            "text": body_text,
            "caption": caption,
            "narration": narration,
            "dialogue": dialogue,
            "scene_description": panel_info.get("scene_description", ""),
            "image_prompt": panel_info.get("image_prompt", "")
        })

    return layout
