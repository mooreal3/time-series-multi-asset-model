import matplotlib.pyplot as plt
import pandas as pd

def plot_ohlcv(data, title="OHLCV Chart"):
    # Convert data to a DataFrame for easier plotting
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    # Plot OHLCV data
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot the OHLC data
    ax1.plot(df.index, df["open"], label="Open")
    ax1.plot(df.index, df["high"], label="High")
    ax1.plot(df.index, df["low"], label="Low")
    ax1.plot(df.index, df["close"], label="Close")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price")
    ax1.set_title(title)
    ax1.legend()

    # Plot the volume data
    ax2 = ax1.twinx()
    ax2.bar(df.index, df["volume"], color="gray", alpha=0.3, label="Volume")
    ax2.set_ylabel("Volume")

    plt.legend()
    plt.show()

# Example usage: Plot OHLCV data for Solana (SOL)
# Assuming `solana_data` is the data fetched from `data_fetching.py`
# plot_ohlcv(solana_data, title="Solana (SOL) OHLCV Chart")
