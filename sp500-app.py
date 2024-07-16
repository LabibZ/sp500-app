from datetime import datetime
import streamlit as st
import pandas as pd
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
import yfinance as yf

st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Sector selection
sorted_sector_unique = sorted( df['GICS Sector'].unique() )
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

data = yf.download(
        tickers = list(df_selected_sector[:10].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Plot Closing Price of Query Symbol
def add_moving_averages(df, window):
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df


def candlestick_chart(symbols, start_date, end_date):
    fig = go.Figure()
    for symbol in symbols:
        df = pd.DataFrame(data[symbol])
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        df = df[(df.index >= start_date) & (df.index <= end_date)]
        fig.add_trace(go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     name=symbol))
    fig.update_layout(title='Candlestick Chart', xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=False)
    st.plotly_chart(fig)

def price_plot(symbols, start_date, end_date, show_ma=False, ma_window=20):
    sns.set_style("whitegrid")
    fig, ax1 = plt.subplots(figsize=(12, 8))

    for symbol in symbols:
        df = pd.DataFrame(data[symbol].Close)
        df['Date'] = df.index

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

        if show_ma:
            df = add_moving_averages(df, ma_window)

        ax1.plot(df.Date, df.Close, label=f'{symbol} Close', linewidth=2)
        if show_ma:
            ax1.plot(df.Date, df[f'SMA_{ma_window}'], label=f'{symbol} SMA {ma_window}', linestyle='--')

    ax1.set_title(f'Stock Closing Prices: {", ".join(symbols)}', fontweight='bold', fontsize=14)
    ax1.set_xlabel('Date', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Closing Price (USD)', fontweight='bold', fontsize=12)
    ax1.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax1.legend(loc='upper left')
    sns.despine()
    st.pyplot(fig)

# Streamlit app part
num_company = st.sidebar.slider('Number of Companies', 1, 5)
start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2024-01-01'))
end_date = st.sidebar.date_input('End Date', value=pd.to_datetime(datetime.today()))
show_ma = st.sidebar.checkbox('Show Moving Averages')
ma_window = st.sidebar.slider('Moving Average Window', 5, 50, 20)

symbols_to_plot = list(df_selected_sector.Symbol)[:num_company]

st.header('Stock Closing Prices')
price_plot(symbols_to_plot, start_date, end_date, show_ma, ma_window)

st.header('Candlestick Chart')
candlestick_chart(symbols_to_plot, start_date, end_date)