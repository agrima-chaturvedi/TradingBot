# logger.py
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/trading.log',
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s',
    filemode='a'  # Append mode
)

logger = logging.getLogger()
