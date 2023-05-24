import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

st.title('Stock Market Analysis')
st.write('This is my first app')

ticker = st.text_input('Which stock would you like to look into? Specify the Ticker: eg: AAPL')
stock_data = yf.Ticker(ticker)

col1, col2 = st.columns(2)

with col1:
   st.write('Start Date')
   sd = st.date_input(
    "Plz enter the start date of analysis",
    datetime.date(2019, 1, 1))

with col2:
   st.write('End Date')
   ed = st.date_input(
       "Plz enter the end date of analysis",
       datetime.date(2022, 1, 1))


stock_df = stock_data.history(period="1d",
                              start =f'{sd}',
                              end =f'{ed}')
st.write(f" Viewing info for {ticker}")
st.write(stock_df)

#line chart
col1, col2 = st.columns(2)

with col1:
   st.write('Volume Analysis')
   st.line_chart(stock_df['Volume'])

with col2:
   st.write('Volume Analysis')
   st.line_chart(stock_df['Close'])




