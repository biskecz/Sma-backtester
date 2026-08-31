import pandas as pd


def calculate_metrics(close, strategy):

    cumulative_return = strategy["cumulative_return"]
    cumulative_buy_hold = strategy["cumulative_buy_hold"]

    buy_dates = strategy["buy_dates"]
    sell_dates = strategy["sell_dates"]

    buy_prices = strategy["buy_prices"]
    sell_prices = strategy["sell_prices"]


    # TOTAL RETURN

    total_return = (
        cumulative_return.iloc[-1] - 1
    ) * 100

    total_buy_hold = (
        cumulative_buy_hold.iloc[-1] - 1
    ) * 100

    difference = total_buy_hold - total_return


    # DRAWDOWN

    running_max = cumulative_return.cummax()

    drawdown = (
        cumulative_return - running_max
    ) / running_max

    max_drawdown = drawdown.min() * 100


    running_max_buy_hold = cumulative_buy_hold.cummax()

    drawdown_buy_hold = (
        cumulative_buy_hold - running_max_buy_hold
    ) / running_max_buy_hold

    max_drawdown_buy_hold = (
        drawdown_buy_hold.min() * 100
    )

    drawdown_difference = (
        max_drawdown_buy_hold - max_drawdown
    )


    # DRAWDOWN DATES

    sma_max_drawdown_date = drawdown.idxmin()

    buy_hold_max_drawdown_date = (
        drawdown_buy_hold.idxmin()
    )

    sma_max_drawdown_value = (
        drawdown.loc[sma_max_drawdown_date] * 100
    )

    buy_hold_max_drawdown_value = (
        drawdown_buy_hold.loc[
            buy_hold_max_drawdown_date
        ] * 100
    )


    # SIGNALS

    number_of_buys = len(buy_dates)
    number_of_sells = len(sell_dates)


    # TRADE ANALYSIS

    trade_return = (
        sell_prices.to_numpy()
        / buy_prices.to_numpy()
        - 1
    ) * 100

    number_of_trades = len(trade_return)

    winning_trades = trade_return > 0
    losing_trades = trade_return < 0

    win_rate = (
        winning_trades.sum()
        / number_of_trades
        * 100
    )

    average_trade = trade_return.mean()


    # BEST TRADE

    best_trade_index = trade_return.argmax()

    best_trade = trade_return[best_trade_index]

    best_trade_date = (
        sell_dates[best_trade_index]
    )


    # WORST TRADE

    worst_trade_index = trade_return.argmin()

    worst_trade = trade_return[worst_trade_index]

    worst_trade_date = (
        sell_dates[worst_trade_index]
    )


    # PROFIT FACTOR

    gross_profit = (
        trade_return[trade_return > 0].sum()
    )

    gross_loss = (
        -trade_return[trade_return < 0].sum()
    )

    profit_factor = gross_profit / gross_loss


    # TRADE TABLE

    trade_df = pd.DataFrame({
        "BUY date": buy_dates.to_numpy(),
        "BUY price": buy_prices.to_numpy(),
        "SELL date": sell_dates.to_numpy(),
        "SELL price": sell_prices.to_numpy(),
        "Return (%)": trade_return
    })

    trade_df.index = range(
        1,
        len(trade_df) + 1
    )

    trade_df.index.name = "Trade"


    return {
        "total_return": total_return,
        "total_buy_hold": total_buy_hold,
        "difference": difference,

        "drawdown": drawdown,
        "drawdown_buy_hold": drawdown_buy_hold,

        "max_drawdown": max_drawdown,
        "max_drawdown_buy_hold": max_drawdown_buy_hold,
        "drawdown_difference": drawdown_difference,

        "sma_max_drawdown_date": sma_max_drawdown_date,
        "buy_hold_max_drawdown_date": buy_hold_max_drawdown_date,

        "sma_max_drawdown_value": sma_max_drawdown_value,
        "buy_hold_max_drawdown_value": buy_hold_max_drawdown_value,

        "number_of_buys": number_of_buys,
        "number_of_sells": number_of_sells,

        "trade_return": trade_return,
        "number_of_trades": number_of_trades,

        "winning_trades": winning_trades.sum(),
        "losing_trades": losing_trades.sum(),

        "win_rate": win_rate,
        "average_trade": average_trade,

        "best_trade": best_trade,
        "best_trade_date": best_trade_date,

        "worst_trade": worst_trade,
        "worst_trade_date": worst_trade_date,

        "profit_factor": profit_factor,

        "trade_df": trade_df
    }