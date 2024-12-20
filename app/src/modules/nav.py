# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of investor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link("pages/00_Investor_Home.py", label="Investor Home", icon='👤')

def StockSearchNav():
    st.sidebar.page_link("pages/01_Stock_Search.py", label="Stock Search", icon='🏦')

def PoliticianSearchNav():
    st.sidebar.page_link("pages/07_Politician_Search.py", label="Politician Search", icon='👨‍⚖️')

def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon='🗺️')

def PortfolioNav():
    st.sidebar.page_link("pages/05_Portfolio.py", label="My Portfolio", icon='🗺️')

## ------------------------ Examples for Role of usaid_worker ------------------------
def editManagerNav():
    st.sidebar.page_link("pages/14_Edit_Manager.py", label="Edit Manager", icon='👤')

def managerHomeNav():
    st.sidebar.page_link("pages/10_Manager_Home.py", label="Manager Home", icon='👤')

def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

def ClassificationNav():
    st.sidebar.page_link("pages/13_Classification.py", label="Classification Demo", icon='🌺')

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Journalist_Home.py", label="Journalist Home", icon='🖥️')
    st.sidebar.page_link("pages/22_Model_Inference.py", label='Inference ML model', icon='🏢')
    st.sidebar.page_link("pages/23_Legislation_Search.py", label='Search Legislation & Politicians', icon='🏢')



# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    # if show_home:
    #     # Show the Home page link (the landing page)
    #     HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'investor':
            PolStratAdvHomeNav()
            StockSearchNav()
            PoliticianSearchNav()
            PortfolioNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'manager':
            # PredictionNav()
            # ApiTestNav() 
            # ClassificationNav()
            managerHomeNav()
            PoliticianSearchNav()
            editManagerNav()
            PortfolioNav()
            
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'journalist':
            AdminPageNav()


    # Always show the About page at the bottom of the list of links
    
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

    if not st.session_state["authenticated"]:
        HomeNav()