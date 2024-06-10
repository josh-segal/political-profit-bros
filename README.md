# Summer 2024 DoC Prof's Project

## About

This project explores some different features of Streamlit & Flask to build a more comprehensive app. 

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database` directory)

## Getting Started
1. Clone the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. Start the docker containers. 

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


## Deploying An ML Model

*Note*: This project only contains the infrastructure for a hypothetical ML model. 

1. Convert your Jupyter Notebook code for an ML model to a purely python script.  You can include the `training` and `testing` functionality as well as the `prediction` functionality.  You don't need to include data cleaning, though. 
1. In `api/backend`, notice the addition of `ml_models` module.  In this folder, I've put a sample (read *fake*) ML model in `model01.py`.  The `predict` function will be called by the Flask REST API to perform real-time prediction based upon model parameter values that are stored in the database.  **Important**: you cannot hard code the model parameter weights directly in the prediction function.  tl;dr - take some time to look over the code in `model01.py`.  
1. The prediction route for the REST API is in `backend/customers/customer_routes.py`. Basically, it accepts two URL parameters and passes them to the `prediction` function in the `models` module. The `prediction` function packages up the value(s) it receives from the model's `predict` function and send its back to Streamlit as JSON. 
1. Back in streamlit, check out `pages/11_Prediction.py`.  What I do on this page is create two numeric input fields.  When the button is pressed, it makes a request to the REST API `/c/prediction/.../...` function and passes the values from the two inputs as URL parameters.  It gets back the results from the route and displays them. Nothing fancy here. 


## README

Overview

Welcome to our cutting-edge website, designed to revolutionize the way you approach stock investments and political transparency. Our platform offers powerful tools to track stock performance, predict market trends, and gain insights into the trading activities of politicians. By leveraging this information, you can make more informed investment decisions and contribute to a more transparent and accountable political environment.

Key Features

1. Stock Tracking and Prediction
Real-Time Data: Stay updated with the latest stock market trends through real-time tracking.
Predictive Analytics: Utilize advanced algorithms to forecast stock movements, helping you to make data-driven investment decisions.

2. Politician Trades Monitoring
Transparency: Access detailed records of buying and selling activities by politicians.
Strategic Insights: Gain valuable insights by analyzing the trades of politicians, who often have access to insider information.

3. Personalized Portfolio Management
Custom Tracking: Add your preferred stocks and politicians to your personal portfolio for tailored updates.
Personalized Dashboard: Get a customized view of your tracked assets and receive relevant notifications.

4. Comprehensive Stock Database
Extensive Database: Our platform utilizes a robust database of stocks, ensuring comprehensive coverage and up-to-date information.
CS3200 Integration: The database and routes for the features and machine learning models were meticulously created by CS3200, providing a seamless and efficient experience.
Data Management: Efficiently manage and retrieve stock data through well-structured routes, enabling smooth functionality for all features.

5. Advanced Machine Learning Models
Linear Regression Model: Developed by DS3000 students, this model uses three years of politicians' trading data to predict stock movements based on their trading values.
LSTM Model: Another innovation by DS3000 students, this Long Short-Term Memory (LSTM) model predicts stock prices based solely on historical price and date data, leveraging deep learning for more accurate predictions.

## Benefits

Informed Investment Decisions
Our platform empowers you with predictive analytics and real-time data, enabling you to anticipate market movements and make informed investment choices.

Enhanced Transparency
By monitoring the financial activities of politicians, you gain insight into potential future regulations and market shifts, promoting a more transparent political system.