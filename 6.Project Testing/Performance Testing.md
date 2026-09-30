# Performance Testing - ComicCraft AI

| Field         | Details                                                    |
| ------------- | ---------------------------------------------------------- |
| Date          | 30-09-2026                                                 |
| Team ID       | SWTID-2026-6831                                            |
| Project Name  | ComicCraft AI - AI Comic Story Creator using Gemini Models |
| Team Size     | 5                                                          |
| Team Leader   | Poornima K K                                               |
| Team Members  | Hemalatha S, Tharani S, Mohana, Sabarivasan                |
| Maximum Marks | 4 Marks                                                    |

## Performance Results

| S.No | Parameter                          | Values      |
| ---- | ---------------------------------- | ----------- |
| 1    | Script generation time             | 6 seconds   |
| 2    | Image generation time per panel    | 14 seconds  |
| 3    | Full comic (6 panels) time         | 95 seconds  |
| 4    | Layout and speech bubble time      | 2 seconds   |
| 5    | Export time (PDF)                  | 3 seconds   |
| 6    | Prompt match quality (team rating) | 8 out of 10 |

## Functional Test Cases

| Test Case ID | Scenario                             | Expected Result          | Actual Result            | Status |
| ------------ | ------------------------------------ | ------------------------ | ------------------------ | ------ |
| TC-01        | Enter a valid story idea             | Script is generated      | Script generated         | Pass   |
| TC-02        | Generate panels for a 6-scene script | 6 images created         | 6 images created         | Pass   |
| TC-03        | Add speech bubbles                   | Text shown on each panel | Text shown on each panel | Pass   |
| TC-04        | Edit dialogue and save               | Updated text displayed   | Updated text displayed   | Pass   |
| TC-05        | Regenerate one panel                 | Only that panel changes  | Only that panel changed  | Pass   |
| TC-06        | Download as PDF                      | PDF file downloads       | PDF downloaded           | Pass   |
