# Stock-Price-Prediction-based-on-Reddit-Sentiment
---

## **Project Overview**

This project aims to predict stock movements, specifically for Apple Inc. (AAPL), using sentiment analysis on Reddit posts related to stock discussions. The core objective is to analyze and predict stock price movements by scraping Reddit data and extracting sentiments. This involves collecting data from Reddit, performing sentiment analysis, and training a machine learning model to make predictions.

## **Objectives**
- Predict stock price movements for Apple (AAPL) using sentiment extracted from Reddit posts.
- Analyze how sentiment scores and economic indicators (e.g., GDP, CPI, Interest Rate) impact stock price predictions.
- Evaluate multiple machine learning models and find the most accurate model for stock prediction.

---

## **Tech Stack**

- **Python Libraries:**
  - `pandas`: Data manipulation
  - `numpy`: Numerical operations
  - `matplotlib`, `seaborn`, `plotly`: Data visualization
  - `sklearn`: Machine learning models and evaluation
  - `praw`: Reddit API for scraping data
  - `yfinance`: Fetching stock data (AAPL)
  - `fredapi`: Accessing economic indicators
  - `transformers`: Hugging Face for sentiment analysis
  - `requests`: HTTP requests
  - `IPython`: For displaying images in Jupyter Notebooks

- **Machine Learning Algorithms:**
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Support Vector Regression (SVR)
  - Random Forest Regressor
  - Decision Tree Regressor
  - Gradient Boosting Regressor

---

## **Getting Started**

### **Install Required Libraries**

You can install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

## **Data Collection**

### **Reddit Scraping:**
- Data is scraped using **PRAW** (Python Reddit API Wrapper) from stock-related subreddits such as:
  - `r/stocks`
  - `r/investing`
  - `r/Wallstreetbets`

- The data includes:
  - Title of the post
  - Post score
  - Number of comments
  - Date of creation
  - Subreddit

The data is collected from **January 2022 to November 2024**.

### **Stock Data:**
- Stock data for Apple Inc. (AAPL) is fetched from Yahoo Finance using **yfinance**.
- Data includes:
  - `Open`, `Close`, `High`, `Low` prices
  - Volume of stocks traded

### **Economic Data:**
- Economic indicators like **GDP**, **CPI**, and **Interest Rate** are fetched from **FRED (Federal Reserve Economic Data)** using the `fredapi` library.

---

## **Data Collection**

### **Reddit Scraping (PRAW)**

To collect Reddit posts related to stock movements, we use the **PRAW (Python Reddit API Wrapper)**. The process to scrape Reddit involves:

- **Setting up Reddit API Access:**
  - Create a Reddit application via [Reddit's Developer Portal](https://www.reddit.com/prefs/apps) to obtain a `client_id`, `client_secret`, and `user_agent`.
  
- **Fetching Reddit Posts:**
  - Posts from subreddits like **r/stocks**, **r/investing**, and **r/Apple** are fetched. Posts are filtered by popularity (top posts) and are related to discussions about stocks.
  
- **Data Collected:**
  - **Fields Collected**: Post title, score, number of comments, post date, and subreddit name.
  - **Time Range**: Data is collected from **January 2022 to November 2024**.

---

### **Stock Data (Yahoo Finance - yfinance)**

- Stock data for **Apple Inc. (AAPL)** is fetched using the **yfinance** library.
- The data collection covers the stock prices, including **daily open, close, high, low**, and **volume**, from **January 2022 to November 2024**.

---

### **Economic Data (FRED API)**

- Economic indicators such as **GDP**, **CPI**, and **Interest Rates** are fetched using the **FRED API** (Federal Reserve Economic Data).
- This data is useful for analyzing the impact of macroeconomic factors on stock price predictions.

---

## **Data Processing**

1. **Sentiment Analysis:**
   - Sentiment is extracted from Reddit posts using the **Hugging Face transformer model**.
   - Sentiment labels are assigned: `positive`, `neutral`, and `negative`.
   - Sentiment score is calculated, and it’s used to determine stock price movements.

2. **Feature Engineering:**
   - Extracted features include sentiment scores, technical indicators (e.g., `RSI`, `Close_lag2`), and macroeconomic indicators.
   - Features such as **lagged stock prices** and **economic factors** are added to enhance the model.

---

## **Machine Learning Models**

Several machine learning models are tested to predict stock movements:
- **Linear Regression**
- **Ridge and Lasso Regression** (with regularization)
- **Support Vector Regression (SVR)**
- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Gradient Boosting Regressor**

Model performance is evaluated using metrics such as:
- **MAE (Mean Absolute Error)**
- **MAPE (Mean Absolute Percentage Error)**
- **R² Score**

---



## **Acknowledgments**

- **Reddit API (PRAW)**: For providing access to Reddit posts and comments.
- **Yahoo Finance (yfinance)**: For stock data.
- **FRED (Federal Reserve Economic Data)**: For economic indicators.
- **Hugging Face Transformers**: For the sentiment analysis model.

---
