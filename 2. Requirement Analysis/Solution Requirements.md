# Solution Requirements - ComicCraft AI

| Field         | Details                                                    |
| ------------- | ---------------------------------------------------------- |
| Date          | 30-09-2026                                                 |
| Team ID       | SWTID-2026-6831                                            |
| Project Name  | ComicCraft AI - AI Comic Story Creator using Gemini Models |
| Team Size     | 5                                                          |
| Team Leader   | Poornima K K                                               |
| Team Members  | Hemalatha S, Tharani S, Mohana, Sabarivasan                |
| Maximum Marks | 4 Marks                                                    |

## Functional Requirements

| FR No. | Functional Requirement (Epic) | Sub Requirement (Story / Sub-task)                                               |
| ------ | ----------------------------- | -------------------------------------------------------------------------------- |
| FR-1   | User Input                    | Enter a story idea, choose genre, tone, art style and number of panels           |
| FR-2   | Script Generation             | Gemini text model creates scenes, dialogues, captions and character descriptions |
| FR-3   | Image Generation              | Gemini image model generates one image per panel from the scene description      |
| FR-4   | Comic Layout                  | Arrange panels on a page and add speech bubbles and captions                     |
| FR-5   | Editing                       | Edit dialogue and regenerate a single panel                                      |
| FR-6   | Export                        | Download the comic as PDF or PNG                                                 |

## Non-Functional Requirements

| NFR No. | Non-Functional Requirement | Description                                                  |
| ------- | -------------------------- | ------------------------------------------------------------ |
| NFR-1   | Usability                  | Simple interface that needs no design or drawing skill       |
| NFR-2   | Security                   | API keys kept on the server and never exposed to the browser |
| NFR-3   | Reliability                | Retry a failed image generation and show a clear message     |
| NFR-4   | Performance                | Script within 10 seconds and each panel within 20 seconds    |
| NFR-5   | Availability               | Application available at least 99 percent of the time        |
| NFR-6   | Scalability                | Cloud deployment that supports many users                    |
