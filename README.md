# Summer 2024 DoC Prof's Project

## About

This project explores some different features of Streamlit & Flask to build a more comprehensive app. 

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database` directory)

## Handling User Role Access and Control

In most applications, when a user logs in, they assume a particular role.  For instance, when one logs in to a stock price prediction app, they may be a single investor, a portfolio manager, or a corporate executive (of a publicly traded company).  Each of those *roles* will likely present some similar features as well as some different features when compared to the other roles. So, how do you accomplish this in Streamlit?  This is sometimes called Role-based Access Control, or RBAC for short. 

The code in this project demonstrates how to implement a simple RBAC system in Streamlit but without actually using user authentication (usernames and passwords).  The Streamlit pages from the original template repo and split up among 2 roles - Political Strategist and USAID Worker, and a System Administrator role is used for any sort of system tasks such as re-training the ML model, etc. It also demonstrates how to deploy an ML model. 

Wrapping your head around this will take a little time and exploration of this code base.  Some highlights are below. 

### Getting Started with the RBAC 
1. We need to turn off the standard panel of links on the left side of the Streamlit app. This is done through the `.streamlit/config.toml` file.  So check that out. We are turning it off so we can control directly what links are shown. 
1. Then I created a new python module in `modules/nav.py`.  When you look at the file, you will se that there are functions for basically each page of the application. The `st.sidebar.page_link(...)` adds a single link to the sidebar. We have a separate function for each page so that we can organize the links/pages by role. 
1. Next, check out the `Home.py` file. Notice that there are 3 buttons added to the page and when one is clicked, it redirects via `st.switch_page(...)` to that Roles Home page in `./pages`.  But before the redirect, I set a few different variables in the Streamlit `session_state` object to track role, first name of the user, and that the user is now authenticated.  
1. Notice near the top of `Home.py` and all other pages, there is a call to `SideBarLinks(...)` from the `nav` module.  This is the function that will use the role set in session_state to determine what links to show the user in the sidebar. 
1. I reorganized the pages by Role.  Pages that start with a `0` are related to the *Political Strategist* role.  Pages that start with a `1` are related to the *USAID worker* role.  And, pages that start with a `2` are related to The *System Administrator* role. 




 