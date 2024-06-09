import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Portfolio')

# You can access the session state to make a more customized/personalized app experience

if st.session_state['role'] == 'investor':

    # stock_pol = st.toggle("Politician / Stock Portfolio", value=True)
    tab1, tab2 = st.tabs(["Stock Portfolio", "Politician Portfolio"])

    with tab1:

        results = requests.get(f'http://api:4000/i/stock_portfolio/{1}').json()
        if results:
            for stock in results:
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(stock['company'],
                                type='primary',
                                use_container_width=True,
                                key=f"{stock['id']}_name"):
                        st.session_state.payload = stock
                        st.switch_page('pages/08_Stock_Detail.py')  

                with col2:
                    if st.button(":x:",
                                type='secondary',
                                use_container_width=False,
                                key=f"{stock['id']}_untrack",
                                help="untrack stock"):
                        stock_id = stock['id']
                        user_id = 1

                        payload = {
                                'stock_id': stock_id,
                                'user_id': user_id
                                }
                        
                        url = 'http://api:4000/i/delete_tracked_stock'
                        response = requests.delete(url, json=payload)
                        st.rerun()

        else:
            st.write('no stocks found... check spelling')
    with tab2:

        results = requests.get(f'http://api:4000/po/politician_portfolio/{1}').json()
        if results:
            for politician in results:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(politician['name'],
                                type='primary',
                                use_container_width=True,
                                key=f"{politician['id']}_name"):
                        st.session_state.payload = politician
                        st.switch_page('pages/09_Politician_Detail.py')  

                with col2:
                    if st.button(":x:",
                                type='secondary',
                                use_container_width=False,
                                help="untrack politician",
                                key=f"{politician['id']}_untrack"):
                        politician_id = politician['id']
                        user_id = 1

                        payload = {
                                'politician_id': politician_id,
                                'user_id': user_id
                                }
                        
                        url = 'http://api:4000/i/delete_tracked_politician'
                        response = requests.delete(url, json=payload)  
                        st.rerun()     
        else:
            st.write('no politician found... check spelling')

elif st.session_state['role'] == 'manager':


    results = requests.get(f'http://api:4000/m/politician_portfolio/{3}').json()

    col1, col2 = st.columns(2)

    response_container = st.empty()

    with col1:
         st.write("Candidate Politicians")
    with col2:
         st.write("Opponent Politicians")

    if results:
         for politician in results:
            if politician['candidate_opp'] == 1:
                with col1:
                    innerCol1, innerCol2 = st.columns([2, 1])
                    with innerCol1:
                        if st.button(politician['name'], type='primary', use_container_width=True, key=f"{politician['id']}_name"):
                            st.session_state.payload = politician
                            st.switch_page('pages/09_Politician_Detail.py')
                    with innerCol2:
                        if st.button(":x:", type='secondary', use_container_width=True, key=f"{politician['id']}_untrack"):
                            response_container.text(f"Untracking {politician['name']}...")
                            politician_id = politician['id']
                            user_id = 3
                            candidate_opp = politician['candidate_opp']
                            payload = {
                                'politician_id': politician_id,
                                'user_id': user_id,
                                'candidate_opp': candidate_opp
                            }
                            url = 'http://api:4000/m/delete_tracked_politician'
                            response = requests.delete(url, json=payload)
                            if response.status_code == 200:
                                response_container.text(f"Successfully untracked {politician['name']}.")
                                st.rerun()
                            else:
                                response_container.text(f"Failed to untrack {politician['name']}.")
            else:
                with col2:
                    innerCol1Bad, innerCol2Bad = st.columns([2, 1])
                    with innerCol1Bad:
                        if st.button(politician['name'], type='primary', use_container_width=True, key=f"{politician['id']}_name"):
                            st.session_state.payload = politician
                            st.switch_page('pages/09_Politician_Detail.py')
                    with innerCol2Bad:
                        if st.button(":x:", type='secondary', use_container_width=True, key=f"{politician['id']}_untrack"):
                            response_container.text(f"Untracking {politician['name']}...")
                            politician_id = politician['id']
                            user_id = 3
                            candidate_opp = politician['candidate_opp']
                            payload = {
                                'politician_id': politician_id,
                                'user_id': user_id,
                                'candidate_opp': candidate_opp
                            }
                            url = 'http://api:4000/m/delete_tracked_politician'
                            response = requests.delete(url, json=payload)
                            if response.status_code == 200:
                                response_container.text(f"Successfully untracked {politician['name']}.")
                                st.rerun()
                            else:
                                response_container.text(f"Failed to untrack {politician['name']}.")