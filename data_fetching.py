import ccxt
from config import CRYPTO_TICKERS, EXCHANGE_ID, CCXT_API_KEY, CCXT_SECRET_KEY, CCXT_SANDBOX_MODE

# Initialize the CCXT exchange object
exchange_class = getattr(ccxt, EXCHANGE_ID)
exchange = exchange_class({
    'apiKey': CCXT_API_KEY,
    'secret': CCXT_SECRET_KEY,
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'},
})

# Enable sandbox mode if required
if CCXT_SANDBOX_MODE:
    exchange.set_sandbox_mode(True)

# Function to fetch data for a specific Solana token
def fetch_solana_token_data(token_symbol):
    # Check if the token symbol is in the CRYPTO_TICKERS dictionary
    if token_symbol in CRYPTO_TICKERS:
        # Fetch the ticker data using CCXT
        ticker = CRYPTO_TICKERS[token_symbol]
        try:
            # Fetch the OHLCV data (Open, High, Low, Close, Volume)
            ohlcv = exchange.fetch_ohlcv(ticker, timeframe='1d')
            return ohlcv
        except Exception as e:
            print(f"Error fetching data for {token_symbol}: {e}")
            return None
    else:
        print(f"Token symbol {token_symbol} not found in CRYPTO_TICKERS.")
        return None

# Example usage: Fetch data for Solana (SOL)
solana_data = fetch_solana_token_data('SOLANA')
if solana_data:
    print(f"Fetched data for Solana (SOL): {solana_data}")
