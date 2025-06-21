from bot import TradingBot

bot = TradingBot()

# ✅ Make sure this is a valid futures symbol and quantity
symbol = "BTCUSDT"
side = "BUY"
order_type = "MARKET"
quantity = 0.001

order = bot.place_order(symbol, side, order_type, quantity)

if order:
    print("✅ Order executed successfully.")
else:
    print("❌ Order failed. Check logs/trading.log")

