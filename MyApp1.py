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

x=df[['interest_rate','unemployment_rate']]
y=df['stock_index_price']
pf=PolynomialFeatures(degree=3)
x_poly=pf.fit_transform(x)

x_train,x_test,y_train,y_test =train_test_split(x_poly,y,random_state=0)

modelRegress=LinearRegression()
modelRegress.fit(x_train,y_train)

#x_input=[[2,5],[2.2,5.7]]
x1=st.number_input("กรุณาป้อนข้อมูล interest_rate:")
x2=st.number_input("กรุณาป้อนข้อมูล unemployment_rate:")

if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1,x2]]
    y_predict=modelRegress.predict(pf.fit_transform(x_input))
    st.write(y_predict)
    st.button("ไม่พยากรณ์")
else:
    st.button("ไม่พยากรณ์")