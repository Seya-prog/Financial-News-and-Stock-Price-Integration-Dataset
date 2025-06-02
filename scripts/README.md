# Scripts

This directory contains utility scripts for data processing, model training, and automation of repetitive tasks in the project workflow.

## Available Scripts

- `data_downloader.py`: Downloads financial news and stock price data
  - Fetches historical stock data using yfinance
  - Can be configured to get data for specific date ranges and tickers

- `sentiment_analyzer.py`: Command-line tool for batch sentiment analysis
  - Processes news headlines from CSV files
  - Outputs sentiment scores using VADER and/or TextBlob
  - Saves results to CSV format

- `technical_indicators.py`: Calculates and saves technical indicators
  - Computes common indicators like MA, RSI, MACD using TA-Lib
  - Takes input from CSV files and outputs processed data

## Usage

All scripts can be run from the command line. For example:

```bash
# To download data
python scripts/data_downloader.py --start-date 2020-01-01 --end-date 2020-12-31 --tickers AAPL,MSFT,GOOG

# To analyze sentiment
python scripts/sentiment_analyzer.py --input data/raw/news_headlines.csv --output data/processed/sentiment_scores.csv

# To calculate technical indicators
python scripts/technical_indicators.py --input data/raw/price_data.csv --output data/processed/indicators.csv
```

## Development

When adding new scripts to this directory:

1. Follow the existing naming conventions
2. Include comprehensive docstrings and comments
3. Add command-line argument parsing for flexibility
4. Include error handling and logging
5. Update this README with documentation for the new script