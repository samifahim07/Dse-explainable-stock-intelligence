# 📈 DSE Stock Intelligence & Forecasting

An end-to-end Machine Learning project for analyzing historical stock market data from the **Dhaka Stock Exchange (DSE)**, predicting future market direction, comparing multiple machine learning models, and explaining model predictions using **SHAP and LIME**.

The project also includes a separate **stock price forecasting** component using a regression model.

---

## 📌 Project Overview

Financial markets are highly dynamic and influenced by many factors such as price movement, trading volume, volatility, and technical indicators.

This project aims to investigate whether historical market information and engineered technical features can be used to build machine learning models capable of predicting the next market direction:

- **Down (-1)**
- **Neutral (0)**
- **Up (1)**

The project follows a complete machine learning workflow:

```text
Raw DSE Data
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Data Visualization
      ↓
Feature Engineering
      ↓
Target Creation
      ↓
Time-Series Train/Test Split
      ↓
Feature Selection
      ↓
Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Explainable AI
   ┌──┴──┐
 SHAP  LIME
      ↓
Price Forecasting
