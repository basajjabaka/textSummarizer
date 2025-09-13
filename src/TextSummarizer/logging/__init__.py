import os
import sys
import logging

logStr = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
logDir = "logs"
logPath = os.path.join(logDir, "runningLogs.log")
os.makedirs(logDir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logStr,
    handlers = [
        logging.FileHandler(logPath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")