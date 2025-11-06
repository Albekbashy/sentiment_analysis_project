# 🧠 Sentiment Analysis with BERT  
### *A collaborative project by Abdullah & Assim (Aivancity)*  

---

## 📌 Project Overview
This project implements a **sentiment analysis pipeline** using **BERT (Bidirectional Encoder Representations from Transformers)**.  
The goal is to classify text into **positive** or **negative** sentiment through a complete end-to-end workflow — including **data extraction, preprocessing, model training, inference, testing, and CI integration**.

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
│   └── unit/
│       ├── test_data_extraction.py
│       ├── test_data_processing.py
│       ├── test_model.py
│       └── test_inference.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```

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
```bash
pytest --cov=.
```

### 🔹 Run Inference
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

| Phase | Task | Lead | Partner |
|-------|------|------|---------|
| 1 | Data Extraction | Abdullah | Review |
| 2 | Data Cleaning | Abdullah | Assist |
| 3 | Tokenization | Assim | Review |
| 4 | Model Training | Assim | Assist |
| 5 | Inference | Assim | Test |
| 6 | Testing & CI | Both | Both |
| 7 | README | Both | Both |

---

## 🧪 Testing and CI
- All modules include unit tests under `tests/unit/`.
- GitHub Actions runs tests automatically on every push.
- 90%+ coverage achieved.

---

## 🧰 Collaboration Workflow

### 🔸 Git & Branches
Feature-based workflow:
- `feature-data-extraction`
- `feature-data-cleaning`
- `feature-tokenization`
- `feature-model-training`
- `feature-inference`
- `feature-testing`
- `feature-ci-integration`
- `feature-documentation-report`

### 🔸 Trello Board
**Lists:**
- To Do
- In Progress
- In Review
- Done

---

## 🌟 Future Improvements
- Fine-tune BERT with larger datasets.
- Add web interface.
- Expand to more sentiment categories.

---

## 🧾 Authors
**Abdullah & Assim**  
Students at Aivancity School for Technology, Business & Society

---