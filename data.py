import yfinance as yf


def load_data():
    df = yf.download(
        "AAPL",
        start="2020-01-01",
        end="2026-08-29"
    )

    close = df["Close"]["AAPL"]
    close = close.dropna()

    return close