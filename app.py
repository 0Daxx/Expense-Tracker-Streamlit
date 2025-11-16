import streamlit as st
import datetime as dt
import pandas as p 
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

    data = fetch_expenses()
    

    st.dataframe(data)

    # st.line_chart(data=data, x="expense_date", y="expense_amount")


    # this month expnse 

    # st.bar_chart(data=data, x="expense_date", y="expense_amount")

    # if data:
    #     total = sum([row[3] for row in data])
    #     highest = max([row[3] for row in data])

    #     st.metric("Total Spent", total)
    #     st.metric("Highest Expense", highest)
    # else:
    #     st.write("No data available")


def ui_ai_helper():
    st.header("AI Helper")
    # st.write("Ask something about your expenses.")

    GOOGLE_API_KEY = "AIzaSyArp4nTMkGs0Kyvy7kSD_KkhKEmX1CzOUQ"
    from google import genai
    client = genai.Client(api_key=GOOGLE_API_KEY)


    chat = client.chats.create(model='gemini-2.0-flash', history=[])

    query = st.text_area("Your Question")

    response_placeholder = st.empty()
    if st.button("Ask"):
        response_placeholder.write("AI Response coming soon...")
        # st.write("AI Response coming soon...")
        response = chat.send_message(query)
        response_placeholder.write(response.text)



# ---------------------------
# MAIN APP
# ---------------------------

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
        ui_ai_helper()


if __name__ == "__main__":
    main()
