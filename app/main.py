import os
import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.image_generator import bootstrap_assets

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("comiccraft")

# Initialize FastAPI App
app = FastAPI(
    title="ComicCraft - AI Comic Story Creator",
    description="Web application using Google Gemini Models and Stable Diffusion to generate personalized comic books.",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure required directories exist
for folder in ["static/panels", "static/exports", "static/fonts", "static/images", "static/css"]:
    os.makedirs(folder, exist_ok=True)

# Bootstrap starter assets if available
bootstrap_assets()

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Application Routes
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logger.info("ComicCraft server starting up...")
    logger.info("Access the application at http://127.0.0.1:8000")
    logger.info("Interactive API docs at http://127.0.0.1:8000/docs")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
