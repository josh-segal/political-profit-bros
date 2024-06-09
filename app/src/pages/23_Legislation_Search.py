import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from modules.nav import SideBarLinks

SideBarLinks()

# Sample legislation data
legislation_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='M'),
    'Politician': ['John Doe', 'Jane Smith', 'John Doe', 'Jane Smith', 'Alex Johnson', 'Chris Lee', 'Alex Johnson', 'Chris Lee', 'Pat Brown', 'Pat Brown'],
    'Party': ['Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B'],
    'Title': ['Legislation 1', 'Legislation 2', 'Legislation 3', 'Legislation 4', 'Legislation 5', 'Legislation 6', 'Legislation 7', 'Legislation 8', 'Legislation 9', 'Legislation 10']
})

# Sample trades data
trades_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-15', periods=10, freq='M'),
    'Politician': ['John Doe', 'Jane Smith', 'John Doe', 'Jane Smith', 'Alex Johnson', 'Chris Lee', 'Alex Johnson', 'Chris Lee', 'Pat Brown', 'Pat Brown'],
    'Party': ['Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B', 'Party A', 'Party B'],
    'Asset_Type': ['Stock', 'Bond', 'Stock', 'Stock', 'Bond', 'Stock', 'Bond', 'Stock', 'Stock', 'Bond'],
    'Trade_Size': np.random.randint(100, 1000, size=10),
    'Trade_Value': np.random.randint(1000, 10000, size=10),
    'Issuer': ['Company A', 'Company B', 'Company A', 'Company B', 'Company A', 'Company B', 'Company A', 'Company B', 'Company A', 'Company B']
})

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.header("Legislation")
    # Filters for legislation
    date_range_legislation = st.date_input("Date Range", [], key='legislation_date_range')
    selected_politicians_legislation = st.multiselect("Select Politicians", legislation_data['Politician'].unique(), key='legislation_politicians')
    selected_parties_legislation = st.multiselect("Select Parties", legislation_data['Party'].unique(), key='legislation_parties')
    
    if date_range_legislation:
        start_date_legislation = pd.to_datetime(date_range_legislation[0])
        end_date_legislation = pd.to_datetime(date_range_legislation[1])
        filtered_legislation = legislation_data[
            (legislation_data['Date'] >= start_date_legislation) &
            (legislation_data['Date'] <= end_date_legislation) &
            (legislation_data['Politician'].isin(selected_politicians_legislation)) &
            (legislation_data['Party'].isin(selected_parties_legislation))
        ]
    else:
        filtered_legislation = legislation_data.copy()
    
    st.dataframe(filtered_legislation)

with col2:
    st.header("Stock Trades")
    # Filters for stock trades
    date_range_trades = st.date_input("Date Range", [], key='trades_date_range')
    selected_politicians_trades = st.multiselect("Select Politicians", trades_data['Politician'].unique(), key='trades_politicians')
    selected_parties_trades = st.multiselect("Select Parties", trades_data['Party'].unique(), key='trades_parties')
    
    if date_range_trades:
        start_date_trades = pd.to_datetime(date_range_trades[0])
        end_date_trades = pd.to_datetime(date_range_trades[1])
        filtered_trades = trades_data[
            (trades_data['Date'] >= start_date_trades) &
            (trades_data['Date'] <= end_date_trades) &
            (trades_data['Politician'].isin(selected_politicians_trades)) &
            (trades_data['Party'].isin(selected_parties_trades))
        ]
    else:
        filtered_trades = trades_data.copy()
    
    st.dataframe(filtered_trades)

# Highlight correlations
st.header("Correlation Highlights")
correlated_data = filtered_legislation.merge(filtered_trades, on='Politician')
st.dataframe(correlated_data)
