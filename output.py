def print_results(signal, metrics):
    
    print("\n" + "=" * 20, "SMA Strategy", "=" * 20)

    print(
    "Total return:",
    round(metrics["total_return"], 2),
    "%"
)
    
print(
    "Maximum drawdown:",
    round(metrics["max_drawdown"], 2),
    "%"
)


print("\n" + "=" * 20, "BUY & HOLD", "=" * 20)

print(
    "Total return:",
    round(metrics["total_buy_hold"], 2),
    "%"
)

print(
    "Maximum drawdown:",
    round(metrics["max_drawdown_buy_hold"], 2),
    "%"
)


print("\n" + "=" * 20, "Comparison", "=" * 20)

print(
    "Buy & Hold advantage:",
    round(metrics["difference"], 2),
    "percentage points"
)


print("\n" + "=" * 20, "Current Signal", "=" * 20)

print(
    "Signal:",
    signal.iloc[-1]
)


print("\n" + "-" * 20, "Risk Comparison", "-" * 20)

print(
    "SMA maximum drawdown:",
    round(metrics["max_drawdown"], 2),
    "%"
)

print(
    "Buy & hold maximum drawdown:",
    round(metrics["max_drawdown_buy_hold"], 2),
    "%"
)

print(
    "Drawdown difference:",
    round(metrics["drawdown_difference"], 2),
    "percentage points"
)


print("\n" + "=" * 20, "Trades", "=" * 20)

print(
    "Number of BUY signals:",
    metrics["number_of_buys"]
)

print(
    "Number of SELL signals:",
    metrics["number_of_sells"]
)


print("\n" + "=" * 20, "Trade Analysis", "=" * 20)

print(
    "Number of trades:",
    metrics["number_of_trades"]
)

print(
    "Winning trades:",
    metrics["winning_trades"]
)

print(
    "Losing trades:",
    metrics["losing_trades"]
)

print(
    "Win rate:",
    round(metrics["win_rate"], 2),
    "%"
)

print(
    "Average trade:",
    round(metrics["average_trade"], 2),
    "%"
)

print(
    "Profit factor:",
    round(metrics["profit_factor"], 2)
)


print("\nBest trade:")

print(
    "Date:",
    metrics["best_trade_date"]
)

print(
    "Return:",
    round(metrics["best_trade"], 2),
    "%"
)


print("\nWorst trade:")

print(
    "Date:",
    metrics["worst_trade_date"]
)

print(
    "Return:",
    round(metrics["worst_trade"], 2),
    "%"
)


print("\n" + "=" * 20, "Trade Table", "=" * 20)

print(
    metrics["trade_df"].round(2)
)


# CHARTS

plot_price_chart(
    close,
    sma_20,
    sma_50,
    buy_dates,
    sell_dates,
    buy_prices,
    sell_prices
)

plot_performance_chart(
    cumulative_return,
    cumulative_buy_hold
)

plot_drawdown_chart(
    metrics["drawdown"],
    metrics["drawdown_buy_hold"],
    metrics["sma_max_drawdown_date"],
    metrics["sma_max_drawdown_value"],
    metrics["buy_hold_max_drawdown_date"],
    metrics["buy_hold_max_drawdown_value"]
)