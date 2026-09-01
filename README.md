# SMA Backtester

Простой backtesting-проект на Python для проверки стратегии пересечения двух скользящих средних (SMA).

Проект использует исторические данные AAPL и сравнивает результат SMA-стратегии с пассивной стратегией Buy & Hold.

## Узнать больше можно тут:
Demo на Youtube: https://www.youtube.com/watch?v=2nBrLU2di_k

## Возможности

* загрузка исторических данных AAPL;
* SMA с настраиваемыми периодами;
* BUY/SELL сигналы при пересечении SMA;
* transaction costs;
* Total Return;
* CAGR;
* Maximum Drawdown;
* Sharpe Ratio;
* Win Rate;
* Average Trade;
* Profit Factor;
* Best/Worst Trade;
* таблица сделок;
* график цены и SMA;
* график стратегии против Buy & Hold;
* график Drawdown.

## Структура проекта

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

## Установка

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его в Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Установить зависимости:

```bash
pip install pandas numpy matplotlib yfinance
```

## Запуск

```bash
python main.py
```

## Настройки стратегии

Периоды SMA и комиссию можно изменить в `main.py`:

```python
fast_window = 20
slow_window = 50
commission = 0.001
```

Например:

```python
fast_window = 10
slow_window = 30
```

## Логика стратегии

BUY:

```text
SMA fast > SMA slow
```

SELL:

```text
SMA fast < SMA slow
```

Стратегия использует сигнал предыдущего дня для расчёта доходности, чтобы избежать look-ahead bias.

## Transaction Costs

Комиссия задаётся в виде десятичной доли.

Например:

```text
0.001 = 0.1%
```

Комиссия применяется при каждом BUY и SELL сигнале.

## Метрики

### Total Return

Общая доходность стратегии за весь период.

### CAGR

Среднегодовая сложная доходность.

### Maximum Drawdown

Максимальное падение капитала от предыдущего максимума.

### Sharpe Ratio

Оценка доходности стратегии с учётом волатильности.

В расчёте используется годовая нормализация через 252 торговых дня.

## Buy & Hold

Результаты стратегии сравниваются с покупкой AAPL в начале периода и удержанием позиции до конца периода.

## Цель проекта

Проект создан как учебный пример разработки простого backtesting framework на Python с разделением кода на:

* получение данных;
* стратегию;
* расчёт метрик;
* отчёт;
* визуализацию;
* запуск приложения.

## Ограничения

Это учебный backtester, а не торговая система.

Он не учитывает:

* slippage;
* bid/ask spread;
* налоги;
* дивиденды отдельно;
* размер позиции;
* управление капиталом;
* market impact.

Результаты исторического backtest не гарантируют будущую доходность.
