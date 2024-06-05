import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime as dt
import uuid

def handler():
     logger.info(f'in handler function')


# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()
logger.info('01_Stock_Search page')
search_query = st.text_input('Search for a stock...')



if search_query:
    # logger.info('search query = ', search_query)
    # query = f'http://api:4000/s/stock/{search_query}'
    # logger.info(f'query = {query}')
    results = requests.get(f'http://api:4000/s/{search_query}').json()
    if results:
            
        for stock in results:
            if st.button(stock['company'],
                        type='primary',
                        use_container_width=True):
                logger.info('Wtf Josh?')
                dates = pd.date_range('2023-01-01', periods=100)
                data = np.random.randn(100).cumsum()
                df = pd.DataFrame(data, index=dates, columns=['Value'])
                st.line_chart(df)
                if st.button('Buy Stock',
                        type='secondary',
                        use_container_width=True, on_click=handler):
                        # add stock to tracked table for user
                    
                    unique_id = uuid.uuid4()
                    payload = {
                                'price': stock['curr_price'],
                                'buy': 1,
                                'stock_id': stock['id'],
                                'investor_id': 1, #TODO: change to specific investor users
                                'volume': 1,
                                'date': dt.now().isoformat(),
                                'id': str(unique_id),
                        }
                    logger.info(f'payload = {payload}')
                    url = 'http://api:4000/s/track'
                    
                    response = requests.post(url, json=payload)
    
                    if response.status_code == 200:
                        st.success('Stock successfully tracked!')
                    else:
                        st.error('Failed to track stock. Please try again.')
                        

        # response = requests.get(query)
        # logger.info('response = ', response)
        # results = response.json()
        # logger.info(results)
    else:
        st.write('no stocks found... check spelling')
        
    
else:
    st.write("Trending Stocks:")

    # SQL query to grab 5 most searched stocks ... eventually
    results = requests.get(f'http://api:4000/s/stocks').json()

    for stock in results:
        if st.button(stock['company'],
                     type='primary',
                     use_container_width=True):
            payload = {
                        'price': stock['curr_price'],
                        'buy': 1,
                        'stock_id': stock['id'],
                        'investor_id': 1, #TODO: change to specific investor users
                        'volume': 1,
                        'date': dt.now().isoformat(),
                        'id': 1,
                }
            logger.info(f'payload = {payload}')
            url = 'http://api:4000/s/track'
            
            response = requests.post(url, json=payload)

            logger.info('respose', response)
            if response.status_code == 200:
                st.success('Stock successfully tracked!')
            else:
                st.error('Failed to track stock. Please try again.')
            # dates = pd.date_range('2023-01-01', periods=100)
            # data = np.random.randn(100).cumsum()
            # df = pd.DataFrame(data, index=dates, columns=['Value'])
            # st.line_chart(df)
            if st.button('Buy Stock',
                            type='secondary',
                            use_container_width=True):
                         # add stock to tracked table for user
                        
                        unique_id = uuid.uuid4()
                        payload = {
                                    'price': stock['curr_price'],
                                    'buy': 1,
                                    'stock_id': stock['id'],
                                    'investor_id': 1, #TODO: change to specific investor users
                                    'volume': 1,
                                    'date': dt.datetime(2024, 6, 5, 14, 30),
                                    'id': 1,
                         }
                        
                        url = 'http://api:4000/s/track'
                        
                        response = requests.post(url, json=payload)
        
                        if response.status_code == 200:
                            st.success('Stock successfully tracked!')
                        else:
                            st.error('Failed to track stock. Please try again.')


    # if st.button('Buy Stock',
    #                     type='secondary',
    #                     use_container_width=True):
    #                     # add stock to tracked table for user
                    
    #                 unique_id = uuid.uuid4()
    #                 payload = {
    #                             'price': stock['curr_price'],
    #                             'buy': 1,
    #                             'stock_id': stock['id'],
    #                             'investor_id': 1, #TODO: change to specific investor users
    #                             'volume': 1,
    #                             'date': dt.now().isoformat(),
    #                             'id': str(unique_id),
    #                     }
    #                 logger.info(f'payload = {payload}')
    #                 url = 'http://api:4000/s/track'
                    
    #                 response = requests.post(url, json=payload)
    
    #                 if response.status_code == 200:
    #                     st.success('Stock successfully tracked!')
    #                 else:
    #                     st.error('Failed to track stock. Please try again.')

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
