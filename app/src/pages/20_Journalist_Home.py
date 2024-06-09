import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Journalist Home Page')

if st.button('Inference Model', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_Model_Inference.py')

if st.button('Search Legislation Database',
             type='primary',
             use_container_width=True,
            help="Explore the legislation database"):
    st.switch_page('pages/23_Legislation_Search.py')