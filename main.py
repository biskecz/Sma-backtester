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

signal_change = signal.diff()

# 1 = buy, -1 = sell, 0 = nothing
buy_signal = signal_change == 1
sell_signal = signal_change == -1

buy_dates = close.index[buy_signal]
sell_dates = close.index[sell_signal]

number_of_buys = buy_signal.sum()
number_of_sells = sell_signal.sum()

buy_prices = close.loc[buy_dates]
sell_prices = close.loc[sell_dates]

sma_max_drawdown_date = drawdown.idxmin()
buy_hold_max_drawdown_date = drawdown_buy_hold.idxmin()

sma_max_drawdown_value = drawdown.loc[sma_max_drawdown_date] * 100
buy_hold_max_drawdown_value = drawdown_buy_hold.loc[buy_hold_max_drawdown_date] * 100


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


print("\n" + "=" * 20, "Trades", "=" * 20)
print("Number of BUY signals:", number_of_buys)
print("Number of SELL signals:", number_of_sells)
print("\nBUY dates:")
print(buy_dates)
print("\nSELL dates:")
print(sell_dates)

# PRICE CHART
mpl.figure(figsize=(18,9))

mpl.plot(close, label="AAPL", linewidth=1.5)
mpl.plot(sma_20, label="SMA 20", linewidth=1.2, alpha=0.8)
mpl.plot(sma_50, label="SMA 50", linewidth=1.2, alpha=0.8)

mpl.scatter(
    buy_dates,
    buy_prices, 
    marker="^", 
    color="green",
    edgecolors="black",
    s=75,
    label="BUY",
    zorder=5
)

mpl.scatter(
sell_dates, 
    sell_prices, 
    marker="v", 
    color="red",
    edgecolors="black",
    s=75,
    label="SELL",
    zorder=5
)

mpl.title("AAPL - SMA 20 / SMA 50 Strategy")
mpl.xlabel("Date")
mpl.ylabel("Price")
mpl.legend()
mpl.grid(alpha=0.3)


# PERFORMANCE CHART
mpl.figure(figsize=(18, 7))

mpl.plot(cumulative_return, label="SMA Strategy")
mpl.plot(cumulative_buy_hold, label="Buy & Hold")

mpl.title("SMA Strategy VS Buy & Hold")
mpl.xlabel("Date")
mpl.ylabel("Cumulative Return")
mpl.legend()
mpl.grid(alpha=0.3)


# DRAWDOWN CHART
mpl.figure(figsize=(18, 7))

mpl.plot(
    drawdown * 100,
    label="SMA Strategy"
)

mpl.plot(
    drawdown_buy_hold * 100,
    label="Buy & Hold"
)

# SMA maximum drawdown
mpl.scatter(
    sma_max_drawdown_date,
    sma_max_drawdown_value,
    color="red",
    s=120,
    edgecolors="black",
    zorder=5,
    label=f"SMA Max Drawdown: {sma_max_drawdown_value:.2f}%"
)

# Buy & Hold maximum drawdown
mpl.scatter(
    buy_hold_max_drawdown_date,
    buy_hold_max_drawdown_value,
    color="orange",
    s=120,
    edgecolors="black",
    zorder=5,
    label=f"Buy & Hold Max Drawdown: {buy_hold_max_drawdown_value:.2f}%"
)

mpl.title("SMA Strategy VS Buy & Hold - Drawdown")
mpl.xlabel("Date")
mpl.ylabel("Drawdown (%)")
mpl.legend()
mpl.grid(alpha=0.3)


mpl.show()