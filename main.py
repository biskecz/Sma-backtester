import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mpl


# DATA BLOCK
df = yf.download(
    'AAPL',
    start='2020-01-01',
    end='2026-08-29'
)

close = df['Close']['AAPL']
close = close.dropna()

# SMA INDICATORS
sma_20 = close.rolling(20).mean()
sma_50 = close.rolling(50).mean()

# SMA STRATEGY
signal = (sma_20 > sma_50).astype(int)
daily_return = close.pct_change()
strategy_return = signal.shift(1) * daily_return
cumulative_return = (strategy_return + 1).cumprod()
total_return = ((cumulative_return.iloc[-1] - 1) * 100)

# BUY & HOLD
cumulative_buy_hold = (daily_return + 1).cumprod()
total_buy_hold = ((cumulative_buy_hold.iloc[-1] - 1) * 100)     

# COMPARISON 
difference = total_buy_hold - total_return 

# SMA DRAWDOWN 
running_max = cumulative_return.cummax()
drawdown = (cumulative_return - running_max) / running_max
max_drawdown = drawdown.min() * 100
running_max_buy_hold = cumulative_buy_hold.cummax()
drawdown_buy_hold = (
    cumulative_buy_hold - running_max_buy_hold
) / running_max_buy_hold

max_drawdown_buy_hold = drawdown_buy_hold.min() * 100

drawdown_difference = max_drawdown_buy_hold - max_drawdown


# OUTPUT BLOCK

print("\n" + "=" * 20, "SMA Strategy", "=" * 20)
print("Total return:", round(total_return, 2), "%")
print("Maximum drawdown:", round(max_drawdown, 2), "%")

print("\n" + "=" * 20, "BUY & HOLD", "=" * 20)
print("Total return:", round(total_buy_hold, 2), "%")
print("Maximum drawdown", round(max_drawdown_buy_hold, 2), "%")

print("\n" + "=" * 20, "Comparison", "=" * 20)
print("Buy & Hold advantage:", round(difference, 2), "percentage points")

print("\n" + "=" * 20, "Current Signal", "=" * 20)
print("Signal:", signal.iloc[-1])

print("\n" + "-" * 20, "Risk Comparison", "-" * 20)
print("SMA maximum drawdown: ", round(max_drawdown, 2), "%")
print("Buy & hold maximum drawdown: ", round(max_drawdown_buy_hold, 2), "%")
print("Drawdown difference:", round(drawdown_difference, 2), "percentage points")


# PRICE CHART
mpl.figure()

mpl.plot(close, label="AAPL")
mpl.plot(sma_20, label="SMA 20")
mpl.plot(sma_50, label="SMA 50")

mpl.title("AAPL stock chart, SMA 20 & SMA 50")
mpl.xlabel("Date")
mpl.ylabel("Price")
mpl.legend()


# PERFORMANCE CHART
mpl.figure()

mpl.plot(cumulative_return, label="SMA strategy")
mpl.plot(cumulative_buy_hold, label="Buy & Hold")

mpl.title("SMA strategy VS Buy & Hold")
mpl.xlabel("Date")
mpl.ylabel("Cumulative Return")
mpl.legend()

mpl.show()