import streamlit as st
import pandas as pd
from ollama import chat
from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

# ----------------------------------
# 1. CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="SpendWise AI",
    page_icon="💸",
    layout="wide"
)

MODEL = "gemma3:1b"

# ----------------------------------
# 2. DEFINE AI OUTPUT STRUCTURE
# ----------------------------------

Category = Literal[
    "Food", "Transport", "Shopping",
    "Education", "Entertainment",
    "Bills", "Health", "Other"
]

class Expense(BaseModel):
    item: str
    amount: float = Field(gt=0)
    category: Category

class ExpenseList(BaseModel):
    expenses: list[Expense]

# ----------------------------------
# 3. SESSION STATE
# ----------------------------------

if "expenses" not in st.session_state:
    st.session_state.expenses = []

# ----------------------------------
# 4. AI EXTRACTION FUNCTION
# ----------------------------------

def extract_expenses(user_text):
    prompt = f"""
    You are an expense extraction assistant.

    Extract all explicitly mentioned expenses
    from the user's text.

    For every expense, identify:
    - item: short description
    - amount: numerical amount in INR
    - category: suitable spending category

    Rules:
    - Do not invent expenses or amounts.
    - Do not count totals as extra expenses.
    - Ignore income and refunds.
    - If no expense is found, return an empty list.
    - Assume INR unless otherwise specified.
    - Return only structured data.

    User text:
    {user_text}
    """

    response = chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        format=ExpenseList.model_json_schema(),
        options={"temperature": 0}
    )

    result = ExpenseList.model_validate_json(
        response.message.content
    )

    return result.expenses

# ----------------------------------
# 5. APPLICATION HEADER
# ----------------------------------

st.title("💸 SpendWise AI")
st.caption(
    "Your private AI-powered expense tracker | "
    "Built with Streamlit + Ollama + Gemma"
)

st.divider()

# ----------------------------------
# 6. USER INPUT
# ----------------------------------

st.subheader("📝 Add Your Expenses")

user_input = st.text_area(
    "Describe your expenses:",
    placeholder=(
        "Example: Spent Rs 250 on pizza, "
        "Rs 120 on coffee and Rs 80 on a notebook"
    ),
    height=120
)

if st.button("✨ Extract Expenses", type="primary"):

    if not user_input.strip():
        st.warning("Please enter some expense details.")

    else:
        with st.spinner("AI is analyzing your expenses..."):

            try:
                extracted = extract_expenses(user_input)

                if not extracted:
                    st.info("No expenses detected.")

                else:
                    for expense in extracted:
                        st.session_state.expenses.append({
                            "Date": str(date.today()),
                            "Item": expense.item,
                            "Amount": expense.amount,
                            "Category": expense.category
                        })

                    st.success(
                        f"Added {len(extracted)} expenses!"
                    )

            except Exception as e:
                st.error(
                    "Could not process expenses. "
                    "Make sure Ollama is running."
                )
                st.error(str(e))

# ----------------------------------
# 7. DASHBOARD
# ----------------------------------

st.divider()
st.subheader("📊 Expense Dashboard")

if st.session_state.expenses:

    df = pd.DataFrame(st.session_state.expenses)

    total = df["Amount"].sum()
    count = len(df)
    average = df["Amount"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Total Spending", f"₹{total:,.2f}")

    with col2:
        st.metric("🧾 Transactions", count)

    with col3:
        st.metric("📈 Average Expense", f"₹{average:,.2f}")

    st.divider()

    # Expense table
    st.subheader("📋 Your Transactions")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Category breakdown
    st.subheader("📉 Spending by Category")

    category_data = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_data)

    # CSV download
    st.divider()

    csv = df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="📥 Download Expenses as CSV",
        data=csv,
        file_name="spendwise_expenses.csv",
        mime="text/csv"
    )

    # Clear data
    if st.button("🗑️ Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()

else:
    st.info(
        "No expenses yet. Add some expenses above "
        "to see your dashboard!"
    )

# ----------------------------------
# 8. FOOTER
# ----------------------------------

st.divider()

st.caption(
    "SpendWise AI | Built with open-source AI "
    "for Hacktoberfest 2026"
)