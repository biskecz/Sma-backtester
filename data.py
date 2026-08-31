import yfinance as yf


def load_data(
    ticker="AAPL",
    start="2020-01-01",
    end=None
):

    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True,
        progress=True
    )

    if data.empty:
        raise ValueError(
            "No data was downloaded."
        )

    close = data["Close"]

    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    return close.dropna()
