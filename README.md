# Predicting Price Moves with News Sentiment

This project focuses on the detailed analysis of financial news data to discover correlations between news sentiment and stock market movements. The analysis aims to provide insights into how headlines shape stock swings, analyzing sentiment scores, running technical indicators, and linking them to daily returns.

## Project Overview

This project is designed to refine skills in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE). It enhances the ability to analyze complex data sets, demonstrate adaptability, and employ innovative thinking skills crucial for the demanding environment at Nova Financial Insights.

## Business Objective

Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency through advanced data analysis. The primary tasks include:

1. **Sentiment Analysis**: Perform sentiment analysis on financial news headlines to quantify tone and sentiment, using NLP techniques to derive sentiment scores associated with stock symbols.

2. **Correlation Analysis**: Establish statistical correlations between news sentiment and corresponding stock price movements, tracking price changes around publication dates and analyzing sentiment impact on performance.

## Dataset Overview

FNSPID (Financial News and Stock Price Integration Dataset) is a comprehensive financial dataset that combines quantitative and qualitative data. The structure includes:

- **headline**: Article release headline, often including key financial actions
- **url**: Direct link to the full news article
- **publisher**: Author/creator of article
- **date**: Publication date and time (UTC-4 timezone)
- **stock**: Stock ticker symbol

## Project Structure

├── .vscode/                # VS Code configuration
│   └── settings.json
├── .github/                # GitHub configuration
│   └── workflows
│       └── unittests.yml
├── .gitignore              # Git ignore file
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── src/                    # Source code
│   └── __init__.py
├── notebooks/              # Jupyter notebooks
│   ├── __init__.py
│   └── README.md
├── tests/                  # Test files
│   └── __init__.py
└── scripts/                # Utility scripts
    ├── __init__.py
    └── README.md

## Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd Financial-News-and-Stock-Price-Integration-Dataset
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/MacOS
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Tasks

### Task 1: Git and GitHub Setup
- Set up Python environment
- Configure Git version control
- Implement CI/CD

### Task 2: Exploratory Data Analysis (EDA)
- Descriptive Statistics
- Text Analysis (Topic Modeling)
- Time Series Analysis
- Publisher Analysis

### Task 3: Quantitative Analysis
- Use finance data with pynance and TA-Lib
- Calculate technical indicators (MA, RSI, MACD)
- Visualize data and indicators

### Task 4: Sentiment Analysis
- Apply NLP techniques to news headlines
- Correlate sentiment with stock movements

## Contributing

Please commit your work at least three times a day with descriptive commit messages.

## License

[Include appropriate license information]