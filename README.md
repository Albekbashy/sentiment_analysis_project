# 🧠 Sentiment Analysis with BERT
### *A collaborative project by Abdullah & Assim (Aivancity)*

---

## 📌 Project Overview
This project implements a **sentiment analysis pipeline** using **BERT (Bidirectional Encoder Representations from Transformers)**. The goal is to classify text into **positive** or **negative** sentiment through a complete end-to-end workflow — including **data extraction, preprocessing, model training, inference, testing, and CI integration**.

This project was developed collaboratively by **Abdullah (Student 1)** and **Assim (Student 2)** as part of our coursework on AI development and teamwork using Git and Trello.

---

## ⚙️ Tech Stack
- **Programming Language:** Python
- **Frameworks/Libraries:**
  - Transformers (Hugging Face)
  - PyTorch
  - pandas, scikit-learn
  - pytest, pytest-cov
- **Collaboration Tools:** GitHub, Trello, GitHub Actions

---

## 🧩 Project Structure

```
sentiment_analysis_project/
│
├── data_extraction.py          # Load and validate dataset
├── data_processing.py          # Clean and tokenize text
├── model.py                    # Load pretrained BERT model
├── inference.py                # Predict sentiment using the model
│
├── tests/
│   └── unit/                   # Unit tests for each module
│       ├── test_data_extraction.py
│       ├── test_data_processing.py
│       ├── test_model.py
│       └── test_inference.py
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```
---

## 🧩 Project Components (Brief Overview)

- **`data_extraction.py`** → Loads and validates the dataset before processing.
- **`data_processing.py`** → Cleans and tokenizes text for BERT input.
- **`model.py`** → Defines and fine-tunes the BERT model for sentiment classification.
- **`inference.py`** → Runs predictions using the trained model.
- **`tests/`** → Contains PyTest scripts to ensure module reliability.
- **`README.md`** → Describes the project, setup, and structure.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your_team_repo>.git
cd sentiment_analysis_project
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 Usage

### 🔹 Run Tests
To verify that all modules work correctly:
```bash
pytest --cov=.
```

### 🔹 Run Inference
To test a sentiment prediction:
```python
from inference import predict_sentiment

text = "I love studying AI!"
print(predict_sentiment(text))
```

**Expected output:**
```
positive
```

---

## 👨‍💻 Team Responsibilities

| Phase | Main Task | Lead | Partner's Role |
|-------|-----------|------|----------------|
| 1 | Data Extraction | Abdullah | Reviewed dataset structure |
| 2 | Data Cleaning | Abdullah | Assisted with validation |
| 3 | Tokenization | Assim | Reviewed tokenizer logic |
| 4 | Model Training | Assim | Created test scripts and metrics |
| 5 | Inference | Assim | Abdullah tested and documented |
| 6 | Testing & CI | Both | Reviewed tests and CI integration |
| 7 | Report & README | Both | Completed documentation together |

---

## 🧪 Testing
- Each module includes unit tests in `tests/unit/`.
- Achieved over **90% test coverage**.

---

## 🧰 Collaboration Workflow

### 🔸 Git & Branches
We followed a feature-branch workflow with 8 clean branches:
```
feature-data-extraction
feature-data-cleaning
feature-tokenization
feature-model-training
feature-inference
feature-testing
feature-documentation-report
```

Each branch included clear commits, PRs, and peer reviews before merging.

### 🔸 Trello Board
A shared Trello board managed our progress with lists:
- **To Do**
- **In Progress**
- **In Review**
- **Done**

Each card included:
- Task description
- Assigned member
- Checklist
- Link to related PR

---

## 📊 Evaluation Criteria Alignment

| Criterion | Description | Achieved |
|-----------|-------------|----------|
| C01 – Git Workflow | 8 branches, clear commits, reviewed PRs | ✅ |
| C02 – Unit Testing | Tests for all modules, >90% coverage | ✅ |
| C03 – Trello Board | Full workflow tracked & documented | ✅ |
| C04 – Collaboration | Both students reviewed PRs & coordinated | ✅ |

---

## 🌟 Future Improvements
- Fine-tune the BERT model with real sentiment datasets (IMDb, SST-2).
- Add a web interface for interactive sentiment analysis.
- Extend sentiment categories (e.g., neutral, mixed).

---

## 🧾 Authors
**Abdullah & Assim**  
Students at Aivancity School for Technology, Business & Society

---
