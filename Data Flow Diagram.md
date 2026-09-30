# Data Flow Diagram - ComicCraft.ai

| Field | Details |
|---|---|
| Date | 30-09-2026 |
| Team ID | SWTID-2026-6831 |
| Project Name | ComicCraft.ai - Your Smart Budget & Recommendation Assistant |
| Team Size | 5 |
| Team Leader | Poornima K K |
| Team Members | Hemalatha S, Tharani S, Mohana, Sabarivasan |
| Maximum Marks | 4 Marks |

## Data Flow
| Flow | From | Process | To |
|---|---|---|---|
| 1 | User | Enters income and expenses (or uploads CSV) | Web application |
| 2 | Web application | Validates and stores the data | Database |
| 3 | Database | Sends expense history | ML categorization and forecast module |
| 4 | ML module | Returns categories, spending summary and forecast | Backend |
| 5 | Backend | Sends spending summary as context | LLM (GenAI) |
| 6 | LLM | Returns budget plan and personalized recommendations | Backend |
| 7 | Backend | Displays dashboard, budget, tips and alerts | User |

## User Stories
| User Type | Functional Requirement | User Story No. | User Story / Task | Acceptance Criteria | Priority | Release |
|---|---|---|---|---|---|---|
| Customer | FR-1 | USN-1 | As a user, I can register and set my monthly income | Account is created and income is saved | High | Sprint-1 |
| Customer | FR-2 | USN-2 | As a user, I can add expenses and see them categorized | Expense is saved with the correct category | High | Sprint-1 |
| Customer | FR-3 | USN-3 | As a user, I get an AI-generated monthly budget | Budget shows limits per category | High | Sprint-2 |
| Customer | FR-4 | USN-4 | As a user, I get personalized saving recommendations | At least 3 relevant tips are shown | High | Sprint-2 |
| Customer | FR-5 | USN-5 | As a user, I can see charts, forecast and alerts | Dashboard and alerts display correctly | Medium | Sprint-3 |
| Customer | FR-6 | USN-6 | As a user, I can download my monthly report | PDF or CSV downloads successfully | Medium | Sprint-3 |
