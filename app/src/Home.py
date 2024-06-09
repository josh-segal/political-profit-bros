import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

st.title('PublicInterest')

st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

col1, col2, col3 = st.columns(3)

with col1:

        if st.button("**investor**", 
                type = 'primary', 
                use_container_width=True,
                help="Act as John, an independent stock investor"):
                st.session_state['authenticated'] = True
                st.session_state['role'] = 'investor'
                st.session_state['first_name'] = 'John'
                st.switch_page('pages/00_Investor_Home.py')

        col1col1, col1col2, col1col3 = st.columns(3)
        with col1col2:
                st.image("assets/stock.png")

        with st.expander("Explore features"):
                st.write('''
                        As an investor you can:
                        - do this
                        - and that
                        - finally this
                        ''')

with col2:

        if st.button('**campaign manager**', 
                type = 'primary', 
                use_container_width=True,
                help="Act as Caroline, a political campaign manager"):
                st.session_state['authenticated'] = True
                st.session_state['role'] = 'manager'
                st.session_state['first_name'] = 'Caroline'
                st.switch_page('pages/10_Manager_Home.py')


        col1col1, col1col2, col1col3 = st.columns(3)
        with col1col2:
                st.image("assets/manager.png")
        
        with st.expander("Explore features"):
                st.write('''
                        As a campaign manager you can:
                        - do this
                        - and that
                        - finally this
                        ''')

with col3:

        if st.button('**journalist**', 
                type = 'primary', 
                use_container_width=True,
                help="Act as Bobby, a financial investigative journalist"):
                st.session_state['authenticated'] = True
                st.session_state['role'] = 'journalist'
                st.session_state['first_name'] = 'Bobby'
                st.switch_page('pages/20_Journalist_Home.py')

        col1col1, col1col2, col1col3 = st.columns(3)
        with col1col2:
                st.image("assets/journalist.png")

        with st.expander("Explore features"):
                st.write('''
                        As a journalist you can:
                        - do this
                        - and that
                        - finally this
                        ''')



