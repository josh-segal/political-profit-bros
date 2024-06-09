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

    st.write('politician Detail Page')
    politician = st.session_state.payload
    st.write(politician['name'])

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
