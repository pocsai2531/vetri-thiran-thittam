# ⚡ ComicCraft - AI Comic Story Creator using Gemini Models

ComicCraft is a full-stack, AI-powered web application that automatically generates personalized 5-panel comic books—including storylines, scene descriptions, dialogues, vivid illustrations, and downloadable multi-page PDFs—based on user-provided prompts.

---

## 🚀 Features

- **Gemini Flash (gemini-1.5-flash)**: Rapid structured generation of 5-panel comic outlines, titles, and visual prompts.
- **Gemini Pro (gemini-1.5-pro)**: Deep, creative storytelling crafting atmospheric captions, narration, and character dialogue for each panel.
- **Stable Diffusion & Diffusers**: High-fidelity comic illustrations tailored to scene prompts, with automated fallback synthesizers.
- **FastAPI Backend**: Asynchronous request processing, form handling, and JSON API endpoints.
- **Dynamic Jinja2 Frontend**: Modern, responsive UI with scenic background, panel previews, and real-time loading feedback.
- **FPDF / fpdf2 Integration**: Automated PDF compilation with image placements, narrative typesetting, and timestamped exports.
- **Offline / Zero-Key Fallback Mode**: Works immediately out-of-the-box even before setting up API keys.

---

## 📁 Project Architecture

```
comiccraft/
├── app/
│   ├── __init__.py           # Application package
│   ├── main.py               # FastAPI entry point, static mounting & CORS
│   ├── routes.py             # Route handlers (/generate, /generate-comic/json, /test-image, etc.)
│   ├── gemini_flash.py       # 5-panel outline generation with Gemini 1.5 Flash
│   ├── gemini_pro.py         # Full narrative & dialogue generation with Gemini 1.5 Pro
│   ├── image_generator.py    # Diffusers / HF API / Pollinations / PIL panel illustration
│   ├── layout_builder.py     # Panel assembly and metadata binding
│   └── exporters.py          # Multi-page PDF generation via FPDF
├── templates/
│   ├── index.html            # User input form with scenic background
│   ├── comic_preview.html    # Panel-by-panel preview with download action
│   ├── export_success.html   # Download confirmation page
│   ├── result.html           # Architecture & AI pipeline status
│   └── all_users.html        # Historical records view
├── static/
│   ├── css/
│   │   └── style.css         # Modern design tokens & styles
│   ├── images/
│   │   └── background.jpg    # Scenic background wallpaper
│   ├── panels/               # Generated panel illustrations
│   ├── exports/              # Compiled comic PDF files
│   └── fonts/                # Fonts for PDF generation
├── .env                      # Environment variables (API keys)
├── .env.example              # Template configuration
├── requirements.txt          # Python dependencies
├── run.py                    # Application launcher
└── README.md                 # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure **Python 3.10+** and `pip` are installed on your system.

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv comiccraft-env
comiccraft-env\Scripts\activate

# macOS / Linux
python -m venv comiccraft-env
source comiccraft-env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Edit `.env` and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
HF_API_KEY=your_huggingface_api_key_here
```
> *Tip: You can obtain a free Gemini API key from [Google AI Studio](https://aistudio.google.com/). If no key is provided, ComicCraft runs in fallback demonstration mode!*

---

## 💻 Running the Application

### Option A: Using the Launcher
```bash
python run.py
```

### Option B: Using Uvicorn Directly
```bash
uvicorn app.main:app --reload
```

Once running, access ComicCraft in your browser:
- **Application Homepage**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Image Generation Test Route**: [http://127.0.0.1:8000/test-image](http://127.0.0.1:8000/test-image)

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Loads ComicCraft homepage (`index.html`) |
| `POST` | `/generate` | Accepts form data, runs AI generation pipeline, and renders `comic_preview.html` |
| `POST` | `/generate-comic/json` | Raw JSON API endpoint for external clients |
| `GET` | `/export-success` | Displays PDF download confirmation page |
| `GET` | `/test-image` | Utility endpoint to generate and verify standalone images |
| `GET` | `/result` | Supplementary AI plan overview |
| `GET` | `/all-users` | Supplementary records view |

---

## 🧪 Testing with cURL / JSON API

```bash
curl -X POST "http://127.0.0.1:8000/generate-comic/json" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "A brave fox exploring an enchanted forest.",
       "character_name": "Free",
       "setting": "Forest",
       "tone": "Dramatic",
       "style": "Comic Book"
     }'
```
