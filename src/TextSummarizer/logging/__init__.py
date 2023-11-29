import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.mkdir(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),  # to store log in a file name running_logs.log
        logging.StreamHandler(sys.stdout)  # to get log at terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")