    💸 SpendWise AI
A lightweight, privacy-friendly expense tracker powered by local AI.
SpendWise AI turns everyday descriptions of spending into organized transactions. Type something like “Spent Rs 150 on coffee, Rs 300 on Uber, and Rs 200 on lunch” and the app uses Gemma 3 (1B) through Ollama to extract expenses, assign categories, and update a Streamlit dashboard.
Built as a learning project for the Hacktoberfest 2026 Open-Source AI Challenge — Week 2: Side Hustle.
✨ Features
- Natural-language input: Add multiple expenses in one sentence.
- Local AI extraction: Identify item names, amounts, and spending categories with Gemma 3 via Ollama.
- Structured output: Validate the model's JSON output with Pydantic.
- Spending overview: Track total spending, transaction count, and average transaction value.
- Category chart: See a bar chart of spending grouped by category.
- CSV export: Download your current transactions.
- Clear data: Reset the current session's expenses.
🛠️ Tech stack
Technology	Used for
Python	Application logic
Streamlit	Web interface and dashboard
Ollama	Running the language model locally
Gemma 3 (gemma3:1b)	Extracting expenses from natural language
Pydantic	Validating structured AI output
Pandas	Organizing transactions and calculating summaries


🚀 Getting started
Prerequisites
- Python with support for the packages in requirements.txt
- Ollama installed and running
- Enough free disk space and memory to run the gemma3:1b model locally
1. Clone the repository
git clone https://github.com/S4TY4M25/SpendWise-AI.git
cd SpendWise-AI
This URL assumes the GitHub repository is named SpendWise-AI. If you use another repository name, update the URL above.

2. Create a virtual environment (recommended)
Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install Python dependencies
python -m pip install -r requirements.txt
4. Download the model
ollama pull gemma3:1b
Make sure the Ollama application/server is running. You can verify the model is installed with ollama list.
5. Launch the app
python -m streamlit run app.py
Open http://localhost:8501 in your browser if it does not open automatically.
🧪 Example
Input
Spent Rs 150 on coffee, Rs 300 on Uber and Rs 200 on lunch.
Illustrative extracted transactions (model output can vary):
Item	Amount	Category
Coffee	₹150	Food
Uber	₹300	Transport
Lunch	₹200	Food


Total: ₹650
The dashboard then displays these entries, summary metrics, and a category spending chart.
📸 Screenshot
After taking a screenshot of the running app, save it as assets/dashboard.png and uncomment the line below:
<!-- ![SpendWise AI dashboard](assets/dashboard.png) -->

🔐 Why local, open-weight AI?
SpendWise AI uses an open-weight language model running through Ollama on your computer. The application does not need a paid model API, and its expense descriptions are sent to your local Ollama service rather than a hosted AI provider. Once the model and dependencies are installed, model inference can work without an internet connection.
This makes the project an accessible way to experiment with practical AI integration while retaining local control over entered financial details.
⚠️ Current limitations
- Transactions are stored only in Streamlit session state and can disappear when the session resets; export the CSV to keep a copy.
- Amounts are treated as INR; the app is not a currency converter.
- The model can occasionally miss, duplicate, or miscategorize an expense. Review results before relying on them.
- No receipt-photo scanning, user accounts, or persistent database are included.
- Anyone running the app must install Ollama and obtain the local model separately.
🔮 Possible improvements
- Editable transactions and duplicate prevention
- SQLite storage for persistent expense history
- Monthly spending trends and budgeting
- Receipt scanning with OCR
- More robust handling of currencies and complex descriptions
🎃 Hacktoberfest 2026
Created for the Hacktoberfest Open-Source AI Challenge: Week 2 — Side Hustle as a small learning project. It explores how local open-weight AI can simplify a repetitive personal-finance task.
👨‍💻 Author
S4TY4M25