# Notebooks

This directory contains Jupyter notebooks for exploratory data analysis, visualization, and model development.

## Structure

- `eda.ipynb`: Exploratory Data Analysis of the financial news dataset
  - Descriptive statistics
  - Text analysis and topic modeling
  - Time series analysis
  - Publisher analysis

- `technical_indicators.ipynb`: Technical indicator analysis using TA-Lib and PyNance
  - Moving averages (SMA, EMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
  - Visualization of indicators

- `sentiment_analysis.ipynb`: News headline sentiment analysis
  - NLP preprocessing
  - Sentiment scoring with VADER and TextBlob
  - Correlation with stock price movements

## Usage

To run these notebooks:

1. Ensure you have activated the virtual environment:
   ```
   # Windows
   .venv\Scripts\activate
   ```

2. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

3. Navigate to the notebook you wish to run and open it.

## Notes

- Data preprocessing code in these notebooks should be refactored into the `src` directory for production use.
- Maintain clear documentation within notebooks using markdown cells.
- Include visualization outputs in the notebooks for easier sharing of insights.