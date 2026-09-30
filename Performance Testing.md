# Performance Testing - ComicCraft.ai

| Field | Details |
|---|---|
| Date | 30-09-2026 |
| Team ID | SWTID-2026-6831 |
| Project Name | ComicCraft.ai - Your Smart Budget & Recommendation Assistant |
| Team Size | 5 |
| Team Leader | Poornima K K |
| Team Members | Hemalatha S, Tharani S, Mohana, Sabarivasan |
| Maximum Marks | 4 Marks |

## Performance Results
| S.No | Parameter | Values |
|---|---|---|
| 1 | Expense categorization accuracy | 92 percent on test data |
| 2 | Add expense response time | 0.6 seconds |
| 3 | Budget generation time | 2.8 seconds |
| 4 | Recommendation generation time | 3.4 seconds |
| 5 | Dashboard load time | 1.4 seconds |
| 6 | Concurrent users tested | 25 users without failure |

## Functional Test Cases
| Test Case ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-01 | Register with valid details | Account created | Account created | Pass |
| TC-02 | Add an expense | Saved with category | Saved with category | Pass |
| TC-03 | Generate budget | Category limits displayed | Category limits displayed | Pass |
| TC-04 | Request recommendations | At least 3 tips shown | 4 tips shown | Pass |
| TC-05 | Spending crosses limit | Overspending alert shown | Alert shown | Pass |
| TC-06 | Download report | PDF downloads | PDF downloaded | Pass |
