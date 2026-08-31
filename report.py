def print_results(strategy, metrics):

    signal = strategy["signal"]

    fast_window = strategy["fast_window"]
    slow_window = strategy["slow_window"]

    commission = strategy["commission"]


    print(
        "\n"
        + "=" * 20,
        "SMA Strategy",
        "=" * 20
    )

    print(
        "SMA:",
        fast_window,
        "/",
        slow_window
    )

    print(
        "Commission:",
        commission * 100,
        "%"
    )

    print(
        "Total return:",
        round(
            metrics["total_return"],
            2
        ),
        "%"
    )

    print(
        "CAGR:",
        round(
            metrics["cagr"],
            2
        ),
        "%"
    )

    print(
        "Sharpe ratio:",
        round(
            metrics["sharpe_ratio"],
            2
        )
    )

    print(
        "Maximum drawdown:",
        round(
            metrics["max_drawdown"],
            2
        ),
        "%"
    )


    print(
        "\n"
        + "=" * 20,
        "BUY & HOLD",
        "=" * 20
    )

    print(
        "Total return:",
        round(
            metrics["total_buy_hold"],
            2
        ),
        "%"
    )

    print(
        "CAGR:",
        round(
            metrics["buy_hold_cagr"],
            2
        ),
        "%"
    )

    print(
        "Sharpe ratio:",
        round(
            metrics["sharpe_buy_hold"],
            2
        )
    )

    print(
        "Maximum drawdown:",
        round(
            metrics["max_drawdown_buy_hold"],
            2
        ),
        "%"
    )


    print(
        "\n"
        + "=" * 20,
        "Comparison",
        "=" * 20
    )

    print(
        "Buy & Hold advantage:",
        round(
            metrics["difference"],
            2
        ),
        "percentage points"
    )


    print(
        "\n"
        + "=" * 20,
        "Current Signal",
        "=" * 20
    )

    print(
        "Signal:",
        signal.iloc[-1]
    )


    print(
        "\n"
        + "-" * 20,
        "Risk Comparison",
        "-" * 20
    )

    print(
        "SMA maximum drawdown:",
        round(
            metrics["max_drawdown"],
            2
        ),
        "%"
    )

    print(
        "Buy & hold maximum drawdown:",
        round(
            metrics["max_drawdown_buy_hold"],
            2
        ),
        "%"
    )

    print(
        "Drawdown difference:",
        round(
            metrics["drawdown_difference"],
            2
        ),
        "percentage points"
    )


    print(
        "\n"
        + "=" * 20,
        "Trades",
        "=" * 20
    )

    print(
        "Number of BUY signals:",
        metrics["number_of_buys"]
    )

    print(
        "Number of SELL signals:",
        metrics["number_of_sells"]
    )


    print(
        "\n"
        + "=" * 20,
        "Trade Analysis",
        "=" * 20
    )

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
        round(
            metrics["win_rate"],
            2
        ),
        "%"
    )

    print(
        "Average trade:",
        round(
            metrics["average_trade"],
            2
        ),
        "%"
    )

    print(
        "Profit factor:",
        round(
            metrics["profit_factor"],
            2
        )
    )


    print("\nBest trade:")

    print(
        "Date:",
        metrics["best_trade_date"]
    )

    print(
        "Return:",
        round(
            metrics["best_trade"],
            2
        ),
        "%"
    )


    print("\nWorst trade:")

    print(
        "Date:",
        metrics["worst_trade_date"]
    )

    print(
        "Return:",
        round(
            metrics["worst_trade"],
            2
        ),
        "%"
    )


    print(
        "\n"
        + "=" * 20,
        "Trade Table",
        "=" * 20
    )

    trade_df = (
        metrics["trade_df"].copy()
    )

    trade_df["BUY price"] = (
        trade_df["BUY price"].round(2)
    )

    trade_df["SELL price"] = (
        trade_df["SELL price"].round(2)
    )

    trade_df["Return (%)"] = (
        trade_df["Return (%)"].round(2)
    )

    print(trade_df)

