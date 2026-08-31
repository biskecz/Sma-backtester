def calculate_strategy(
    close,
    fast_window=20,
    slow_window=50,
    commission=0.001
):

    # SMA

    sma_fast = close.rolling(
        fast_window
    ).mean()

    sma_slow = close.rolling(
        slow_window
    ).mean()


    # SIGNAL

    signal = (
        sma_fast > sma_slow
    ).astype(int)


    # DAILY RETURN

    daily_return = close.pct_change()


    # BUY / SELL SIGNALS

    signal_change = signal.diff()

    buy_signal = signal_change == 1
    sell_signal = signal_change == -1


    # TRANSACTION COSTS

    transaction_cost = (
        signal.astype(float) * 0
    )

    transaction_cost.loc[
        buy_signal
    ] = -commission

    transaction_cost.loc[
        sell_signal
    ] = -commission


    # STRATEGY RETURN

    strategy_return = (
        signal.shift(1) * daily_return
        + transaction_cost
    )


    # CUMULATIVE RETURN

    cumulative_return = (
        strategy_return + 1
    ).cumprod()

    cumulative_buy_hold = (
        daily_return + 1
    ).cumprod()


    # TRADE DATA

    buy_dates = close.index[buy_signal]
    sell_dates = close.index[sell_signal]

    buy_prices = close.loc[buy_dates]
    sell_prices = close.loc[sell_dates]


    return {
        "sma_fast": sma_fast,
        "sma_slow": sma_slow,
        "signal": signal,

        "cumulative_return":
            cumulative_return,

        "cumulative_buy_hold":
            cumulative_buy_hold,

        "buy_dates": buy_dates,
        "sell_dates": sell_dates,

        "buy_prices": buy_prices,
        "sell_prices": sell_prices,

        "fast_window": fast_window,
        "slow_window": slow_window,
        "commission": commission
    }
