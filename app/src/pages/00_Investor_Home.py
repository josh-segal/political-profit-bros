import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Investor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Search Stock Database', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Stock_Search.py')

if st.button('Search Politician Database', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/07_Politician_Search.py')

if st.button('View My Portfolio', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Portfolio.py')