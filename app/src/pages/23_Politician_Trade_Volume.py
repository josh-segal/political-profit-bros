import streamlit as st
from modules.nav import SideBarLinks
import requests
import plotly as px
import pandas as pd

st.set_page_config(layout = 'wide')

SideBarLinks()


response = requests.get(f'http://api:4000/po/distinct_politicians')
results = response.json()
politician_names = [item['Name'] for item in results]

option = st.selectbox('Select a politician name:', politician_names)
st.write(f"You selected: {option}")

if st.button('View Trade Volume Information', type='primary', use_container_width=True):
    response = requests.get(f'http://api:4000/po/volume_politicians/{option}').json()
    df = pd.DataFrame(response)
    
    # Display the DataFrame
    st.dataframe(df, column_order=["Name", "Party", "Date_Traded", "Total_Trade_Value"])
    
    # Define the color map
    color_map = {
        'Democrat': 'blue',
        'Republican': 'red',
        'Other': 'black'
    }

    # Add a color column to the DataFrame based on the Party
    df['color'] = df['Party'].map(color_map)

    # Converting trade value into integers and Date into Datetime object
    df['Total_Trade_Value'] = df['Total_Trade_Value'].astype(int)
    df['Date_Traded'] = pd.to_datetime(df['Date_Traded'])

    
    # Create the line plot
    st.line_chart(df, x='Date_Traded', y='Total_Trade_Value', color='Party')





