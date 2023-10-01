import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

st.title("Index Price Prediction")
st.header("Index Price Prediction from NPRU")

df=pd.read_csv("./data/stock_index_price.csv")
st.write(df.head(10))

st.header("Prediction Chart")
st.line_chart(df, x="interest_rate",y=["unemployment_rate","stock_index_price"])