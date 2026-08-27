import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as mpl

df = yf.download(
    'AAPL',
    start='2020-01-01',
    end='2026-08-26'
)

close = df['Close']['AAPL']

sma_20 = close.rolling(20).mean()
sma_50 = close.rolling(50).mean()

signal = (sma_20 > sma_50).astype(int)

daily_return = close.pct_change()

strategy_return = signal * daily_return

cumulative_return = (strategy_return + 1).cumprod()

print("последние 20 торговых дней + сигнал: \n", signal.tail(20))
print("Доходность AAPL за последние 10 торговых дней: \n",daily_return.tail(10))
print("Последние 5 значений накопленого результа: \n",cumulative_return.tail())

mpl.plot(close, label="AAPL")
mpl.plot(sma_20, label="SMA 20")
mpl.plot(sma_50, label="SMA 50")

mpl.title("AAPL stock chart, SMA 20 & SMA 50")
mpl.xlabel("Date")
mpl.ylabel("Price")
mpl.legend()

mpl.show()