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

search_query = st.text_input('Search for a stock...')

if search_query:

    if st.button('Stock 1', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)


else:
    st.write("Trending Stocks:")

    # SQL query to grab 5 most searched stocks
    
    if st.button('Stock 1', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)

    if st.button('Stock 2', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)

    if st.button('Stock 3', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)

    if st.button('Stock 4', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)

    if st.button('Stock 5', 
        type='primary',
        use_container_width=True):
        # results = requests.get(f'http://api:4000/stock/{search_query}').json()
        # results should be dataframe
        dates = pd.date_range('2023-01-01', periods=100)
        data = np.random.randn(100).cumsum()
        df = pd.DataFrame(data, index=dates, columns=['Value'])
        st.line_chart(df)









# set the header of the page
# st.header('World Bank Data')

# # You can access the session state to make a more customized/personalized app experience
# st.write(f"### Hi, {st.session_state['first_name']}.")

# # get the countries from the world bank data
# with st.echo(code_location='above'):
#     countries:pd.DataFrame = wb.get_countries()
   
#     st.dataframe(countries)

# # the with statment shows the code for this block above it 
# with st.echo(code_location='above'):
#     arr = np.random.normal(1, 1, size=100)
#     test_plot, ax = plt.subplots()
#     ax.hist(arr, bins=20)

#     st.pyplot(test_plot)


# with st.echo(code_location='above'):
#     slim_countries = countries[countries['incomeLevel'] != 'Aggregates']
#     data_crosstab = pd.crosstab(slim_countries['region'], 
#                                 slim_countries['incomeLevel'],  
#                                 margins = False) 
#     st.table(data_crosstab)
