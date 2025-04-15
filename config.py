# config.py
"""
Configuration settings for the quantitative market analysis model.
Manage API keys, asset tickers, and analysis parameters here.
"""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file in the project root
# Create a .env file for sensitive data like API keys
# Example .env file:
# BITUNIX_API_KEY=your_key_here
# BITUNIX_SECRET_KEY=your_secret_here
load_dotenv()

# --- Logging Configuration ---
LOG_FILE = 'quant_model.log'
LOG_LEVEL = 'INFO' # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# --- Data Sources ---

# Yahoo Finance Tickers for traditional assets and volatility
# Keys are used internally (e.g., 'SP500'), Values are the symbols yfinance uses.
YFINANCE_TICKERS = {
    'SP500': '^GSPC',       # S&P 500 Index
    'NASDAQ100': '^NDX',    # Nasdaq 100 Index
    'DOWJONES': '^DJI',     # Dow Jones Industrial Average
    'VIX': '^VIX',          # CBOE Volatility Index
    'GOLD': 'GC=F',         # Gold Futures (Comex)
    'SILVER': 'SI=F',       # Silver Futures (Comex)
    'CRUDE_OIL': 'CL=F'     # WTI Crude Oil Futures (NYMEX)
}

# CCXT Configuration for Cryptocurrency Data
# Ensure the exchange ID is correct for Bitunix as per CCXT documentation
# Check https://github.com/ccxt/ccxt for supported exchanges and their IDs
EXCHANGE_ID = 'bitunix' # Verify this ID. Alternatives might be needed or use a larger exchange like 'binance' if tokens are listed there.

# Optional: Add API keys if needed for private data or higher rate limits
# It's STRONGLY recommended to use environment variables for security.
CCXT_API_KEY = os.getenv('BITUNIX_API_KEY')
CCXT_SECRET_KEY = os.getenv('BITUNIX_SECRET_KEY')
# Set to True if your keys are for a sandbox/testnet environment
CCXT_SANDBOX_MODE = False

# Crypto Tickers (Use CCXT format: BASE/QUOTE, e.g., 'BTC/USDT')
# Keys are used internally, Values are the symbols the exchange uses.
CRYPTO_TICKERS = {
    'BITCOIN': 'BTC/USDT',
    'ETHEREUM': 'ETH/USDT',
    # --- Add specific Solana ecosystem tokens available on Bitunix here ---
    # Verify these symbols EXACTLY match what Bitunix uses via CCXT
    'SOLANA': 'SOL/USDT',
    # 'BONK': 'BONK/USDT', # Example, verify symbol
    # 'JUPITER': 'JUP/USDT', # Example, verify symbol
    # 'PYTH': 'PYTH/USDT', # Example, verify symbol
}

# Define which Solana tokens are the primary focus for detailed analysis (subset of CRYPTO_TICKERS keys)
TARGET_SOLANA_TOKENS = ['SOLANA'] # Add keys like 'BONK', 'JUPITER' if defined above

# --- Analysis Parameters ---

# Data fetching period (e.g., '1y', '2y', '6mo', '3mo') passed to yfinance/ccxt
DATA_PERIOD = '2y'
# Data fetching interval (e.g., '1d' for daily, '1h' for hourly, '4h')
# Ensure the interval is supported by both yfinance and the CCXT exchange
DATA_INTERVAL = '1d'

# Rolling window for correlation calculation (in periods based on DATA_INTERVAL)
# E.g., 90 periods for a 90-day rolling correlation if interval is '1d'
CORRELATION_WINDOW = 90

# Beta calculation benchmark keys (must exist in YFINANCE_TICKERS or CRYPTO_TICKERS)
# Define benchmarks for comparing asset volatility
BETA_BENCHMARK_YAHOO = 'SP500'      # Traditional market benchmark
BETA_BENCHMARK_CRYPTO = 'BITCOIN'   # Crypto market benchmark

# GARCH Model Parameters (Generalized Autoregressive Conditional Heteroskedasticity)
# GARCH(p, q) orders. (1, 1) is a common starting point.
GARCH_P = 1
GARCH_Q = 1
# Volatility forecast horizon (number of periods ahead based on DATA_INTERVAL)
GARCH_FORECAST_HORIZON = 5
# GARCH model distribution assumption ('Normal', 't', 'skewt')
GARCH_DISTRIBUTION = 'Normal'

# --- API / Web UI Configuration ---
FLASK_HOST = '0.0.0.0' # Listen on all available network interfaces
FLASK_PORT = 5000      # Port for the web server
FLASK_DEBUG = False    # Set to False for production deployments

# --- Scheduler Configuration ---
# How often to automatically refresh data and analysis (in hours)
# Adjust based on DATA_INTERVAL and desired freshness
SCHEDULER_UPDATE_INTERVAL_HOURS = 6 # e.g., Run every 6 hours
