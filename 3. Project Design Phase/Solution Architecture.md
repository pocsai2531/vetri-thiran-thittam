# Solution Architecture - ComicCraft AI

| Field         | Details                                                    |
| ------------- | ---------------------------------------------------------- |
| Date          | 30-09-2026                                                 |
| Team ID       | SWTID-2026-6831                                            |
| Project Name  | ComicCraft AI - AI Comic Story Creator using Gemini Models |
| Team Size     | 5                                                          |
| Team Leader   | Poornima K K                                               |
| Team Members  | Hemalatha S, Tharani S, Mohana, Sabarivasan                |
| Maximum Marks | 4 Marks                                                    |

| Layer        | Component                 | Function                                                     |
| ------------ | ------------------------- | ------------------------------------------------------------ |
| Presentation | Web UI                    | Story input, preview, editing and download                   |
| Application  | Flask backend             | Coordinates the pipeline and handles requests                |
| AI (text)    | Gemini text model         | Creates script, scenes, dialogues and character descriptions |
| AI (image)   | Gemini image model        | Generates panel images                                       |
| Processing   | Layout engine (Pillow)    | Places panels, speech bubbles and captions                   |
| Data         | SQLite database           | Stores users and saved comics                                |
| Output       | Export module (ReportLab) | Creates PDF and PNG files                                    |
