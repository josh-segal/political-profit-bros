import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
from modules.nav import SideBarLinks
import requests

SideBarLinks()

new_name = st.text_input("Change name...")

party = st.toggle("Choose party...")

if party:
    st.write("Democrat")
else:
    st.write("Republican")

if st.button('Update',
             type='primary',
             use_container_width=True):
    if party:
        party = 'Democrat'
    else:
        party = 'Republican'
    payload = {
        'name': new_name,
        'party': party
        }

    url = 'http://api:4000/m/update'

    response = requests.put(url, json=payload)
    