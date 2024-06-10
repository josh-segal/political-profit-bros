import streamlit as st
from modules.nav import SideBarLinks
import requests
import plotly as px
import pandas as pd
from datetime import datetime

st.set_page_config(layout = 'wide')

SideBarLinks()

def convert_date(date_string):
    # convert string to date object
    date_object = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z').date()
    return date_object


response = requests.get(f'http://api:4000/po/distinct_politicians')
results = response.json()
politician_names = [item['Name'] for item in results]

name = st.selectbox('Select a politician name:', politician_names)
st.write(f"You selected: {name}")

if st.button('View Trade Volume Information', type='primary', use_container_width=True):
    response = requests.get(f'http://api:4000/po/volume_politicians/{name}').json()
    df = pd.DataFrame(response)
    # Display the DataFrame
    st.dataframe(df, column_order=["Name", "Party", "Date_Traded", "Total_Trade_Value"])

    prediction_response = requests.get(f'http://api:4000/po/predict_volume/{name}').json()
    #st.write(prediction_response)
    
    # Define the color map
    color_map = {
        'Democrat': 'blue',
        'Republican': 'red',
        'Other': 'black'
    }
    # Converting trade value into integers and Date into Datetime object
    df['Total_Trade_Value'] = df['Total_Trade_Value'].astype(int)
    df['Date_Traded'] = df['Date_Traded'].apply(lambda x: convert_date(x))
    df = df.sort_values(by='Date_Traded')
    df['ypreds'] = prediction_response['result']['ypreds']
    
    # Create the line plot
    st.line_chart(df, x='Date_Traded', y=['Total_Trade_Value','ypreds'], color=["#0000FF","#FF0000"], title='HI')
    st.write(f"Linear Regression Equation: {prediction_response['result']['equation']}")
   
   

