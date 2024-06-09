DROP DATABASE IF EXISTS JoshProject;
CREATE DATABASE IF NOT EXISTS JoshProject;

USE JoshProject;

CREATE TABLE IF NOT EXISTS poly_trade_data (
    txId VARCHAR(255),
    Name VARCHAR(255),
    id VARCHAR(255),
    Party VARCHAR(255),
    Chamber VARCHAR(255),
    State VARCHAR(255),
    Asset_Type VARCHAR(255),
    Issuer VARCHAR(255),
    Ticker VARCHAR(255),
    Issuer_Country VARCHAR(255),
    Type VARCHAR(255),
    Date_Traded DATE,
    Date_Published DATE,
    Trade_Size FLOAT,
    Trade_Price FLOAT,
    Trade_Value INT
);

