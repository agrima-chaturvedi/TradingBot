from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging
from config import API_KEY, API_SECRET, BASE_URL

# Setup logger
logging.basicConfig(
    filename='logs/trading.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

class TradingBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)  # ✅ enables testnet
        self.client.FUTURES_URL = BASE_URL  # ✅ used only for futures
        logger.info("Initialized Binance Futures Testnet client.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price must be specified for LIMIT orders.")
                order_params.update({
                    "price": price,
                    "timeInForce": "GTC"  # Good-Til-Canceled
                })

            order = self.client.futures_create_order(**order_params)
            logger.info(f"Order placed successfully: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: {e}")
            return None
        except ValueError as ve:
            logger.error(f"ValueError: {ve}")
            return None

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            logger.info(f"Account Balance: {balance}")
            return balance
        except BinanceAPIException as e:
            logger.error(f"Balance check failed: {e}")
            return None
    def cancel_order(self, symbol, order_id):
        try:
            response = self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            logger.info(f"Order cancelled: {response}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Order cancel failed: {e}")
            return None

    def get_order_status(self, symbol, order_id):
        try:
            status = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            logger.info(f"Order Status: {status}")
            return status
        except BinanceAPIException as e:
            logger.error(f"Order status fetch failed: {e}")
            return None
