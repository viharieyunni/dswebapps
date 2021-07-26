import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write(
"""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of the company!
"""
)

# Asking for company as user input
user_input = st.text_input("Company name",
'GOOGL')
tickersymbol = user_input
tickerData = yf.Ticker(tickersymbol)

# Asking for date input from user
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')
tickerDf = tickerData.history(
period = '1d',
start = start_date,
end = end_date
)

st.write(
"""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write(
"""
### Volume
""")
st.line_chart(tickerDf.Volume)
