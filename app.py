import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Analysis')

if st.checkbox("Show only cars under $20,000"):
    df = df[df['price'] < 20000]
st.write(px.histogram(df, x='model', y='price', nbins= 20))
st.write(px.scatter(df, x='model', y='price'))
st.write(px.scatter(df, x='model', y='price', title='Price vs. Model', log_y=True))
