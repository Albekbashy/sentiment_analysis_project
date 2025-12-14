
# 🧠 Sentiment Analysis MLOps Pipeline

### *A collaborative project by Abdullah & Assim (Aivancity)*

-----

## 📌 Project Overview

This project implements a complete **MLOps sentiment analysis pipeline** using **BERT**. It evolves a basic machine learning workflow into a production-ready system featuring **Docker containerization, PostgreSQL database logging, and automated CI/CD pipelines via GitHub Actions**.

The goal is to classify text into **positive** or **negative** sentiment through an end-to-end workflow — including data extraction, preprocessing, model training, inference, testing, containerization, and automated deployment.

-----

## ⚙️ Tech Stack

  - **Programming Language:** Python 3.10
  - **Machine Learning:** Transformers (Hugging Face), PyTorch (CPU Optimized), scikit-learn, pandas
  - **Containerization:** Docker, Docker Compose
  - **Database:** PostgreSQL (for prediction logging)
  - **CI/CD:** GitHub Actions (Testing, Evaluation, Build & Push)
  - **Collaboration:** GitHub, Trello

-----

## 🧩 Project Structure

```text
sentiment_analysis_project/
│
├── .github/workflows/          # CI/CD Automation
│   ├── test.yml                # Unit tests & linting
│   ├── evaluate.yml            # Model evaluation trigger
│   └── build.yml               # Docker build & push to Docker Hub
│                 
│── data_extraction.py      # Load and validate dataset
│── data_processing.py      # Clean and tokenize text
│── model.py                # Load pretrained BERT model
│── inference.py            # Predict sentiment logic
│── cli.py                  # Command Line Interface (Entry point)
│── logger.py               # Database logging module
│── train.py                # Train the model
|── evaluate.py             # Model evaluation
|
├── tests/
│   └── unit/                   # Unit tests for all modules
│
├── init-db.sql             # SQL script to initialize database schema
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

-----

## 🧩 Project Components (Detailed Overview)

### 🔹 Core ML Pipeline

  - **`data_extraction.py`**: Loads the dataset, validates structure, and handles initial data ingestion.
  - **`data_processing.py`**: Preprocesses raw text (cleaning, tokenization) to prepare inputs for the BERT model.
  - **`model.py`**: Defines the architecture, loads the pre-trained BERT model, and handles fine-tuning.
  - **`inference.py`**: Contains the logic to accept a processed string and return a sentiment prediction using the trained model.

### 🔹 MLOps & Application Logic (Part 2)

  - **`cli.py`**: The main entry point for the application. It provides a Command Line Interface that accepts text arguments, runs inference, and triggers the logger.
  - **`logger.py`**: A modular component that connects to the PostgreSQL service. It securely inserts prediction results (Text, Sentiment, Timestamp) into the database.
  - **`Dockerfile`**: Defines the portable environment using a lightweight Python 3.10 image. It optimizes PyTorch for CPU usage to reduce image size and build time.
  - **`docker-compose.yml`**: Orchestrates the application. It spins up two services (`sentiment_app` and `db`), sets up a private network, and creates persistent volumes for the model cache and database storage.
  - **`init-db.sql`**: A setup script that runs automatically when the database starts. It creates the `sentiment_logs` table and sets up performance indexes.

### 🔹 Automation (CI/CD)

  - **`test.yml`**: Triggers on push/pull requests. Installs dependencies, runs code quality checks (flake8, black), and executes unit tests.
  - **`evaluate.yml`**: Runs after tests pass to evaluate model performance (simulated).
  - **`build.yml`**: Runs after evaluation. Builds the Docker image and securely pushes it to Docker Hub using repository secrets.

-----

## 🚀 Installation & Setup

### Option A: Running with Docker (Recommended)

This method ensures the environment is exactly as intended without installing local dependencies.

**1. Build and Run Services**

```bash
docker-compose up --build
```

**2. Make a Prediction (via CLI)**

```bash
docker exec sentiment_app python cli.py --text "This MLOps pipeline is amazing!"
```

**3. Check Database Logs**

```bash
docker exec -it sentiment_logs_db psql -U sentiment_user -d sentiment_logs -c "SELECT * FROM sentiment_logs;"
```

### Option B: Local Python Setup

**1. Clone the repository**

```bash
git clone https://github.com/Albekbashy/sentiment_analysis_project.git
cd sentiment_analysis_project
```

**2. Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

-----

## 🧠 Usage

### 🔹 Run Tests

To verify that all modules work correctly:

```bash
pytest --cov=.
```

### 🔹 Run Inference (Local)

```python
from inference import predict_sentiment
text = "I love studying AI!"
print(predict_sentiment(text))
```

**Expected output:** `positive`

-----

## 👨‍💻 Team Responsibilities

| Phase | Main Task | Lead | Partner's Role |
|-------|-----------|------|----------------|
| **Part 1** | Data & Model | Abdullah | Data Cleaning & extraction |
| | Tokenization & Inference | Assim | Tokenizer & Training logic |
| **Part 2** | Containerization | Abdullah | Dockerfile & Volumes |
| | Database Integration | Assim | Logging logic & SQL init |
| | CI/CD Pipelines | Both | Workflow configuration & GitHub Secrets |
| | Documentation | Both | Final Report & README |

-----

## 🧰 Collaboration Workflow

### 🔸 Git & Branches

We followed a feature-branch workflow. New branches created for Part 2 included:

  - `feature-docker-setup`
  - `feature-database-logging`
  - `feature-cicd-pipelines`

### 🔸 Trello Board

A shared Trello board managed our progress with lists (To Do, In Progress, In Review, Done). Each card was linked to specific Pull Requests.

-----

## 📊 Evaluation Criteria Alignment

| Criterion | Description | Achieved |
|-----------|-------------|----------|
| **C01 – Git Workflow** | Clean branches, clear commits, reviewed PRs | ✅ |
| **C02 – Unit Testing** | Tests for all modules, \>90% coverage | ✅ |
| **C03 – Containerization** | Working Dockerfile & Compose with persistence | ✅ |
| **C04 – CI/CD** | Automated Testing, Eval, and Docker Push | ✅ |

-----

## 🧾 Authors

**Abdullah & Assim**
Students at Aivancity School for Technology, Business & Society
