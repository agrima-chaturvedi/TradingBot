# ui_app.py

import tkinter as tk
from tkinter import messagebox
from bot import TradingBot

bot = TradingBot()

def place_order():
    symbol = symbol_entry.get().upper()
    side = side_var.get()
    order_type = type_var.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if not symbol or not side or not order_type or not quantity:
        messagebox.showwarning("Input Error", "All fields except price (for Market orders) are required.")
        return

    try:
        quantity = float(quantity)
        if order_type == "LIMIT":
            price = float(price)
            order = bot.place_order(symbol, side, order_type, quantity, price)
        else:
            order = bot.place_order(symbol, side, order_type, quantity)

        if order:
            last_order_id.set(order["orderId"])  # Save for cancel
            messagebox.showinfo("Success", f"✅ Order placed: ID {order['orderId']}")
        else:
            messagebox.showerror("Failed", "❌ Order failed. Check logs.")
    except ValueError:
        messagebox.showerror("Type Error", "Enter valid numeric values for quantity and price.")

def cancel_order():
    symbol = symbol_entry.get().upper()
    order_id = last_order_id.get()

    if not symbol or not order_id:
        messagebox.showwarning("Cancel Error", "Enter symbol and place an order first.")
        return

    try:
        order_id = int(order_id)
        result = bot.cancel_order(symbol, order_id)
        if result:
            messagebox.showinfo("Cancelled", f"🛑 Order {order_id} cancelled.")
        else:
            messagebox.showerror("Cancel Failed", "Could not cancel order. Check logs.")
    except ValueError:
        messagebox.showerror("Invalid Order ID", "Order ID should be numeric.")

def check_balance():
    balance_data = bot.get_balance()
    if balance_data:
        for asset in balance_data:
            if asset["asset"] == "USDT":
                messagebox.showinfo("Balance", f"USDT Balance: {asset['balance']}")
                return
        messagebox.showinfo("Balance", "USDT balance not found.")
    else:
        messagebox.showerror("Balance Error", "Failed to fetch balance.")

# --- UI Setup ---
root = tk.Tk()
root.title("🪙 Binance Futures Trading Bot")
root.geometry("420x430")
root.resizable(False, False)

# Shared variable to store last order ID
last_order_id = tk.StringVar()

tk.Label(root, text="Trading Pair (e.g., BTCUSDT)").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

tk.Label(root, text="Order Side").pack()
side_var = tk.StringVar(value="BUY")
tk.OptionMenu(root, side_var, "BUY", "SELL").pack()

tk.Label(root, text="Order Type").pack()
type_var = tk.StringVar(value="MARKET")
tk.OptionMenu(root, type_var, "MARKET", "LIMIT").pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Limit Price (only for LIMIT)").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Button(root, text="✅ Place Order", command=place_order, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="🛑 Cancel Last Order", command=cancel_order, bg="orange", fg="black").pack(pady=5)
tk.Button(root, text="💰 Check Balance", command=check_balance, bg="blue", fg="white").pack(pady=5)

tk.Label(root, text="Last Order ID").pack()
tk.Entry(root, textvariable=last_order_id).pack()

root.mainloop()
