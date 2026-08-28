import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as mpl

df = yf.download(
    'AAPL',
    start='2020-01-01',
    end='2026-08-27'
)

close = df['Close']['AAPL']

sma_20 = close.rolling(20).mean()
sma_50 = close.rolling(50).mean()
signal = (sma_20 > sma_50).astype(int)
daily_return = close.pct_change()
strategy_return = signal * daily_return
cumulative_return = (strategy_return + 1).cumprod()
total_return = ((cumulative_return.tail(1) - 1) * 100)          # SMA 20 / SMA 50
cumulative_buy_hold = (daily_return + 1).cumprod()
total_buy_hold = ((cumulative_buy_hold.tail(1) - 1 ) * 100)     # buy & hold
difference = total_buy_hold - total_return 

print("Последние 20 торговых дней + сигнал: \n", signal.tail(20))
print("Доходность AAPL за последние 10 торговых дней: \n",daily_return.tail(10))
print("Последние 5 значений накопленого результата: \n",cumulative_return.tail())
print("Итоговая доходность стратегии:", total_return)
print("Накопленный результат Buy & Hold: \n", cumulative_buy_hold)
print("Итоговая доходность Buy & Hold:", total_buy_hold)
print("Преимущество BUY & HOLD над SMA: ", difference)

# графики AAPL price и SMA (20 & 50)
mpl.figure()

mpl.plot(close, label="AAPL")
mpl.plot(sma_20, label="SMA 20")
mpl.plot(sma_50, label="SMA 50")

mpl.title("AAPL stock chart, SMA 20 & SMA 50")
mpl.xlabel("Date")
mpl.ylabel("Price")
mpl.legend()

# сравнение доходности SMA против Buy & Hold
mpl.figure()

mpl.plot(cumulative_return, label="SMA strategy")
mpl.plot(cumulative_buy_hold, label="Buy & Hold")

mpl.title("SMA strategy VS Buy & Hold")
mpl.xlabel("Date")
mpl.ylabel("Cumulative Return")
mpl.legend()

mpl.show()
