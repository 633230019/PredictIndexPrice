import pandas as pd
import streamlit as st

st.title("Index Price Prediction")
st.header("Index Price Prediction from NPRU")

df=pd.read_csv("./data/stock_index_price.csv")
st.write(df.head(10))

st.header("Prediction Chart")
st.line_chart(df, x="interest_rate",y=["unemployment_rate","stock_index_price"])