# Borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st


def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def Page1Nav():
    st.sidebar.page_link("pages/01_World_Bank_Viz.py", label="World Bank Visualization")

def Page2Nav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration")

def Page3Nav():
    st.sidebar.page_link("pages/05_API_Test.py", label="Test the API")

def SideBarLinks(user_roles=None):
    
    st.sidebar.image("assets/logo.png", width = 150)

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')

    # Always show the home and login navigators.
    HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # (1) Only the admin role can access page 1 and other pages.
        # In a user roles get all the usernames with admin role.
        # admins = [k for k, v in user_roles.items() if v == 'admin']

        # Show page 1 if the username that logged in is an admin.
        if st.session_state['role'] == 'pol_strat_advisor':
            Page1Nav()
            Page2Nav()

        # (2) users with user and admin roles have access to page 2.
        Page3Nav() 

        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')