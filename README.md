
---

# 📈 Advanced Stock Price AI Bot 🤖

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-green?style=for-the-badge&logo=openai)
![YFinance](https://img.shields.io/badge/YFinance-0.2.28-yellow?style=for-the-badge)

Welcome to the **Advanced Stock Price AI Bot**! This is a powerful tool for stock market analysis, visualization, and AI-driven insights. Built with Python, Streamlit, and OpenAI's GPT-4, this application provides real-time stock data, technical analysis, and an AI-powered chatbot for financial queries. Whether you're a beginner or an experienced trader, this tool is designed to help you make informed decisions.

---

## 🚀 Features

### 📊 **Stock Data Visualization**
- **Interactive Charts**: Candlestick, Line, and Area charts for stock price trends.
- **Technical Indicators**: SMA, EMA, Bollinger Bands, and RSI for advanced analysis.
- **Comparative Analysis**: Compare multiple stocks in a single view.

### 🤖 **AI-Powered Chatbot**
- **Financial Insights**: Ask questions about stock performance, trends, and predictions.
- **Context-Aware Responses**: GPT-4 provides detailed and accurate answers based on historical data.
- **Customizable Temperature**: Adjust the creativity of AI responses.

### 🔒 **User Authentication**
- **Secure Login**: Password hashing for secure user authentication.
- **Portfolio Management**: Add and track your favorite stocks.

### 📈 **Advanced Analytics**
- **Relative Returns**: Calculate cumulative returns for selected stocks.
- **OHLC Data**: Open, High, Low, and Close prices for detailed analysis.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (for GPT-4)
- Streamlit (for the web interface)

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rohanpatil2/Advanced-Stock-AI-Bot.git
   cd Advanced-Stock-AI-Bot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

6. **Access the App**:
   - Open your browser and go to `http://localhost:8501`.

---

## 🖥️ Usage

### **1. User Authentication**
- **Login**: Use your email and password to access the app.
- **Register**: Create a new account with a secure password.

### **2. Stock Analysis**
- **Select Stocks**: Choose from a list of popular tickers (e.g., AAPL, TSLA, GOOGL).
- **Set Date Range**: Analyze stock performance over a specific period.
- **Visualize Data**: View interactive charts and technical indicators.

### **3. AI Chatbot**
- **Ask Questions**: Type your financial queries in the chatbox.
- **Get Insights**: Receive detailed responses from GPT-4.

### **4. Portfolio Management**
- **Add Stocks**: Track your favorite stocks in a personalized portfolio.
- **Remove Stocks**: Update your portfolio as needed.

---

## 📂 Project Structure

```
Advanced-Stock-AI-Bot/
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables
├── MASTER.db               # SQLite database for user authentication
├── README.md               # Project documentation
└── htmlTemplates/          # HTML templates for chat UI
    ├── css.py              # Custom CSS styles
    ├── user_template.html   # User chat template
    └── bot_template.html   # Bot chat template
```

---

## 📊 Example Queries for AI Chatbot

| **Query**                                      | **Example Response**                                                                 |
|------------------------------------------------|-------------------------------------------------------------------------------------|
| "What is the trend for AAPL in the last month?" | "AAPL has shown an upward trend with a 5% increase in the last month."              |
| "Compare TSLA and NVDA performance."           | "TSLA has grown by 10% while NVDA has grown by 8% over the last 3 months."          |
| "What are the Bollinger Bands for GOOGL?"      | "The Bollinger Bands for GOOGL indicate a period of low volatility."                |

---

## 🛠️ Technologies Used

| **Technology**       | **Purpose**                              |
|-----------------------|------------------------------------------|
| **Streamlit**         | Web application framework                |
| **YFinance**          | Fetching stock market data               |
| **OpenAI GPT-4**      | AI-powered financial insights            |
| **Plotly**            | Interactive data visualizations          |
| **SQLite**            | User authentication and data storage     |
| **Pandas**            | Data manipulation and analysis           |
| **NumPy**             | Numerical computations                   |

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## 📧 Contact

For questions or feedback, feel free to reach out:
- **GitHub**: [Rohanpatil2](https://github.com/Rohanpatil2)
- **Email**: [Your Email Address]

---

## 🌟 Show Your Support

If you find this project useful, please give it a ⭐️ on GitHub!

---

Enjoy using the **Advanced Stock Price AI Bot**! 🚀📈

---
