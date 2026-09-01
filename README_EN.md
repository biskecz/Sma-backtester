# SMA Backtester

A simple Python backtesting project for testing a moving-average crossover strategy.

The project uses historical AAPL data and compares the SMA strategy against a passive Buy & Hold strategy.

## Here you can see more:
Demo on Youtube: https://www.youtube.com/watch?v=2nBrLU2di_k

## Features

* historical AAPL data;
* configurable SMA periods;
* BUY/SELL signals;
* transaction costs;
* Total Return;
* CAGR;
* Maximum Drawdown;
* Sharpe Ratio;
* Win Rate;
* Average Trade;
* Profit Factor;
* Best/Worst Trade;
* trade table;
* price and SMA chart;
* strategy vs Buy & Hold chart;
* Drawdown chart.

## Project Structure

```text
sma-backtester/
│
├── data.py
├── strategy.py
├── metrics.py
├── report.py
├── charts.py
├── main.py
├── README.md
└── README_EN.md
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install pandas numpy matplotlib yfinance
```

## Run

```bash
python main.py
```

## Strategy Settings

SMA periods and transaction costs can be changed in `main.py`:

```python
fast_window = 20
slow_window = 50
commission = 0.001
```

For example:

```python
fast_window = 10
slow_window = 30
```

## Strategy Logic

BUY:

```text
SMA fast > SMA slow
```

SELL:

```text
SMA fast < SMA slow
```

The previous day's signal is used when calculating strategy returns to avoid look-ahead bias.

## Transaction Costs

The commission is specified as a decimal fraction.

For example:

```text
0.001 = 0.1%
```

The commission is applied on every BUY and SELL signal.

## Metrics

### Total Return

Total strategy return over the backtest period.

### CAGR

Compound Annual Growth Rate.

### Maximum Drawdown

The largest decline from a previous portfolio peak.

### Sharpe Ratio

A risk-adjusted measure of strategy returns.

The calculation uses annualization based on 252 trading days.

## Buy & Hold

The strategy is compared against buying AAPL at the beginning of the period and holding it until the end.

## Project Goal

This project was created as a learning example of building a simple Python backtesting framework with separate modules for:

* data loading;
* strategy logic;
* metrics;
* reporting;
* visualization;
* application execution.

## Limitations

This is an educational backtester, not a production trading system.

It does not model:

* slippage;
* bid/ask spread;
* taxes;
* dividends separately;
* position sizing;
* capital management;
* market impact.

Historical backtest results do not guarantee future performance.
