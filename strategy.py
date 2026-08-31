def calculate_strategy(
    close,
    fast_window=20,
    slow_window=50,
    commission=0.001
):

    sma_20 = close.rolling(fast_window).mean()
    sma_50 = close.rolling(slow_window).mean()

    signal = (sma_20 > sma_50).astype(int)

    daily_return = close.pct_change()

    signal_change = signal.diff()

    buy_signal = signal_change == 1
    sell_signal = signal_change == -1

    transaction_cost = signal.astype(float) * 0

    transaction_cost.loc[buy_signal] = -commission
    transaction_cost.loc[sell_signal] = -commission

    strategy_return = (
        signal.shift(1) * daily_return
        + transaction_cost
    )

    cumulative_return = (
        strategy_return + 1
    ).cumprod()

    cumulative_buy_hold = (
        daily_return + 1
    ).cumprod()

    buy_dates = close.index[buy_signal]
    sell_dates = close.index[sell_signal]

    buy_prices = close.loc[buy_dates]
    sell_prices = close.loc[sell_dates]

    return {
        "sma_20": sma_20,
        "sma_50": sma_50,
        "signal": signal,
        "cumulative_return": cumulative_return,
        "cumulative_buy_hold": cumulative_buy_hold,
        "buy_dates": buy_dates,
        "sell_dates": sell_dates,
        "buy_prices": buy_prices,
        "sell_prices": sell_prices
    }