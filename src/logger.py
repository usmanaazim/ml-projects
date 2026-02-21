import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(log_file, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_file, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s -  %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    logging.info("Logging has started.")