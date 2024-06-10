import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Political Manager, :green[{st.session_state['first_name']}]")
st.write('')
st.write('')
st.write('### What would you like to do today?')




col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Edit Manager Profile', 
             type='primary',
             use_container_width=True):
        st.switch_page('pages/14_Edit_Manager.py')
with col2:
    if st.button('Search Politician Database', 
             type='primary',
             use_container_width=True):
      st.switch_page('pages/07_Politician_Search.py')
with col3:
    if st.button('View My Portfolio', 
             type='primary',
             use_container_width=True):
      st.switch_page('pages/05_Portfolio.py')