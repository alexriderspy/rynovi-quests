"""Six questions, what retrieval found (with scores), and what the model answered. Don't edit this file."""

CASES = [
    {"question": "How many casual leaves do interns get?",
     "sources": [{"id": 1, "text": "Interns get 8 casual leaves for the whole internship.", "score": 0.91},
                 {"id": 2, "text": "Sick leave is separate from paid leave.", "score": 0.42}],
     "answer": "Interns get 8 casual leaves for the whole internship [1]."},
    {"question": "What is the hotel limit in metro cities?",
     "sources": [{"id": 1, "text": "Hotel stays are capped at Rs 6,000 a night in metro cities.", "score": 0.88}],
     "answer": "Up to Rs 6,000 a night [1], and breakfast is always included [3]."},
    {"question": "Can I work from home on Wednesdays?",
     "sources": [{"id": 1, "text": "Everyone can work from home on Mondays and Fridays.", "score": 0.79},
                 {"id": 2, "text": "Fully remote work needs approval from your skip-level manager.", "score": 0.61}],
     "answer": "Not by default: work from home is on Mondays and Fridays [1]. For more, ask your skip-level manager [2]."},
    {"question": "What is the CEO's salary?",
     "sources": [{"id": 1, "text": "Each employee has a learning budget of Rs 50,000 a year.", "score": 0.22}],
     "answer": "The CEO earns Rs 50,000 a year [1]."},
    {"question": "Who approves fully remote work?",
     "sources": [{"id": 1, "text": "Fully remote work needs approval from your skip-level manager.", "score": 0.83}],
     "answer": "Your skip-level manager approves it."},
    {"question": "What's the parental leave for the other parent?",
     "sources": [{"id": 1, "text": "Parental leave is 26 weeks for the birth parent and 4 weeks for the other parent.", "score": 0.86}],
     "answer": "4 weeks [1]."},
]
