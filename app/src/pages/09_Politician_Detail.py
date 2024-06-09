import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime as dt

SideBarLinks()

if st.session_state['role'] == 'investor':


    politician = st.session_state.payload
    st.write(politician['name'])
    politician_name = politician['name']

    if st.button('Track politician',
                            type='primary',
                            use_container_width=True):

        payload = {
                'investor_id': 1, # TODO: figure out how to do this with 3 users
                        'politician_id': politician['id'],
                        'date': dt.now().isoformat(),
        }


        url = 'http://api:4000/po/track'

        response = requests.post(url, json=payload)

        logger.info('respose', response)
        if response.status_code == 200:
            st.success('politician successfully tracked!')
        else:
            st.error('Failed to track politician. Please try again.')

    elif st.button(f"What Securities Does {politician_name} hold?",
                    type='primary',
                    use_container_width=True):
        try:
            politician_response = requests.get(f'http://api:4000/po/politician_stock_details/{politician_name}')
            logger.info(f'politician_response: {politician_response}')
            politician_results = politician_response.json()
            if len(politician_results) > 0:
                politician_results_df = pd.DataFrame(politician_results)

                # Group by columns and sum the Trade_Value
                grouped_df = politician_results_df.groupby(["Name", "Party", "State", "Ticker"], as_index=False)["Trade_Value"].sum()
                
                # Display the grouped dataframe
                st.dataframe(grouped_df.sort_values(by='Trade_Value', ascending=False).reset_index(), column_order=["Name", "Party", "State", "Ticker", "Trade_Value"])
            #    column_order=["Name", "Politician_id", "Party", "Chamber", "State", "Asset_Type", \
            #  "Issuer", "Ticker", "Issuer_Country", "Type", "txId", "Date_Traded", "Date_Published", "Trade_Size",\
            #      "Trade_Price", "Trade_Value"])
            else:
                st.write(f"{politician_name} holds no Securities.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")


elif st.session_state['role'] == 'manager':

    st.write('politician Detail Page')
    politician = st.session_state.payload
    st.write(politician['name'])

    if st.button('Track candidate politician',
                            type='primary',
                            use_container_width=True):

        payload = {
                'manager_id': 3, # TODO: figure out how to do this with 3 users
                        'politician_id': politician['id'],
                        'date': dt.now().isoformat(),
                        'candidate_opp': 1,
        }

        url = 'http://api:4000/m/track'

        response = requests.post(url, json=payload)

        logger.info('respose', response)
        if response.status_code == 200:
            st.success('politician successfully tracked!')
        else:
            st.error('Failed to track politician. Please try again.')

    if st.button('Track opponent politician',
                            type='primary',
                            use_container_width=True):

        payload = {
                'manager_id': 3, # TODO: figure out how to do this with 3 users
                        'politician_id': politician['id'],
                        'date': dt.now().isoformat(),
                        'candidate_opp': 0,
        }

        url = 'http://api:4000/m/track'

        response = requests.post(url, json=payload)

        logger.info('respose', response)
        if response.status_code == 200:
            st.success('politician successfully tracked!')
        else:
            st.error('Failed to track politician. Please try again.')
