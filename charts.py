import matplotlib.pyplot as mpl


def plot_price_chart(close, strategy):

    mpl.figure(figsize=(18, 9))

    mpl.plot(
        close,
        label="AAPL",
        linewidth=1.5
    )

    mpl.plot(
        strategy["sma_20"],
        label="SMA 20",
        linewidth=1.2,
        alpha=0.8
    )

    mpl.plot(
        strategy["sma_50"],
        label="SMA 50",
        linewidth=1.2,
        alpha=0.8
    )

    mpl.scatter(
        strategy["buy_dates"],
        strategy["buy_prices"],
        marker="^",
        color="green",
        edgecolors="black",
        s=75,
        label="BUY",
        zorder=5
    )

    mpl.scatter(
        strategy["sell_dates"],
        strategy["sell_prices"],
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


def plot_performance_chart(strategy):

    mpl.figure(figsize=(18, 7))

    mpl.plot(
        strategy["cumulative_return"],
        label="SMA Strategy"
    )

    mpl.plot(
        strategy["cumulative_buy_hold"],
        label="Buy & Hold"
    )

    mpl.title("SMA Strategy VS Buy & Hold")
    mpl.xlabel("Date")
    mpl.ylabel("Cumulative Return")
    mpl.legend()
    mpl.grid(alpha=0.3)


def plot_drawdown_chart(metrics):

    mpl.figure(figsize=(18, 7))

    mpl.plot(
        metrics["drawdown"] * 100,
        label="SMA Strategy"
    )

    mpl.plot(
        metrics["drawdown_buy_hold"] * 100,
        label="Buy & Hold"
    )

    mpl.scatter(
        metrics["sma_max_drawdown_date"],
        metrics["sma_max_drawdown_value"],
        color="red",
        s=120,
        edgecolors="black",
        zorder=5,
        label=(
            f"SMA Max Drawdown: "
            f"{metrics['sma_max_drawdown_value']:.2f}%"
        )
    )

    mpl.scatter(
        metrics["buy_hold_max_drawdown_date"],
        metrics["buy_hold_max_drawdown_value"],
        color="orange",
        s=120,
        edgecolors="black",
        zorder=5,
        label=(
            f"Buy & Hold Max Drawdown: "
            f"{metrics['buy_hold_max_drawdown_value']:.2f}%"
        )
    )

    mpl.title("SMA Strategy VS Buy & Hold - Drawdown")
    mpl.xlabel("Date")
    mpl.ylabel("Drawdown (%)")
    mpl.legend()
    mpl.grid(alpha=0.3)


def show_charts(close, strategy, metrics):

    plot_price_chart(
        close,
        strategy
    )

    plot_performance_chart(
        strategy
    )

    plot_drawdown_chart(
        metrics
    )