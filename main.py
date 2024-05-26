import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import re
from dotenv import load_dotenv
import sqlite3
import openai
from htmlTemplates import css, user_template, bot_template

# Set your OpenAI API key
openai.api_key = "sk-proj-wlgPkseFJuFaLxnCaYIPT3BlbkFJIjEGHK3OcpWu7pkaHGBs"

def create_users_db():
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_user_to_db(email, password):
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO Users (email, password)
        VALUES (?, ?)
    """
    cursor.execute(insert_query, (email, password))
    conn.commit()
    conn.close()

def authenticate_user(email, password):
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    select_query = """
        SELECT * FROM Users WHERE email = ? AND password = ?
    """
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def init_ses_states():
    st.session_state.setdefault('chat_history', [])
    st.session_state.setdefault('user', None)
    st.session_state.setdefault('user_authenticated', False)  # Initialize user_authenticated

def relative_returns(df):
    rel = df.pct_change()
    cumret = ((1 + rel).cumprod() - 1).fillna(0)
    return cumret

def display_convo():
    with st.container():
        for i, message in enumerate(reversed(st.session_state.chat_history)):
            if i % 2 == 0:
                st.markdown(bot_template.replace("{{MSG}}", message), unsafe_allow_html=True)
            else:
                st.markdown(user_template.replace("{{MSG}}", message), unsafe_allow_html=True)

def approve_password(password):
    if len(password) >= 8 and re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_@$#!?&*%])", password):
        return True
    return False

def approve_email(email):
    email_regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(email_regex, email):
        return True
    else:
        return False

def get_line_chart(df):
    fig = go.Figure(data=go.Scatter(x=df.index, y=df['Close'], mode='lines'))
    return fig

def user_authentication_tab():
    with st.expander("User Authentication", expanded=True):
        login_tab, create_account_tab = st.tabs(["Login", "Create Account"])

        with login_tab:
            email = st.text_input("Email:") 
            password = st.text_input("Password:", type='password')
            if st.button("Login"):
                user = authenticate_user(email=email, password=password)
                if user and len(user) >= 3:
                    st.session_state.user = {'email': user[1]}
                    st.session_state.user_authenticated = True
                else:
                    st.caption('Incorrect Username or Password.')

            if st.session_state.user_authenticated and st.session_state.user:
                st.caption(f"User Authenticated: {st.session_state.user['email']}")

        with create_account_tab:
            new_email = st.text_input("New Email:")
            new_password = st.text_input("New Password:", type='password')
            confirm_password = st.text_input("Confirm Password:", type='password')
            if st.button("Create Account"):
                if not approve_email(new_email):
                    st.caption("Invalid Email")
                    return
                if not approve_password(new_password):
                    st.caption("Invalid Password")
                    return
                if new_password != confirm_password:
                    st.caption("Passwords do not match")
                    return
                add_user_to_db(email=new_email, password=new_password)
                st.caption(f"{new_email} Successfully Added")

def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Use GPT-3.5 Turbo engine
            prompt=prompt,
            temperature=0.5,
            max_tokens=150,
            n=1,
            stop=None,
            timeout=15,
        )
        return response.choices[0].text.strip()

    except Exception as e:
        st.error(f"An error occurred while communicating with the OpenAI API: {str(e)}")

def main():
    st.set_page_config(page_title="Stock Price AI Bot", page_icon=":chart:")
    st.write(css, unsafe_allow_html=True)
    create_users_db()
    init_ses_states()
    st.title("Stock Price AI Bot")
    st.caption("Visualizations and OpenAI Chatbot for Multiple Stocks Over A Specified Period")

    with st.sidebar:
        user_authentication_tab()

    if st.session_state.get('user_authenticated', False):
        with st.sidebar:
            with st.expander("Settings", expanded=True):
                # Updated list of available assets
                asset_tickers = sorted(['DOW', 'NVDA', 'TSLA', 'GOOGL', 'AMZN', 'AI', 'NIO', 'LCID', 'F', 'LYFY', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD', 'GOOG', 'NFLX', 'SPY'])
                asset_dropdown = st.multiselect('Pick Assets:', asset_tickers)

                metric_tickers = ['Adj. Close', 'Relative Returns']
                metric_dropdown = st.selectbox("Metric", metric_tickers)

                # Updated list of available charts
                viz_tickers = ['Line Chart', 'Area Chart', 'Line Chart (OHLC Data)']
                viz_dropdown = st.multiselect("Pick Charts:", viz_tickers)

                start = st.date_input('Start', value=pd.to_datetime('2023-01-01'))
                end = st.date_input('End', value=pd.to_datetime('today'))

                chatbot_temp = st.slider("Chat Bot Temperature", 0.0, 1.0, 0.5)

        if len(asset_dropdown) > 0:
            df = yf.download(asset_dropdown, start, end)
            if not df.empty:
                df = df['Adj Close']
                if metric_dropdown == 'Relative Returns':
                    df = relative_returns(df)
                if len(viz_dropdown) > 0:
                    with st.expander("Data Visualizations for {} of {}".format(metric_dropdown, asset_dropdown), expanded=True):
                        if "Line Chart" in viz_dropdown:
                            st.subheader("Line Chart")
                            st.line_chart(df)
                        if "Area Chart" in viz_dropdown:
                            st.subheader("Area Chart")
                            st.area_chart(df)
                        if "Line Chart (OHLC Data)" in viz_dropdown:
                            st.subheader("Line Chart (OHLC Data)")
                            st.plotly_chart(get_line_chart(df))

            st.header("Chat with your Data")

            query = st.text_input("Enter a query:")

            if st.button("Execute") and query:
                with st.spinner('Generating response...'):
                    try:
                        answer = get_openai_response(query)
                        st.session_state.chat_history.append(f"USER: {query}\n")
                        st.session_state.chat_history.append(f"AI: {answer}\n")
                        display_convo()

                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    load_dotenv()
    main()
