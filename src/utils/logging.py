import logging

def get_logger(name="stock_select"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        h  = logging.StreamHandler()
        h.setLevel(loggingFormatter())