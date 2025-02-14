# 📊 Stock Price AI Bot

## 🚀 Overview
Stock Price AI Bot is a **Streamlit** web application designed to help users visualize stock prices and interact with an AI-powered chatbot using OpenAI's GPT-3.5 Turbo. This bot fetches stock market data from **Yahoo Finance (yfinance)** and provides an interactive visualization platform for analyzing stock trends and relative returns.

---
## ✨ Features

- 🔑 **User Authentication**: Secure login and signup functionality using SQLite.
- 📈 **Stock Data Visualization**:
  - Fetch historical stock prices from Yahoo Finance.
  - Interactive charting (Line Chart, Area Chart, OHLC Chart).
  - Supports multiple stock assets like **DOW, NVDA, TSLA, GOOGL, AMZN, BTC, ETH, AAPL, etc.**.
  - Compute and display **relative returns** over time.
- 🤖 **AI Chatbot Integration**:
  - Users can chat with OpenAI’s GPT-3.5 Turbo for stock-related insights.
  - Adjustable chatbot response **temperature settings**.
- 🔄 **Session State Management**: Preserves **chat history** and authentication status across sessions.
- 🔐 **Secure Password Handling**: Strong password enforcement for enhanced security.

---
## 🏗️ How It Works

### **1️⃣ User Authentication**
- Users **register** with an email and a strong password.
- Credentials are stored securely in an **SQLite database (MASTER.db)**.
- Users can **log in** to access personalized features.

### **2️⃣ Fetching Stock Market Data**
- Users select their **preferred stocks** from a predefined list.
- The app queries **Yahoo Finance (yfinance)** to fetch **historical stock prices**.
- Data is **preprocessed using Pandas** and stored in a structured format.

### **3️⃣ Visualizing Stock Trends**
- Users select a **metric** (Adjusted Close Price or Relative Returns).
- Choose a **chart type** (Line Chart, Area Chart, OHLC Chart).
- The selected stock data is **displayed using Plotly and Streamlit’s visualization tools**.

### **4️⃣ AI Chatbot for Insights**
- Users input a query about stock performance or financial advice.
- The query is sent to **OpenAI’s GPT-3.5 Turbo**.
- The chatbot generates a **contextual response** based on the stock data.

### **5️⃣ Session Management**
- Chat history and user authentication states are stored in **session variables**.
- Users can **log out and log in without losing progress**.

---
## 🔧 Installation Guide
### 🖥️ 1. Clone the Repository
```sh
  git clone https://github.com/RohanPatil2/Bot.git
  cd Bot
```

### 🏗️ 2. Create a Virtual Environment
```sh
  python -m venv venv
  source venv/bin/activate  # On macOS/Linux
  venv\Scripts\activate     # On Windows
```

### 📦 3. Install Required Dependencies
```sh
  pip install -r requirements.txt
```

### 🔑 4. Set Up Environment Variables
Create a `.env` file in the project directory and add your **OpenAI API Key**:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 🚀 5. Run the Application
```sh
  streamlit run app.py
```

---
## 🗃️ Database Structure
**Users Table (SQLite - MASTER.db):**
| Column | Data Type | Description |
|--------|----------|-------------|
| user_id | INTEGER (Primary Key) | Auto-incrementing user ID |
| email | TEXT | User's email (unique) |
| password | TEXT | Hashed password |

---
## 📊 Example Screenshots
### 📌 **Stock Data Visualization**
![Stock Chart](https://via.placeholder.com/800x400?text=Stock+Price+Visualization)

### 🔐 **User Authentication Interface**
![Login Page](https://via.placeholder.com/800x400?text=Login+Page)

### 💬 **AI Chatbot in Action**
![Chatbot](https://via.placeholder.com/800x400?text=AI+Chatbot+Response)

---
## 📦 Dependencies
- **Streamlit** - Web framework for UI components.
- **yfinance** - Retrieves stock market data.
- **Pandas** - Data manipulation and analysis.
- **Plotly** - Interactive stock price visualizations.
- **OpenAI** - GPT-3.5 Turbo API integration.
- **SQLite** - Local database for user authentication.
- **dotenv** - Secure environment variable handling.

---
## 🔮 Future Enhancements
- ✅ Implement **OAuth authentication** (Google, GitHub, etc.).
- 📊 Enable **real-time stock price updates**.
- 💡 Improve chatbot responses with a **financial knowledge base**.
- 🎨 Enhance **UI/UX** with better styling and interactive elements.

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 👨‍💻 Contributors
- **Rohan Patil** - [GitHub](https://github.com/RohanPatil2)
- Open for contributions! Feel free to **fork and submit PRs**! 🚀

---
## 📩 Contact
For any issues or feature requests, create an issue in the GitHub repository or email **[your_email@example.com](mailto:your_email@example.com)**.

