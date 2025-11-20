import streamlit as st
import altair as alt

import datetime as dt
import pandas as p 
import matplotlib.pyplot as plt

import calendar

# from db import get_connection

# ---------------------------
# Database Base Functions
# ---------------------------
import mysql.connector as mc

st.session_state.reload_table = True 

# cur = con.cursor()
# con.commit = True


# 

# import os
# from supabase import create_client, Client

# url: str = os.environ.get("https://gdjhxhpwtvfyomkrqarl.supabase.co")
# key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdkamh4aHB3dHZmeW9ta3JxYXJsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMzMDY0ODIsImV4cCI6MjA3ODg4MjQ4Mn0.brNZVw8Fcc21yx2X_MZzsCMXHXNQqUtV3oQjGAd5XKA")
# supabase: Client = create_client(url, key)


def get_connection():
    """
    Returns a MySQL database connection object.
    Update the credentials before running.
    """
    return mc.connect(
        host="localhost",
        user="adrian",
        password="sittingClarity",    
        database="expenses")


def get_cursor():
    """
    Creates a database connection and returns (connection, cursor).
    Helps avoid global connections and keeps code stable.
    """
    con = get_connection()
    cur = con.cursor()
    return con, cur


def insert_expense(name, date, amount):
    """
    Inserts a new expense into the database.
    """
    conn, cur = get_cursor()
    query = """INSERT INTO expenses(expense_name, expense_date, expense_amount)
               VALUES (%s, %s, %s)"""
    cur.execute(query, (name, date, amount))
    conn.commit()
    conn.close()


def fetch_expenses():
    """
    Returns a list of all stored expenses.
    """
    # conn, cur = get_cursor()
    # cur.execute("SELECT * FROM expenses")
    # rows = cur.fetchall()
    # conn.close()

    con , cur = get_cursor()
    cur.execute("SELECT * FROM expenses;")
    data = []
    expense_Data = cur.fetchall()
    global col_names
    col_names = [col[0] for col in cur.description]

    df = p.DataFrame(data=expense_Data,columns=col_names)
    return df 
    # st.dataframe(df)
    # return rows


def delete_expense(expense_id):
    """
    Deletes a specific expense given its ID.
    """
    conn, cur = get_cursor()
    cur.execute("DELETE FROM expenses WHERE expense_id = %s", (expense_id,))

    # st.experimental_rerun() # refresh table else changes are not visible
    conn.commit()
    conn.close()


def update_expense(expense_id, name, date, amount):
    """
    Updates an existing expense.
    """
    conn, cur = get_cursor()
    query = """UPDATE expenses
               SET expense_name=%s, expense_date=%s, expense_amount=%s
               WHERE id=%s"""
    cur.execute(query, (name, date, amount, expense_id))
    conn.commit()
    conn.close()


# ---------------------------
# UI SECTIONS
# ---------------------------

def ui_home_archive():
    """
    Displays the home section with app summary.
    """
    st.title("Expense Manager")
    st.write("Welcome! Use the sidebar to navigate through sections.")
    st.image("https://www.shutterstock.com/image-vector/financial-planning-app-earnings-expenses-control-2210089361", width=400)

# import streamlit as st

def ui_home():
    IMAGE_WIDTH = 400
    st.title("Why You Need an Expense Tracker")

    # --- HERO SECTION ---
    st.markdown("""
    ### Take control of your money with simple daily tracking.
    A clear view of your expenses helps you build better financial habits.
    """)

    st.image(
        "https://images.unsplash.com/photo-1553729459-efe14ef6055d",
        caption="A clean financial dashboard showing spending patterns.",width='stretch'
    )

    st.markdown("---")


    # --- SECTION 1 ---
    st.header("Why Tracking Expenses Matters")
    st.write("""
    • Helps you control daily spending  
    • Builds long-term saving habits  
    • Prevents financial surprises  
    """)

    st.image(
        # "https://images.unsplash.com/photo-1605902711622-cfb43c44367c"
        "spending.jpeg",width='stretch'        
    )

    st.markdown("---")

    # --- SECTION 2 ---
    st.header("Common Problems Without Tracking")
    st.write("""
    • Forgetting small daily purchases  
    • Money leaking through unplanned spending  
    • Difficulties in planning monthly budgets  
    """)

    st.image(
        "overhead.png",
        caption="Forgetting small daily purchases can lead to big financial problems.",
        width='stretch'
    )


    st.markdown("---")

    # --- SECTION 3 ---
    st.header("Benefits of Using a Digital Expense Tracker")
    st.write("""
    • Automatically saves data  
    • Easy monthly comparisons  
    • Clear charts and categories  
    """)

# **************************HERE 
    # st.image("charts.webp" , width='stretch')
    st.image(
        "charts.webp",
        caption="Charts make it easier to identify spending patterns.",
        width='stretch'
    )

    st.markdown("---")

    # --- SECTION 4 ---
    st.header("What This App Helps You Do")
    st.write("""
    • Add, edit, delete expenses  
    • Analyze your spending  
    • Track monthly totals  
    • Chat with AI for financial insights  
    """)

    st.image(
        "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4",
        caption="Managing your finances becomes easier when everything is in one place.",
        width='stretch'
    )

    st.markdown("---")

    # --- FOOTER ---
    st.subheader("Start Tracking Today")
    st.write("Small steps today build a stronger financial future.")



def ui_add_expense():
    """
    Form for adding a new expense.
    """
    st.header("Add New Expense")

    with st.form("add_expense_form"):
        name = st.text_input("Expense Name")
        amount = st.number_input("Amount", min_value=0.0)
        date = st.date_input(
            "Date",
            min_value=dt.date(1990, 1, 1),
            max_value=dt.date.today(),
            value=dt.date.today()
        )

        submitted = st.form_submit_button("Add Expense")

        if submitted:
            insert_expense(name, date, amount)
            st.success("Expense Added")
            # st.rerun()



def ui_view_expense():
    """
    Displays all stored expenses and supports delete/update operations.
    """
    st.header("All Expenses")

    data = fetch_expenses()

    st.dataframe(data)
    st.session_state.reload_table = True 

    delete_id = st.number_input("Enter Expense ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        delete_expense(delete_id)
        st.success("Expense Deleted")
        # st.session_state.reload_table = True

        # st.session_state.reload_table = True 
        st.rerun()

def ui_analytics():
    """
    Shows simple analytics like total spent and largest expense.
    """
    st.header("Analytics")

    # gives panda data table 
    data = fetch_expenses()
    st.dataframe(data)

    data_df = p.DataFrame(data)

# MONTH WISE EXPENSES 
    st.header("Month Expenditure")
    con , cur = get_cursor()
    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    # st.selectbox("Select month",month_list)
    selected_month = month_list.index(st.selectbox("Select month",month_list))
    cur.execute("SELECT expense_amount , expense_date FROM expenses WHERE MONTH(expense_date) = %s;",(selected_month+1,))

    data = cur.fetchall() 
    
    df = p.DataFrame(data, columns=["expense_amount", "expense_date"])
    df["expense_date"] = p.to_datetime(df["expense_date"])
    df["expense_amount"] = p.to_numeric(df["expense_amount"])

    # st.dataframe(df)
    st.line_chart(df, x="expense_date", y="expense_amount")

    # YEARLY TREND as months sum 

    st.header("Monthly Expenditure")
    yearQuery = '''
    SELECT 
    MONTH(expense_date) AS month_num,
    MONTHNAME(expense_date) AS Month,
    SUM(expense_amount) AS TotalSpend
    FROM expenses
    GROUP BY MONTH(expense_date) , 
    MONTHNAME(expense_date)
    ;'''
    # ORDER BY MIN(expense_date);'''
    cur.execute(yearQuery)

    yearData = cur.fetchall()

    dfYearData = p.DataFrame(yearData,columns=["month_num","Month","Total Spend"])
    dfYearData["Total Spend"] = p.to_numeric(dfYearData["Total Spend"])
    dfYearData = dfYearData.sort_values("month_num")
#sol2 
    months = [calendar.month_name[i] for i in range(1, 13)]

# make month_name an ordered categorical and sort
    dfYearData['Month'] = p.Categorical(dfYearData['Month'], categories=months, ordered=True)

    dfYearData = dfYearData.sort_values('Month')

# now this will respect the calendar order
    st.bar_chart(dfYearData.set_index('Month')['Total Spend'])


import lmstudio as lms
def local_ai_helper():
    st.header("AI Helper")
    if "messages" not in st.session_state:
        st.session_state.messages = []  # list of dicts: {"role": "user"|"assistant", "content": str}
    model = lms.llm("qwen3-0.6b")
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    prompt = st.chat_input("Type your message")
    if prompt:
        st.session_state.messages.append({"role":"user","content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        # st.spinner("Thinking...")
        result = model.respond(prompt)
        with st.chat_message("ai"):
            st.session_state.messages.append({"role": "assistant", "content": result})
            # st.session_state.messages.append({"role":"AI","content": prompt})
            st.markdown(result)



import requests

def ui_ai_helper():
    st.header("AI Helper")

    model_id = "qwen3-0.6b"
    temperature = 0.7
    max_tokens = -1
    stream = False

    if "messages" not in st.session_state:
        st.session_state.messages = []  # list of dicts: {"role": "user"|"assistant", "content": str}
    with st.sidebar:
        st.subheader("Settings")
        model_id = st.selectbox("Model", ["qwen3-0.6b"], index=0)
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=temperature, step=0.1)
        max_tokens = st.slider("Max tokens", min_value=0, max_value=1000, value=max_tokens, step=50 )
        stream = st.checkbox("Stream", value=stream)
        if st.button("Clear chat"):
            st.session_state.messages = []
            st.rerun()

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    prompt = st.chat_input("Type your message")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                url = "http://localhost:1234/v1/chat/completions"
                headers = {"Content-Type": "application/json"}
                data = {
                    "model": model_id,
                    "messages": st.session_state.messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "stream": stream
                }
                resp = requests.post(url, headers=headers, json=data)
                if resp.status_code == 200:
                    reply = resp.json()["choices"][0]["message"]["content"]
                else:
                    raise Exception(f"API error: {resp.text}")
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"API error: {e}")


def ui_ai_helper_original():
    from google import genai
    st.header("AI Helper")
    # st.write("Ask something about your expenses.")

    GOOGLE_API_KEY = "AIzaSyArp4nTMkGs0Kyvy7kSD_KkhKEmX1CzOUQ"
    client = genai.Client(api_key=GOOGLE_API_KEY)
    chat = client.chats.create(model='gemini-2.0-flash', history=[])
    # Page config and title
    st.set_page_config(page_title="Basic Chat • Gemini", page_icon="💬")
    st.title("Basic Chat (Gemini) 💬")

    # Resolve API key: prefer st.secrets, otherwise env var
    # api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    
    # Initialize client (explicit key)
    client = genai.Client(api_key=GOOGLE_API_KEY)

    # Model to use — 2.5 Flash is fast and cost‑effective for chat
    model_id = "gemini-2.5-flash"

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []  # list of dicts: {"role": "user"|"assistant", "content": str}

    # print('HELLLo hehe****************')
    # Sidebar: simple settings
    with st.sidebar:
        st.subheader("Settings")
        model_id = st.selectbox("Model", ["gemini-2.5-flash", "gemini-1.5-pro"], index=0)
        if st.button("Clear chat"):
            st.session_state.messages = []
            st.rerun()

    # Render existing messages
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # Chat input at bottom
    prompt = st.chat_input("Type your message")
    if prompt:
        # Echo user
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call Gemini API
        with st.chat_message("assistant"):
            try:
                # Convert history to Gemini contents: minimal mapping
                contents = []
                for msg in st.session_state.messages:
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append({"role": role, "parts": [{"text": msg["content"]}]})

                # Append latest user prompt is already included above
                resp = client.models.generate_content(
                    model=model_id,
                    contents=contents,
                )
                reply = getattr(resp, "text", "") or "No response."
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"API error: {e}")

    # client = genai.Client(GOOGLE_API_KEYy=GOOGLE_API_KEY)
    # chat = client.chats.create(model='gemini-2.0-flash', history=[])
    # query = st.text_area("Your Question")
    # response_placeholder = st.empty()
    # if st.button("Ask"):
    #     response_placeholder.write("AI Response coming soon...")
    #     # st.write("AI Response coming soon...")
    #     response = chat.send_message(query)
    #     response_placeholder.write(response.text)


def main():
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Go To", 
        ["Home", "Add Expense", "View Expenses", "Analytics", "AI Helper"]
    )

    if menu == "Home":
        ui_home()
    elif menu == "Add Expense":
        ui_add_expense()
    elif menu == "View Expenses":
        ui_view_expense()
    elif menu == "Analytics":
        ui_analytics()
    elif menu == "AI Helper":
        # ui_ai_helper()
        local_ai_helper()


if __name__ == "__main__":
    main()
