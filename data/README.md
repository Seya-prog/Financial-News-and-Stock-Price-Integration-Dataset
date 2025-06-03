# Data Directory

This directory contains the data files for the Financial News and Stock Price Integration Dataset (FNSPID).

## Structure

- `raw/`: Original, unmodified data files
  - Financial news data
  - Stock price historical data

- `processed/`: Cleaned and preprocessed data
  - Processed news data with sentiment scores
  - Stock price data with technical indicators
  - Merged datasets for analysis

- `interim/`: Intermediate data that has been transformed but is not yet ready for analysis
  - Partially processed datasets
  - Temporary results

- `external/`: External data from third-party sources
  - Market index data
  - Economic indicators
  - Additional reference data

## Data Files

The main dataset (FNSPID) includes:
- News headlines
- URLs to articles
- Publisher information
- Publication dates
- Associated stock tickers

## Notes

- Large data files are not tracked in Git (see .gitignore)
- Data preprocessing steps are documented in the notebooks directory
- For accessing raw data files, use the data download script in the scripts directory
