import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import re
from dotenv import load_dotenv
import sqlite3
import openai
import hashlib
import os
from datetime import datetime, timedelta
from htmlTemplates import css, user_template, bot_template

# Configuration
openai.api_key = os.getenv("OPENAI_API_KEY")
CACHE_EXPIRY = 3600  # 1 hour cache
DEFAULT_START_DATE = datetime.now() - timedelta(days=365*2)

# Technical Indicators
def calculate_technical_indicators(df, window=20):
    df['SMA'] = df['Close'].rolling(window=window).mean()
    df['EMA'] = df['Close'].ewm(span=window, adjust=False).mean()
    
    # Calculate Bollinger Bands
    df['STD'] = df['Close'].rolling(window=window).std()
    df['Upper Band'] = df['SMA'] + (df['STD'] * 2)
    df['Lower Band'] = df['SMA'] - (df['STD'] * 2)
    
    # Calculate RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df.dropna()

# Enhanced Authentication
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_db():
    with sqlite3.connect('MASTER.db') as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password_hash TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def add_user_to_db(email, password):
    with sqlite3.connect('MASTER.db') as conn:
        password_hash = hash_password(password)
        conn.execute("""
            INSERT INTO Users (email, password_hash)
            VALUES (?, ?)
        """, (email, password_hash))

def authenticate_user(email, password):
    with sqlite3.connect('MASTER.db') as conn:
        password_hash = hash_password(password)
        return conn.execute("""
            SELECT * FROM Users 
            WHERE email = ? AND password_hash = ?
        """, (email, password_hash)).fetchone()

# Cached Data Loading
@st.cache_data(ttl=CACHE_EXPIRY)
def load_data(tickers, start, end):
    return yf.download(tickers, start, end, group_by='ticker')

# Enhanced Visualization
def create_candlestick_chart(df, ticker):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name=ticker
    )])
    fig.update_layout(title=f'{ticker} Candlestick Chart', yaxis_title='Price')
    return fig

def create_technical_chart(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], name='SMA'))
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA'], name='EMA'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Upper Band'], name='Upper Band'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Lower Band'], name='Lower Band'))
    fig.update_layout(title=f'{ticker} Technical Indicators', yaxis_title='Price')
    return fig

# Enhanced AI Chat
def get_ai_response(query, context):
    messages = [
        {"role": "system", "content": "You are a financial analyst assistant. Provide detailed technical analysis."},
        {"role": "user", "content": f"Analyze this query: {query}. Context: {context}"}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

# Main Application
def main():
    st.set_page_config(page_title="Advanced Stock AI", layout="wide")
    st.write(css, unsafe_allow_html=True)
    create_users_db()
    
    # Session State Management
    if 'auth' not in st.session_state:
        st.session_state.auth = False
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = []
    
    # Authentication Sidebar
    with st.sidebar:
        if not st.session_state.auth:
            st.title("🔒 Authentication")
            auth_mode = st.radio("Choose:", ["Login", "Register"])
            
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            
            if st.button("Submit"):
                if auth_mode == "Login":
                    user = authenticate_user(email, password)
                    if user:
                        st.session_state.auth = True
                        st.success("Login successful!")
                    else:
                        st.error("Invalid credentials")
                else:
                    if authenticate_user(email, password):
                        st.error("User already exists")
                    else:
                        add_user_to_db(email, password)
                        st.success("Account created successfully!")
    
    # Main Interface
    if st.session_state.auth:
        st.title("📈 Advanced Stock Analysis Platform")
        
        # Portfolio Management
        with st.expander("💰 Portfolio Management"):
            col1, col2 = st.columns(2)
            with col1:
                new_asset = st.text_input("Add Asset (Ticker)")
                if st.button("Add to Portfolio"):
                    if new_asset not in st.session_state.portfolio:
                        st.session_state.portfolio.append(new_asset)
            with col2:
                selected_asset = st.selectbox("Remove Asset", st.session_state.portfolio)
                if st.button("Remove"):
                    st.session_state.portfolio.remove(selected_asset)
        
        # Data Analysis Section
        with st.expander("📊 Market Analysis"):
            selected_tickers = st.multiselect("Select Assets", st.session_state.portfolio)
            start_date = st.date_input("Start Date", DEFAULT_START_DATE)
            end_date = st.date_input("End Date", datetime.now())
            
            if selected_tickers:
                data = load_data(selected_tickers, start_date, end_date)
                
                # Enhanced Visualization Tabs
                tab1, tab2, tab3 = st.tabs(["Candlestick", "Technical", "Performance"])
                
                with tab1:
                    for ticker in selected_tickers:
                        st.plotly_chart(create_candlestick_chart(data[ticker], ticker))
                
                with tab2:
                    for ticker in selected_tickers:
                        analyzed_data = calculate_technical_indicators(data[ticker])
                        st.plotly_chart(create_technical_chart(analyzed_data, ticker))
                
                with tab3:
                    returns = data.xs('Close', axis=1, level=1).pct_change().cumsum()
                    st.line_chart(returns)
        
        # AI Chat Interface
        with st.expander("🤖 AI Analyst Assistant"):
            user_query = st.text_area("Ask your financial question:")
            if st.button("Analyze"):
                context = f"Analyzing {selected_tickers} from {start_date} to {end_date}"
                response = get_ai_response(user_query, context)
                
                st.markdown(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)
                st.session_state.chat_history.append(response)

if __name__ == "__main__":
    load_dotenv()
    main()
