import os
import re
from datetime import datetime
from fpdf import FPDF

EXPORT_FOLDER = os.path.join("static", "exports")
FONTS_FOLDER = os.path.join("static", "fonts")
os.makedirs(EXPORT_FOLDER, exist_ok=True)
os.makedirs(FONTS_FOLDER, exist_ok=True)


def clean_unicode_for_pdf(text: str) -> str:
    """Replaces non-latin1 unicode characters with safe ascii equivalents."""
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2014": " - ",
        "\u2013": "-",
        "\u2026": "...",
        "\u00a0": " ",
        "•": "*",
        "⚡": "[*]",
        "📖": "[Comic]",
        "✔": "[OK]",
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    # Strip any remaining unencodable characters
    return text.encode("latin-1", "replace").decode("latin-1")


def save_pdf(layout: list) -> str:
    """
    Compiles the full comic into a multi-page PDF file using the FPDF library.
    Each panel's image and narration are placed neatly on separate pages.

    Args:
        layout (list): List of panel dictionaries with metadata and image paths.

    Returns:
        str: Filepath to the saved PDF in static/exports/.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Check for Unicode font if available
    font_name = "Helvetica"
    dejavu_path = os.path.join(FONTS_FOLDER, "DejaVuSans.ttf")
    if os.path.exists(dejavu_path):
        try:
            pdf.add_font("DejaVu", "", dejavu_path, uni=True)
            font_name = "DejaVu"
        except Exception:
            font_name = "Helvetica"

    for panel in layout:
        image_path = panel.get("image_path", "")
        # Normalize local filesystem path for image loading
        if image_path.startswith("/"):
            image_path = image_path.lstrip("/")
        image_path = image_path.replace("/", os.sep)

        story_text = panel.get("text", "")
        panel_num = panel.get("panel", 1)
        panel_title = panel.get("title", f"Panel {panel_num}")

        pdf.add_page()

        # Panel title (centered, 14pt)
        pdf.set_font(font_name, "B" if font_name == "Helvetica" else "", 14)
        title_str = clean_unicode_for_pdf(f"Panel {panel_num}: {panel_title}")
        pdf.cell(0, 10, title_str, ln=True, align="C")

        # Image placement
        y_image = 25
        image_height = 105
        spacing_after_image = 12

        if os.path.exists(image_path):
            try:
                pdf.image(image_path, x=15, y=y_image, w=pdf.w - 30, h=image_height)
            except Exception as img_err:
                pdf.set_y(y_image)
                pdf.set_font(font_name, "", 10)
                pdf.multi_cell(0, 8, clean_unicode_for_pdf(f"[Illustration: {panel.get('image_prompt', 'Comic Scene')}]"))
        else:
            pdf.set_y(y_image)
            pdf.set_font(font_name, "", 10)
            pdf.multi_cell(0, 8, clean_unicode_for_pdf(f"Image placeholder: {panel.get('image_prompt', image_path)}"))

        # Text placement below image
        pdf.set_y(y_image + image_height + spacing_after_image)

        # Scene description if present
        scene_desc = panel.get("scene_description", "")
        if scene_desc:
            pdf.set_font(font_name, "I" if font_name == "Helvetica" else "", 10)
            pdf.multi_cell(0, 6, clean_unicode_for_pdf(f"Scene: {scene_desc}"))
            pdf.ln(3)

        # Narrative / dialogue text
        pdf.set_font(font_name, "", 11)
        story_lines = story_text.strip().splitlines()
        # Remove title line if it was repeated
        if story_lines and story_lines[0].strip().lower().startswith(("**panel", "panel")):
            story_lines = story_lines[1:]
        cleaned_text = "\n".join(story_lines).strip()
        pdf.multi_cell(0, 7, clean_unicode_for_pdf(cleaned_text))

    # Save with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"comic_{timestamp}.pdf"
    pdf_path = os.path.join(EXPORT_FOLDER, filename)
    pdf.output(pdf_path)

    # Return web-friendly path
    return pdf_path.replace("\\", "/")
