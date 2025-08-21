import os
from datetime import datetime
import yfinance as yf
from src.utils.io import ensure_dirs, save_csv
from src.utils.config import load_config
from src.utils.logging import get_logger

def main():
    cfg = load_config()
    logger = get_logger()
    ensure_dirs(cfg["paths"])

    tickers = cfg
