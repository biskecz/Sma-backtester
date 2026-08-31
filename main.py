from data import load_data
from strategy import calculate_strategy
from metrics import calculate_metrics
from report import print_results
from charts import show_charts

import matplotlib.pyplot as mpl


def main():

    # SETTINGS

    fast_window = 20
    slow_window = 50

    commission = 0.001


    # DATA

    close = load_data()


    # STRATEGY

    strategy = calculate_strategy(
        close,
        fast_window,
        slow_window,
        commission
    )


    # METRICS

    metrics = calculate_metrics(
        close,
        strategy
    )


    # REPORT

    print_results(
        strategy,
        metrics
    )


    # CHARTS

    show_charts(
        close,
        strategy,
        metrics
    )

    mpl.show()


if __name__ == "__main__":
    main()
