# Data Flow Diagram - ComicCraft AI

| Field         | Details                                                    |
| ------------- | ---------------------------------------------------------- |
| Date          | 30-09-2026                                                 |
| Team ID       | SWTID-2026-6831                                            |
| Project Name  | ComicCraft AI - AI Comic Story Creator using Gemini Models |
| Team Size     | 5                                                          |
| Team Leader   | Poornima K K                                               |
| Team Members  | Hemalatha S, Tharani S, Mohana, Sabarivasan                |
| Maximum Marks | 4 Marks                                                    |

## Data Flow

| Flow | From               | Process                                              | To                 |
| ---- | ------------------ | ---------------------------------------------------- | ------------------ |
| 1    | User               | Submits story idea, genre, style and panel count     | Web application    |
| 2    | Web application    | Sends the request to the backend                     | Flask backend      |
| 3    | Backend            | Sends a scripting prompt                             | Gemini text model  |
| 4    | Gemini text model  | Returns scenes, dialogues and character descriptions | Backend            |
| 5    | Backend            | Sends each scene description as an image prompt      | Gemini image model |
| 6    | Gemini image model | Returns a panel image                                | Backend            |
| 7    | Backend            | Combines images with speech bubbles and captions     | User (preview)     |
| 8    | User               | Edits and exports the comic                          | PDF or PNG file    |

## User Stories

| User Type | Functional Requirement | User Story No. | User Story / Task                                         | Acceptance Criteria               | Priority | Release  |
| --------- | ---------------------- | -------------- | --------------------------------------------------------- | --------------------------------- | -------- | -------- |
| Customer  | FR-1                   | USN-1          | As a user, I can enter a story idea and choose a style    | Input is accepted and saved       | High     | Sprint-1 |
| Customer  | FR-2                   | USN-2          | As a user, I get a comic script with scenes and dialogues | Script matches the story idea     | High     | Sprint-1 |
| Customer  | FR-3                   | USN-3          | As a user, I see an image for every panel                 | One image is generated per scene  | High     | Sprint-2 |
| Customer  | FR-4                   | USN-4          | As a user, I see speech bubbles and captions on panels    | Text appears on the correct panel | High     | Sprint-2 |
| Customer  | FR-5                   | USN-5          | As a user, I can edit dialogue and regenerate one panel   | Change is saved and shown         | Medium   | Sprint-3 |
| Customer  | FR-6                   | USN-6          | As a user, I can download my comic                        | PDF or PNG downloads successfully | Medium   | Sprint-3 |
