import os
import traceback
import logging
from typing import Optional
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

logger = logging.getLogger("comiccraft.routes")

router = APIRouter()
templates = Jinja2Templates(directory="templates")


class PromptRequest(BaseModel):
    prompt: str
    character_name: Optional[str] = "Finn"
    setting: Optional[str] = "enchanted forest"
    tone: Optional[str] = "dramatic"
    style: Optional[str] = "comic book"


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Loads the homepage where users can submit story details."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "ComicCraft - AI Comic Story Creator"}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    style: str = Form(...)
):
    """
    Handles form submission, processes the input using AI models,
    generates comic panels, and returns the comic preview page.
    """
    try:
        # Combine user input into a single full prompt as specified in documentation
        full_prompt = (
            f"{prompt}\n"
            f"The main character is {character_name}.\n"
            f"The setting is a {setting}.\n"
            f"The tone is {tone}. The art style is {style}."
        )

        logger.info(f"Generating comic for prompt: {full_prompt[:100]}...")

        # Step 1: Generate panel outline using Gemini Flash
        outline = generate_outline(full_prompt)
        if not isinstance(outline, list) or not all("image_prompt" in panel for panel in outline):
            raise ValueError("Invalid outline structure from Gemini response.")

        # Step 2: Generate story narration and dialogue using Gemini Pro
        full_story = generate_story(outline)

        # Step 3: Generate images for each panel
        images = [generate_image(panel["image_prompt"]) for panel in outline]

        # Step 4: Build layout structure
        layout = build_comic_layout(images, full_story, outline)

        # Step 5: Export to PDF using FPDF
        pdf_path = save_pdf(layout)
        web_pdf_path = "/" + pdf_path.replace("\\", "/").lstrip("/")

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "layout": layout,
                "pdf_path": web_pdf_path,
                "character_name": character_name,
                "setting": setting,
                "tone": tone,
                "style": style,
                "prompt": prompt
            }
        )

    except Exception as e:
        traceback.print_exc()
        logger.error(f"Error during comic generation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-comic/json")
async def generate_comic_json(req: PromptRequest):
    """
    JSON API route that accepts JSON payloads, triggers comic generation,
    and returns comic layout data along with the generated PDF path.
    """
    try:
        full_prompt = (
            f"{req.prompt}\n"
            f"The main character is {req.character_name}.\n"
            f"The setting is a {req.setting}.\n"
            f"The tone is {req.tone}. The art style is {req.style}."
        )

        outline = generate_outline(full_prompt)
        if not isinstance(outline, list) or not all("image_prompt" in panel for panel in outline):
            raise ValueError("Invalid outline structure.")

        full_story = generate_story(outline)
        images = [generate_image(panel["image_prompt"]) for panel in outline]
        layout = build_comic_layout(images, full_story, outline)
        pdf_path = save_pdf(layout)
        web_pdf_path = "/" + pdf_path.replace("\\", "/").lstrip("/")

        return JSONResponse({
            "status": "success",
            "layout": layout,
            "pdf_path": web_pdf_path
        })
    except Exception as e:
        logger.error(f"API generation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request, pdf_path: str):
    """Displays a success confirmation page after the comic is downloaded."""
    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={"pdf_path": pdf_path}
    )


@router.get("/test-image")
async def test_image(prompt: str = "A futuristic city at sunset, sci-fi, cinematic, artstation"):
    """Developer utility route to test image generation from a direct prompt."""
    try:
        image_path = generate_image(prompt)
        web_path = "/" + image_path.replace("\\", "/").lstrip("/")
        return {"message": "Image generated successfully", "path": web_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/result", response_class=HTMLResponse)
async def result_view(request: Request):
    """Supplementary view for AI generation plan as referenced in documentation."""
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={}
    )


@router.get("/all-users", response_class=HTMLResponse)
async def all_users_view(request: Request):
    """Supplementary view for administrative / user records."""
    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={}
    )
