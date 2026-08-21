import pickle
import streamlit as st
import pandas as pd

# Load saved model
with open("catboost_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("DSE Stock Intelligence Dashboard")

# Input
st.write("Enter stock features")

volume = st.number_input("Volume")
return_ = st.number_input("Return")
return_lag1 = st.number_input("Return Lag 1")
return_lag2 = st.number_input("Return Lag 2")
return_lag5 = st.number_input("Return Lag 5")
volatility_5 = st.number_input("Volatility 5")
volatility_20 = st.number_input("Volatility 20")
price_range = st.number_input("Price Range")
volume_sma_20 = st.number_input("Volume SMA 20")
macd_hist = st.number_input("MACD Hist")
atr = st.number_input("ATR")
roc = st.number_input("ROC")


if st.button("Predict"):

    input_data = pd.DataFrame([[
        volume,
        return_,
        return_lag1,
        return_lag2,
        return_lag5,
        volatility_5,
        volatility_20,
        price_range,
        volume_sma_20,
        macd_hist,
        atr,
        roc
    ]], columns=[
        "Volume",
        "Return",
        "Return_Lag1",
        "Return_Lag2",
        "Return_Lag5",
        "Volatility_5",
        "Volatility_20",
        "Price_Range",
        "Volume_SMA_20",
        "MACD_Hist",
        "ATR",
        "ROC"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        signal = "UP 📈"
    elif prediction == -1:
        signal = "DOWN 📉"
    else:
        signal = "NEUTRAL"

    st.success(f"Prediction: {signal}")