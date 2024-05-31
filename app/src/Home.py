import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

st.title('Political Profit Bros App')

st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

if st.button("Act as John, an independent stock investor", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'investor'
    st.session_state['first_name'] = 'John'
    st.switch_page('pages/00_Investor_Home.py')

if st.button('Act as Caroline, a political campaign manager', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'manager'
    st.session_state['first_name'] = 'Caroline'
    st.switch_page('pages/10_Manager_Home.py')

if st.button('Act as Bobby, a financial investigative journalist', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'journalist'
    st.session_state['first_name'] = 'Bobby'
    st.switch_page('pages/20_Journalist_Home.py')



