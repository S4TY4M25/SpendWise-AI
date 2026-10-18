# 💸 SpendWise AI

**Track expenses using everyday language — powered by an AI model running on your own computer.**

SpendWise AI is a simple expense tracker built with **Python**, **Streamlit**, **Ollama**, and **Gemma 3 (1B)**. Describe your purchases in a sentence, and the app extracts individual expenses, categorizes them, and displays a spending dashboard.

> Built for learning and submitted as a project for the **Hacktoberfest 2026 Open-Source AI Challenge — Week 2: Side Hustle**.

## ✨ Features

- 📝 **Natural-language input** — Add several expenses in a single sentence.
- 🤖 **Local AI extraction** — Extract descriptions, amounts, and categories with Gemma 3.
- 📊 **Dashboard** — View total spending, transaction count, and average expense.
- 📉 **Category breakdown** — Visualize spending with a bar chart.
- 📥 **CSV export** — Download transactions for later use.
- 🔒 **Local inference** — No paid AI API key required.

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Core application logic |
| Streamlit | Web app and dashboard |
| Ollama | Local model inference |
| Gemma 3 (`gemma3:1b`) | Expense extraction and categorization |
| Pydantic | Validating structured model output |
| Pandas | Expense tables and summaries |

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or later
- [Ollama](https://ollama.com/download) installed on your computer
- Enough RAM and free space to run `gemma3:1b`

### 1. Clone the repository

```bash
git clone https://github.com/S4TY4M25/SpendWise-AI.git
cd SpendWise-AI
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the AI model

Make sure Ollama is installed and running, then enter:

```bash
ollama pull gemma3:1b
```

To confirm the download:

```bash
ollama list
```

### 5. Launch SpendWise AI

```bash
python -m streamlit run app.py
```

Open **http://localhost:8501** if Streamlit does not automatically open the browser.

## 💡 Example Usage

**Input:**

```text
Spent Rs 150 on coffee, Rs 300 on Uber, and Rs 200 on lunch.
```

**Example extracted expenses:**

| Item | Amount | Category |
| --- | ---: | --- |
| Coffee | ₹150 | Food |
| Uber | ₹300 | Transport |
| Lunch | ₹200 | Food |
| **Total** | **₹650** | |

The app then displays the transactions, spending metrics, and category chart. Results may vary because extraction is AI-generated.

## 📸 Screenshots

Add a screenshot of your working dashboard to `assets/dashboard.png`, then replace this sentence with:

`![SpendWise AI Dashboard](assets/dashboard.png)`

## 🔐 Why Open-Weight, Local AI?

The Gemma model is run locally with Ollama. Expense text is processed by your local model service instead of being sent to a paid cloud model API. Once installed, the model can run without internet access. This offers more control over entered data and avoids per-request model charges.

## ⚠️ Limitations

- Expenses are stored in **Streamlit session state**, not a database; download the CSV before closing or resetting the session.
- Amounts are assumed to be in **Indian rupees (INR)**.
- AI extraction can sometimes make mistakes, so review transactions before relying on them.
- Receipt-image upload, user accounts, and persistent history are not included.
- Running the project requires a local Ollama installation and downloaded model.

## 🔮 Future Improvements

- Persistent storage with SQLite
- Edit or delete individual transactions
- Receipt scanning using OCR
- Monthly budgets and spending alerts
- Improved currency handling

## 🎃 Hacktoberfest 2026

Created as a small practical learning project for the **Hacktoberfest Open-Source AI Challenge: Week 2 — Side Hustle**. The goal was to learn how to connect a local language model to a real application, validate structured output, and build an end-to-end Python app.

## 👨‍💻 Author

**[S4TY4M25](https://github.com/S4TY4M25)**
