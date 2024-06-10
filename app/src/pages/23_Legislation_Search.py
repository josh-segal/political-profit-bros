import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from modules.nav import SideBarLinks
import requests
import json

SideBarLinks()

# Sample legislation data
legislation = requests.get(f'http://api:4000/l/legislations').json()
# Sample trades data
trade = requests.get(f'http://api:4000/po/politician_trade').json()

politicians = requests.get(f'http://api:4000/po/politicians_all').json()

id_list = []
for t in trade:
    p_id = t['id']
    id_list.append(p_id)

url = 'http://api:4000/po/legislations'
payload = id_list
pol_data_list = requests.post(url, json=payload)

trade = pd.DataFrame(trade)
# # Layout with columns
col1, col2= st.columns(2)

with col1:
    st.header("Legislations")
    if legislation:
        for i, l in enumerate(legislation):
            with st.expander(l['Title'], expanded=False):
                for key, value in l.items():
                    st.write(f"- **{key}:** {value}")
                if st.button("Find Stocks",
                         help="Find stocks with similar date, party, and subject",
                         key=f"find_stocks_button_{i}"):
                    date = str(l['Date_of_Introduction'])
                    date_str = "Wed, 08 May 2024 00:00:00 GMT"
                    date_obj = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
                    date_only = date_obj.date()
                    trade = requests.get(f'http://api:4000/po/politician_trade_party_date/{date_only}').json()

with col2:
    st.header("Politician Trades")
    st.write("Select a bill to see stocks bought around the same time")
    for i, l in enumerate(trade):
        st.write('- ' + l['Ticker'] + ' - $' + str(l['Trade_Value']) + ' - on ' + str(l['Date_Traded'][:16]))


    
