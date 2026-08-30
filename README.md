# SMA Backtester

## 🇷🇺 Русская версия

Простой backtester торговой стратегии на основе пересечения **SMA 20** и **SMA 50**.

Проект загружает исторические данные AAPL, рассчитывает торговые сигналы и сравнивает результат стратегии с обычным **Buy & Hold**.

### Возможности

* Загрузка исторических данных через `yfinance`
* Расчёт SMA 20 и SMA 50
* Определение BUY и SELL сигналов
* Расчёт общей доходности стратегии
* Сравнение с Buy & Hold
* Расчёт Maximum Drawdown
* Анализ отдельных сделок
* Расчёт Win Rate
* Расчёт средней доходности сделки
* Поиск лучшей и худшей сделки
* Таблица всех сделок
* Визуализация результатов

### Как работает стратегия

Используются две скользящие средние:

* **SMA 20** — короткая средняя
* **SMA 50** — длинная средняя

Основное правило:

```text
SMA 20 > SMA 50 → BUY / LONG
SMA 20 < SMA 50 → SELL / OUT
```

BUY сигнал появляется при изменении:

```text
0 → 1
```

SELL сигнал появляется при изменении:

```text
1 → 0
```

Доходность стратегии рассчитывается с использованием сигнала предыдущего торгового дня.

### Основные метрики

**Total Return**

Общая доходность стратегии за выбранный период.

**Maximum Drawdown**

Максимальное падение капитала от предыдущего максимума.

**Win Rate**

Процент прибыльных сделок:

```text
Winning trades / Total trades
```

**Average Trade**

Средняя доходность одной завершённой сделки.

**Best Trade**

Самая прибыльная сделка.

**Worst Trade**

Самая убыточная сделка.

### Графики

Проект создаёт три графика.

**1. Price Chart**

Показывает:

* цену AAPL
* SMA 20
* SMA 50
* BUY сигналы
* SELL сигналы

**2. Performance Chart**

Сравнивает:

* SMA Strategy
* Buy & Hold

**3. Drawdown Chart**

Сравнивает:

* Drawdown SMA Strategy
* Drawdown Buy & Hold
* Maximum Drawdown обеих стратегий

### Trade Analysis

Для каждой завершённой сделки создаётся таблица:

```text
Trade
BUY date
BUY price
SELL date
SELL price
Return (%)
```

Это позволяет отдельно анализировать результаты каждой сделки.

### Установка

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его в PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Установить зависимости:

```bash
pip install pandas yfinance matplotlib
```

### Запуск

```bash
python main.py
```

### Структура проекта

```text
sma-backtester/
│
├── main.py
├── README.md
└── .gitignore
```

### Текущий результат

На текущем тестовом периоде:

```text
SMA Strategy
Total return: 121.58%
Maximum drawdown: -29.09%

Buy & Hold
Total return: 342.36%
Maximum drawdown: -33.36%

Number of trades: 20
Winning trades: 10
Losing trades: 10
Win rate: 50.0%
Average trade: 5.05%
```

Результаты зависят от выбранного периода и исторических данных.

### Цель проекта

Проект создан для практики работы с:

* Python
* pandas
* yfinance
* matplotlib
* торговыми стратегиями
* backtesting
* анализом доходности
* анализом риска

Проект предназначен для обучения и исследования и **не является финансовой рекомендацией**.

---

# SMA Backtester

## 🇬🇧 English Version

A simple backtester for a trading strategy based on the crossover of **SMA 20** and **SMA 50**.

The project downloads historical AAPL data, generates trading signals, and compares the strategy performance with a simple **Buy & Hold** approach.

### Features

* Download historical data using `yfinance`
* Calculate SMA 20 and SMA 50
* Generate BUY and SELL signals
* Calculate total strategy return
* Compare the strategy with Buy & Hold
* Calculate Maximum Drawdown
* Analyze individual trades
* Calculate Win Rate
* Calculate average trade return
* Find the best and worst trades
* Create a trade table
* Visualize the results

### How the Strategy Works

The strategy uses two moving averages:

* **SMA 20** — short-term moving average
* **SMA 50** — long-term moving average

Main rule:

```text
SMA 20 > SMA 50 → BUY / LONG
SMA 20 < SMA 50 → SELL / OUT
```

A BUY signal appears when the signal changes:

```text
0 → 1
```

A SELL signal appears when the signal changes:

```text
1 → 0
```

Strategy returns are calculated using the previous trading day's signal.

### Main Metrics

**Total Return**

The total return of the strategy over the selected period.

**Maximum Drawdown**

The largest decline from a previous portfolio peak.

**Win Rate**

The percentage of profitable trades:

```text
Winning trades / Total trades
```

**Average Trade**

The average return of a completed trade.

**Best Trade**

The most profitable trade.

**Worst Trade**

The least profitable trade.

### Charts

The project creates three charts.

**1. Price Chart**

Shows:

* AAPL price
* SMA 20
* SMA 50
* BUY signals
* SELL signals

**2. Performance Chart**

Compares:

* SMA Strategy
* Buy & Hold

**3. Drawdown Chart**

Compares:

* SMA Strategy Drawdown
* Buy & Hold Drawdown
* Maximum Drawdown for both strategies

### Trade Analysis

A table is created for each completed trade:

```text
Trade
BUY date
BUY price
SELL date
SELL price
Return (%)
```

This makes it possible to analyze each trade individually.

### Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install pandas yfinance matplotlib
```

### Run

```bash
python main.py
```

### Project Structure

```text
sma-backtester/
│
├── main.py
├── README.md
└── .gitignore
```

### Current Results

For the current test period:

```text
SMA Strategy
Total return: 121.58%
Maximum drawdown: -29.09%

Buy & Hold
Total return: 342.36%
Maximum drawdown: -33.36%

Number of trades: 20
Winning trades: 10
Losing trades: 10
Win rate: 50.0%
Average trade: 5.05%
```

Results depend on the selected period and historical data.

### Project Goal

This project was created to practice working with:

* Python
* pandas
* yfinance
* matplotlib
* trading strategies
* backtesting
* return analysis
* risk analysis

This project is intended for educational and research purposes and **is not financial advice**.
