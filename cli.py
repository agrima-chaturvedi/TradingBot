# cli.py

import argparse
from bot import TradingBot

def get_user_input():
    print("\n📈 Welcome to the Simplified Binance Futures Trading Bot")
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Order side (BUY/SELL): ").upper()
    order_type = input("Order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Quantity to trade: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))

    return symbol, side, order_type, quantity, price


def main():
    parser = argparse.ArgumentParser(description="Simplified Binance Futures Trading Bot")
    parser.add_argument('--symbol', help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', type=float, help='Quantity to trade')
    parser.add_argument('--price', type=float, help='Price for LIMIT order (required if type is LIMIT)')

    args = parser.parse_args()

    # Check if CLI args are provided or fallback to interactive
    if all(v is None for v in [args.symbol, args.side, args.type, args.quantity]):
        symbol, side, order_type, quantity, price = get_user_input()
    else:
        # Validate required args
        if not all([args.symbol, args.side, args.type, args.quantity]):
            parser.error("Missing one or more required arguments.")
        if args.type == 'LIMIT' and not args.price:
            parser.error("--price is required for LIMIT orders")

        symbol = args.symbol.upper()
        side = args.side.upper()
        order_type = args.type.upper()
        quantity = args.quantity
        price = args.price

    # Execute order
    bot = TradingBot()
    order = bot.place_order(symbol, side, order_type, quantity, price)

    if order:
        print("✅ Order placed successfully!")
        print(order)
    else:
        print("❌ Order failed. Check logs for details.")

if __name__ == "__main__":
    main()
