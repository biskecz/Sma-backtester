from data import load_data
from strategy import calculate_strategy
from metrics import calculate_metrics
from report import print_results
from charts import show_charts

import matplotlib.pyplot as mpl


def main():

    close = load_data()

    fast_window = 50
    slow_window = 200
    
    commission = 0.001
    strategy = calculate_strategy(
        close,
        fast_window,
        slow_window,
        commission
    )
    

    metrics = calculate_metrics(
        close,
        strategy
    )

    print_results(
        strategy,
        metrics
    )

    show_charts(
        close,
        strategy,
        metrics
    )

    mpl.show()


if __name__ == "__main__":
    main()