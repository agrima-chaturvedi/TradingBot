# 🤖 Binance Futures Trading Bot

A simplified Binance Futures Trading Bot built in Python, connected to the [Binance Futures Testnet](https://testnet.binancefuture.com/). It allows users to place market and limit orders, check balance, cancel orders, and view order status — via CLI and a simple UI.

---

## 📦 Features

- ✅ Place **Market** and **Limit** orders
- 🔁 Support for both **BUY** and **SELL** sides
- 💼 Fetch **USDT account balance**
- 🛑 Cancel existing orders
- 📊 Check order execution status
- 🖥️ Simple Tkinter GUI interface
- 📄 Command-line interface (CLI)
- 🧾 Logs all actions and API errors in `logs/trading.log`

---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/<your-username>/binance-futures-bot.git<div>
cd binance-futures-bot<div>

### 2. Install Dependencies

pip install python-binance

### 3. Create config.py 

API_KEY = "your_api_key"<div>
API_SECRET = "your_api_secret"<div>
BASE_URL = "https://testnet.binancefuture.com"<div>

🚀 How to Use
📋 Run CLI App

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

For a LIMIT order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 68000

🖥️ Run UI App<div>
python ui_app.py

📁 Project Structure
binance-futures-bot/
├── bot.py              # Core TradingBot class<div>
├── cli.py              # Command-line interface<div>
├── ui_app.py           # Tkinter-based GUI<div>
├── config.py           # Your API keys (excluded)<div>
├── logs/<div>
│   └── trading.log     # Order activity and error logs<div>
├── .gitignore<div>
└── README.md<div>

📝 Log Files

 All API requests, order responses, and errors are logged in logs/trading.log.<div>
 Logging is encoded in UTF-8 to support emoji and symbols.

📎 Binance Futures Testnet

  Register here: https://testnet.binancefuture.com<div>
  Get USDT testnet balance<div>
  Create API keys for testnet<div>
  Add them to config.py<div>

💡 Optional Enhancements

Add support for Stop-Limit or OCO orders<div>
Add order history tracking<div>
Integrate WebSockets for real-time updates<div>
Host a lightweight Flask frontend<div>


![image](https://github.com/user-attachments/assets/5e422396-6b78-4a14-963a-613dc07d5b07)
![image](https://github.com/user-attachments/assets/0856525c-9af6-445d-8080-21e77af76f5a)

👨‍💻 Author

Agrima Chaturvedi
