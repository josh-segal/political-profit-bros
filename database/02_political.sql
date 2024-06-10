-- DROP DATABASE IF EXISTS JoshProject;
-- CREATE DATABASE IF NOT EXISTS JoshProject;
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
CREATE TABLE IF NOT EXISTS investor
(
    name VARCHAR(50) NOT NULL,
    created_at DATETIME,
    amount_invested FLOAT,
    id INT,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS journalist
(
    name VARCHAR(50) NOT NULL,
    created_at DATETIME,
    expert_industry VARCHAR(80),
    company VARCHAR(80),
    state VARCHAR(50),
    party VARCHAR(50),
    id INT,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS manager
(
    name VARCHAR(50) NOT NULL,
    created_at DATETIME,
    party VARCHAR(50),
    id INT,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS politician_list
(
    name VARCHAR(50) NOT NULL,
    party VARCHAR(50),
    state VARCHAR(50),
    manager_id INT,
    id VARCHAR(80),
    PRIMARY KEY (id),
    FOREIGN KEY (manager_id) REFERENCES manager (id)
);
-- CREATE TABLE IF NOT EXISTS poly_trade_data (
--     txId VARCHAR(255),
--     Name VARCHAR(255),
--     id VARCHAR(255),
--     Party VARCHAR(255),
--     Chamber VARCHAR(255),
--     State VARCHAR(255),
--     Asset_Type VARCHAR(255),
--     Issuer VARCHAR(255),
--     Ticker VARCHAR(255),
--     Issuer_Country VARCHAR(255),
--     Type VARCHAR(255),
--     Date_Traded DATE,
--     Date_Published DATE,
--     Trade_Size FLOAT,
--     Trade_Price FLOAT,
--     Trade_Value INT
-- );
CREATE TABLE politician AS SELECT distinct id, Name, Party, Chamber, State from poly_trade_data;
CREATE TABLE politician_trade AS SELECT txId,
    id, Asset_Type, Issuer, Ticker, Issuer_Country, Type,
    Date_Traded, Date_Published, Trade_Size, Trade_Price,
    Trade_Value from poly_trade_data;
ALTER TABLE politician ADD PRIMARY KEY (id);
ALTER TABLE politician_trade ADD PRIMARY KEY (txId);
ALTER TABLE politician_trade ADD FOREIGN KEY (id) REFERENCES politician (id);
CREATE TABLE IF NOT EXISTS legislation
(
    title VARCHAR(80),
    date DATETIME,
    pass TINYINT(1),
    active TINYINT(1),
    sector VARCHAR(80),
    id INT,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS stocks
(
    Date DATETIME,
    Open float,
    High float,
    Low float,
    Close FLOAT,
    Adj_Close float,
    Volume int,
    ticker VARCHAR(10),
    company Varchar(255),
    PRIMARY KEY (ticker, Date)
);
CREATE TABLE IF NOT EXISTS politician_order
(
    price FLOAT,
    buy TINYINT(1),
    stock_id VARCHAR(10),
    politician_id VARCHAR(255),
    volume FLOAT,
    date DATETIME,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (stock_id, date) REFERENCES stocks(ticker,Date),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS investor_order
(
    price FLOAT,
    buy TINYINT(1),
    stock_id VARCHAR(10),
    investor_id INT,
    volume FLOAT,
    date DATETIME,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (stock_id, date) REFERENCES stocks(ticker, Date),
    FOREIGN KEY (investor_id) REFERENCES investor (id)
);
CREATE TABLE IF NOT EXISTS politician_search_history
(
  investor_id INT,
  politician_id VARCHAR(255),
  date DATETIME,
  id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (investor_id) REFERENCES investor (id),
  FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS stock_search_history
(
    investor_id INT,
    stock_id VARCHAR(10),
    date DATETIME,
    PRIMARY KEY (investor_id, stock_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (stock_id) REFERENCES stock_unique(ticker)
);
CREATE TABLE IF NOT EXISTS journalist_legislation
(
    created_at DATETIME,
    journalist_id INT,
    legislation_id INT,
    PRIMARY KEY (journalist_id, legislation_id),
    FOREIGN KEY (journalist_id) REFERENCES journalist (id),
    FOREIGN KEY (legislation_id) REFERENCES legislation (id)
);
CREATE TABLE IF NOT EXISTS journalist_politician
(
    created_at DATETIME,
    journalist_id INT,
    politician_id VARCHAR(255),
    PRIMARY KEY (journalist_id, politician_id),
    FOREIGN KEY (journalist_id) REFERENCES journalist (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS politician_legislation
(
    created_at DATETIME,
    legislation_id INT,
    politician_id VARCHAR(255),
    PRIMARY KEY (legislation_id, politician_id),
    FOREIGN KEY (legislation_id) REFERENCES legislation (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS politician_manager
(
    created_at DATETIME,
    manager_id INT,
    politician_id VARCHAR(255),
    candidate_opp TINYINT(1),
    PRIMARY KEY (manager_id, politician_id),
    FOREIGN KEY (manager_id) REFERENCES manager (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS politician_investor
(
    created_at DATETIME,
    investor_id INT,
    politician_id VARCHAR(255),
    PRIMARY KEY (investor_id, politician_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);
CREATE TABLE IF NOT EXISTS investor_stock
(
    created_at DATETIME,
    investor_id INT,
    stock_id VARCHAR(10),
    PRIMARY KEY (investor_id, stock_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (stock_id) REFERENCES stock_unique (ticker)
);
CREATE TABLE IF NOT EXISTS investor_politician_order
(
    created_at DATETIME,
    investor_id INT,
    politician_order_id INT,
    PRIMARY KEY (investor_id, politician_order_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (politician_order_id) REFERENCES politician_order (id)
);
CREATE TABLE IF NOT EXISTS legislation_politician_ids
(
    legislation_id INT,
    politician_id VARCHAR(255),
    PRIMARY KEY (legislation_id, politician_id),
    FOREIGN KEY (legislation_id) REFERENCES legislation (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

-- Sample data for investor table
insert into investor (name, created_at, amount_invested, id) values ('Bertina Robeiro', '2024-01-02', 39068.19, 1);
insert into investor (name, created_at, amount_invested, id) values ('Birgit Kuller', '2023-01-01', 47542.44, 2);
insert into investor (name, created_at, amount_invested, id) values ('Ricard Eastgate', '2022-08-26', 26107.25, 3);
insert into investor (name, created_at, amount_invested, id) values ('Daniel Littlepage', '2022-07-10', 16705.29, 4);
insert into investor (name, created_at, amount_invested, id) values ('Jeri Lonsbrough', '2023-01-14', 99222.96, 5);
insert into investor (name, created_at, amount_invested, id) values ('Hercule Benyon', '2023-04-08', 89922.41, 6);
insert into investor (name, created_at, amount_invested, id) values ('Kelli Stocking', '2023-03-14', 64525.58, 7);
insert into investor (name, created_at, amount_invested, id) values ('Kelila Bartoszinski', '2024-03-18', 21102.16, 8);
insert into investor (name, created_at, amount_invested, id) values ('Keith Landrean', '2023-09-20', 49096.22, 9);
insert into investor (name, created_at, amount_invested, id) values ('Jerald Tewelson', '2023-11-26', 84208.73, 10);
insert into investor (name, created_at, amount_invested, id) values ('Bidget Hradsky', '2023-07-15', 42985.83, 11);
insert into investor (name, created_at, amount_invested, id) values ('Marcus Dawid', '2022-12-30', 37983.5, 12);
insert into investor (name, created_at, amount_invested, id) values ('Chic Watting', '2022-06-19', 58316.63, 13);
insert into investor (name, created_at, amount_invested, id) values ('Buiron Banck', '2023-12-05', 24328.62, 14);
insert into investor (name, created_at, amount_invested, id) values ('Nickolai Ferrierio', '2022-09-15', 40848.4, 15);
insert into investor (name, created_at, amount_invested, id) values ('Betta Swinfen', '2024-03-21', 95923.14, 16);
insert into investor (name, created_at, amount_invested, id) values ('Carmella Pocknell', '2023-04-28', 41667.52, 17);
insert into investor (name, created_at, amount_invested, id) values ('Nessy Wollacott', '2024-01-15', 88487.57, 18);
insert into investor (name, created_at, amount_invested, id) values ('Noah Tackle', '2023-04-09', 34906.01, 19);
insert into investor (name, created_at, amount_invested, id) values ('Allie Duprey', '2024-06-03', 23661.61, 20);
insert into investor (name, created_at, amount_invested, id) values ('Dorita Plaister', '2023-03-31', 92433.07, 21);
insert into investor (name, created_at, amount_invested, id) values ('Nathanial Flaherty', '2022-12-21', 92204.47, 22);
insert into investor (name, created_at, amount_invested, id) values ('Nata Marriott', '2023-05-05', 11461.73, 23);
insert into investor (name, created_at, amount_invested, id) values ('Almeda Sesons', '2024-04-16', 65974.56, 24);
insert into investor (name, created_at, amount_invested, id) values ('Nell Aaronsohn', '2023-01-02', 2712.31, 25);
insert into investor (name, created_at, amount_invested, id) values ('Zonnya Skirling', '2023-03-19', 64855.82, 26);
insert into investor (name, created_at, amount_invested, id) values ('Judah Ryott', '2023-05-16', 27515.22, 27);
insert into investor (name, created_at, amount_invested, id) values ('Cosmo Winters', '2023-03-30', 94638.37, 28);
insert into investor (name, created_at, amount_invested, id) values ('Catrina Plummer', '2023-02-13', 86029.76, 29);
insert into investor (name, created_at, amount_invested, id) values ('Levi Finnimore', '2022-10-13', 15276.34, 30);
insert into investor (name, created_at, amount_invested, id) values ('Jeramie Goulthorp', '2024-04-24', 25080.16, 31);
insert into investor (name, created_at, amount_invested, id) values ('George MacPadene', '2024-03-01', 35698.06, 32);
insert into investor (name, created_at, amount_invested, id) values ('Kerk Tonsley', '2023-01-10', 22759.07, 33);
insert into investor (name, created_at, amount_invested, id) values ('Catherina Bidder', '2022-10-11', 64394.32, 34);
insert into investor (name, created_at, amount_invested, id) values ('Josselyn Aleksashin', '2023-04-18', 99913.04, 35);
insert into investor (name, created_at, amount_invested, id) values ('Michel Lory', '2023-07-23', 36067.48, 36);
insert into investor (name, created_at, amount_invested, id) values ('Clementina Hellsdon', '2023-01-15', 88620.88, 37);
insert into investor (name, created_at, amount_invested, id) values ('Viv Fumagall', '2023-12-18', 94357.81, 38);
insert into investor (name, created_at, amount_invested, id) values ('Hans Djekovic', '2022-07-17', 87120.4, 39);
insert into investor (name, created_at, amount_invested, id) values ('Hewitt Gare', '2023-08-03', 8326.08, 40);
insert into investor (name, created_at, amount_invested, id) values ('Aprilette Cellone', '2022-06-11', 64643.74, 41);
insert into investor (name, created_at, amount_invested, id) values ('Reinwald Bendtsen', '2024-05-31', 97529.5, 42);
insert into investor (name, created_at, amount_invested, id) values ('Micheil Wingatt', '2022-12-17', 17473.96, 43);
insert into investor (name, created_at, amount_invested, id) values ('Vladimir Borland', '2024-05-26', 29061.39, 44);
insert into investor (name, created_at, amount_invested, id) values ('Anallise Righy', '2022-11-23', 8288.64, 45);
insert into investor (name, created_at, amount_invested, id) values ('Max Harvie', '2022-06-22', 25314.52, 46);
insert into investor (name, created_at, amount_invested, id) values ('Beatrix Liccardo', '2022-07-06', 84437.89, 47);
insert into investor (name, created_at, amount_invested, id) values ('Prue Staries', '2023-06-26', 97738.21, 48);
insert into investor (name, created_at, amount_invested, id) values ('Mick Aspinal', '2022-06-29', 71384.69, 49);
insert into investor (name, created_at, amount_invested, id) values ('Kelly Heale', '2023-01-25', 6610.95, 50);
insert into investor (name, created_at, amount_invested, id) values ('Hiram Bridgeland', '2023-11-21', 60087.89, 51);
insert into investor (name, created_at, amount_invested, id) values ('Nat Kleinsmuntz', '2023-01-18', 72491.54, 52);
insert into investor (name, created_at, amount_invested, id) values ('Maison Presidey', '2023-06-16', 73913.61, 53);
insert into investor (name, created_at, amount_invested, id) values ('Taryn Marte', '2023-03-27', 91496.65, 54);
insert into investor (name, created_at, amount_invested, id) values ('Nichol Adams', '2022-08-03', 69666.91, 55);
insert into investor (name, created_at, amount_invested, id) values ('Manfred Whipp', '2023-03-22', 43030.6, 56);
insert into investor (name, created_at, amount_invested, id) values ('Boone Paulsson', '2024-03-10', 46916.02, 57);
insert into investor (name, created_at, amount_invested, id) values ('Steve Vedyashkin', '2023-01-10', 77977.95, 58);
insert into investor (name, created_at, amount_invested, id) values ('Darline Quidenham', '2024-05-06', 23536.61, 59);
insert into investor (name, created_at, amount_invested, id) values ('Beckie Lavender', '2022-09-24', 19541.25, 60);
insert into investor (name, created_at, amount_invested, id) values ('Kara-lynn Kores', '2023-02-21', 25079.59, 61);
insert into investor (name, created_at, amount_invested, id) values ('Chane Pepler', '2023-03-19', 68314.11, 62);
insert into investor (name, created_at, amount_invested, id) values ('Packston Hubbart', '2023-11-17', 77267.26, 63);
insert into investor (name, created_at, amount_invested, id) values ('Jacquenette Hendrich', '2023-03-01', 91416.74, 64);
insert into investor (name, created_at, amount_invested, id) values ('Putnam Glasman', '2024-01-10', 41009.09, 65);
insert into investor (name, created_at, amount_invested, id) values ('June Follett', '2022-10-26', 95043.32, 66);
insert into investor (name, created_at, amount_invested, id) values ('Anette Chaster', '2022-12-05', 89670.39, 67);
insert into investor (name, created_at, amount_invested, id) values ('Hewitt Cabble', '2023-06-15', 43945.87, 68);
insert into investor (name, created_at, amount_invested, id) values ('Creighton Juanico', '2022-10-31', 8663.11, 69);
insert into investor (name, created_at, amount_invested, id) values ('Maxine Shropsheir', '2023-09-18', 18868.61, 70);
insert into investor (name, created_at, amount_invested, id) values ('Nathanael Prowting', '2022-07-29', 22529.35, 71);
insert into investor (name, created_at, amount_invested, id) values ('Clementina Bour', '2023-07-11', 23314.96, 72);
insert into investor (name, created_at, amount_invested, id) values ('Dunc Waterman', '2023-04-12', 9591.15, 73);
insert into investor (name, created_at, amount_invested, id) values ('Consuelo Peller', '2024-05-21', 30207.57, 74);
insert into investor (name, created_at, amount_invested, id) values ('Lisa Menelaws', '2023-04-28', 33511.4, 75);
insert into investor (name, created_at, amount_invested, id) values ('Kristine Pretsel', '2022-07-22', 13760.22, 76);
insert into investor (name, created_at, amount_invested, id) values ('Donavon Lippiatt', '2023-11-26', 63099.07, 77);
insert into investor (name, created_at, amount_invested, id) values ('Kippy Craddock', '2023-12-12', 59036.01, 78);
insert into investor (name, created_at, amount_invested, id) values ('Aldridge Hailwood', '2024-04-23', 29531.21, 79);
insert into investor (name, created_at, amount_invested, id) values ('Paolina Kingett', '2024-02-27', 72605.54, 80);
insert into investor (name, created_at, amount_invested, id) values ('Fredrika Hews', '2023-07-04', 16093.34, 81);
insert into investor (name, created_at, amount_invested, id) values ('Kathye Uppett', '2023-05-25', 93397.24, 82);
insert into investor (name, created_at, amount_invested, id) values ('Vaughan Bendall', '2023-03-12', 18439.11, 83);
insert into investor (name, created_at, amount_invested, id) values ('Shurlock Ewbanke', '2022-07-25', 71650.05, 84);
insert into investor (name, created_at, amount_invested, id) values ('Barth Zuker', '2023-12-25', 79602.29, 85);
insert into investor (name, created_at, amount_invested, id) values ('Ringo Trowel', '2023-07-04', 75392.43, 86);
insert into investor (name, created_at, amount_invested, id) values ('Fawne Huskinson', '2024-03-31', 45960.13, 87);
insert into investor (name, created_at, amount_invested, id) values ('Brina MacCheyne', '2022-09-14', 71142.62, 88);
insert into investor (name, created_at, amount_invested, id) values ('Jemima Ashmole', '2023-06-07', 81578.82, 89);
insert into investor (name, created_at, amount_invested, id) values ('Nissy Remer', '2022-08-03', 79915.78, 90);
insert into investor (name, created_at, amount_invested, id) values ('Susannah Corselles', '2023-04-30', 54342.13, 91);
insert into investor (name, created_at, amount_invested, id) values ('Cobby Philipps', '2023-05-18', 33962.19, 92);
insert into investor (name, created_at, amount_invested, id) values ('Misti Jeffery', '2023-12-06', 26800.36, 93);
insert into investor (name, created_at, amount_invested, id) values ('Ciel Leppo', '2023-04-15', 73128.23, 94);
insert into investor (name, created_at, amount_invested, id) values ('Binni Sapson', '2023-12-12', 87207.18, 95);
insert into investor (name, created_at, amount_invested, id) values ('Hale Lougheid', '2023-06-27', 67506.06, 96);
insert into investor (name, created_at, amount_invested, id) values ('Kally Harome', '2023-04-26', 80868.83, 97);
insert into investor (name, created_at, amount_invested, id) values ('Gwynne Cabera', '2023-08-17', 92095.72, 98);
insert into investor (name, created_at, amount_invested, id) values ('Witty Fabb', '2024-05-20', 63987.72, 99);
insert into investor (name, created_at, amount_invested, id) values ('Bev Kimbley', '2022-11-03', 97886.15, 100);

-- Sample data for manager table
INSERT INTO manager (name, created_at, party, id) VALUES
('Dee dee Chisnall', '2024-02-05', 'Equality Party', 1),
('Granville Claeskens', '2022-08-27', 'Liberty Party', 2),
('Jerrome Schowenburg', '2022-10-07', 'Liberty Party', 3),
('Cathrine Tellenbrook', '2023-12-03', 'Progressive Party', 4),
('Rip Vears', '2023-09-30', 'Unity Party', 5),
('Pernell Lougheed', '2022-10-03', 'Justice Party', 6),
('Kilian Coverdale', '2022-12-01', 'Progressive Party', 7),
('Katherina Fullalove', '2023-10-13', 'Unity Party', 8),
('Web Penhall', '2023-01-19', 'Progressive Party', 9),
('Kennett Aland', '2024-02-19', 'Unity Party', 10),
('Michel Canepe', '2022-11-30', 'Progressive Party', 11),
('Levi Oliver', '2022-09-17', 'Equality Party', 12),
('Clarke McKeachie', '2023-05-22', 'Equality Party', 13),
('Laurel Hendrich', '2022-11-13', 'Liberty Party', 14),
('Chiquita Doniso', '2022-08-07', 'Liberty Party', 15),
('Vivianna Woolston', '2024-04-18', 'Liberty Party', 16),
('Dorette Barnewille', '2022-12-12', 'Unity Party', 17),
('Beatriz Shmyr', '2023-03-02', 'Liberty Party', 18),
('Gertie Keys', '2023-07-25', 'Liberty Party', 19),
('Weylin Muffen', '2022-11-18', 'Progressive Party', 20),
('Lishe Bocke', '2023-05-23', 'Liberty Party', 21),
('Enrica Curlis', '2023-10-20', 'Equality Party', 22),
('Min Swales', '2022-12-23', 'Justice Party', 23),
('Hamnet Wolfarth', '2022-07-25', 'Liberty Party', 24),
('Renard Surgeon', '2024-01-20', 'Justice Party', 25),
('Mattie Balshaw', '2022-08-05', 'Justice Party', 26),
('Chris Petrovsky', '2022-09-26', 'Unity Party', 27),
('Cate Ebbens', '2024-05-13', 'Equality Party', 28),
('Tibold Senecaut', '2023-12-30', 'Unity Party', 29),
('Jesse Sedgwick', '2023-07-21', 'Unity Party', 30),
('Bab Robardley', '2023-09-06', 'Justice Party', 31),
('Claiborn Clara', '2022-12-19', 'Equality Party', 32),
('Rosalind Oldman', '2022-10-06', 'Liberty Party', 33),
('Sigismond Gioani', '2022-08-29', 'Equality Party', 34),
('Nicholas Aldus', '2022-07-21', 'Progressive Party', 35),
('Edythe Searston', '2023-10-22', 'Justice Party', 36),
('Dyann Tullett', '2023-02-11', 'Progressive Party', 37),
('Zora Lainge', '2022-09-16', 'Unity Party', 38),
('Gilli Twydell', '2023-01-09', 'Unity Party', 39),
('Pris Scibsey', '2024-05-05', 'Liberty Party', 40),
('Mariana Reppaport', '2024-02-07', 'Unity Party', 41),
('Ethelred Peacocke', '2024-03-27', 'Equality Party', 42),
('Bathsheba Taffie', '2022-11-18', 'Liberty Party', 43),
('Cindra Rissen', '2024-01-10', 'Justice Party', 44),
('Berni Pickton', '2022-07-30', 'Progressive Party', 45),
('Aviva Veltman', '2023-05-06', 'Unity Party', 46),
('Fifine Arkow', '2022-11-30', 'Equality Party', 47),
('Caritta Diben', '2024-03-15', 'Progressive Party', 48),
('Tobe Elland', '2023-06-28', 'Unity Party', 49),
('Ruthanne Borkett', '2023-06-15', 'Progressive Party', 50);

-- Sample data for journalist table
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Reta Runcie', '2022-08-29', 'Banks', 'Morning Herald Post', 'Florida', 'Progressive Party', 1);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Scarface Van Dale', '2024-02-17', 'Electric Utilities: Central', 'Morning Herald Post', 'Texas', 'Equality Party', 2);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Tiff Stirgess', '2023-04-27', 'n/a', 'Metro News Express', 'Louisiana', 'Equality Party', 3);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Riobard Sturgeon', '2023-01-22', 'Biotechnology: Commercial Physical & Biological Resarch', 'The Sunday Times', 'District of Columbia', 'Equality Party', 4);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Anthea Selby', '2024-03-09', 'Major Pharmaceuticals', 'The Daily Gazette', 'Texas', 'Justice Party', 5);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Herbert Demongeot', '2023-02-02', 'n/a', 'Metro News Express', 'Alabama', 'Unity Party', 6);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Kayne Perri', '2024-03-13', 'Military/Government/Technical', 'Metro News Express', 'Texas', 'Equality Party', 7);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Sutherland Mosen', '2023-01-07', 'Homebuilding', 'Metro News Express', 'Arizona', 'Unity Party', 8);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Tess Boulde', '2023-11-14', 'Semiconductors', 'The Weekly Observer', 'Iowa', 'Justice Party', 9);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Rubetta Basile', '2023-02-01', 'n/a', 'Morning Herald Post', 'Colorado', 'Liberty Party', 10);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Olenka Bartalini', '2023-07-08', 'n/a', 'The Weekly Observer', 'District of Columbia', 'Progressive Party', 11);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Ivar Wilcher', '2022-09-30', 'Power Generation', 'Daily Sun Chronicle', 'New York', 'Progressive Party', 12);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Leoine Hardeman', '2024-02-14', 'Broadcasting', 'Morning Star Tribune', 'Texas', 'Equality Party', 13);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Teena Schwieso', '2024-05-05', 'n/a', 'The Daily Gazette', 'Florida', 'Progressive Party', 14);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Augustine Bolf', '2023-05-28', 'Electric Utilities: Central', 'Morning Herald Post', 'Texas', 'Liberty Party', 15);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Joel Lintot', '2023-08-23', 'Oil & Gas Production', 'The Weekly Observer', 'California', 'Unity Party', 16);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Danit Wilber', '2023-01-17', 'Major Banks', 'Metro News Express', 'Florida', 'Progressive Party', 17);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Juana Buret', '2023-04-15', 'Savings Institutions', 'Morning Star Tribune', 'California', 'Unity Party', 18);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Wald Volage', '2022-10-28', 'Real Estate Investment Trusts', 'Daily Sun Chronicle', 'Michigan', 'Justice Party', 19);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Kristan Simkovitz', '2022-07-14', 'Major Banks', 'Morning Star Tribune', 'Arizona', 'Progressive Party', 20);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Joaquin Shone', '2024-04-29', 'Oil & Gas Production', 'Sunrise News Journal', 'Wisconsin', 'Unity Party', 21);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Christoph Robertson', '2022-11-18', 'n/a', 'The Sunday Times', 'Louisiana', 'Justice Party', 22);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Hannis Kelley', '2023-09-10', 'Clothing/Shoe/Accessory Stores', 'Daily Sun Chronicle', 'California', 'Unity Party', 23);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Belva Eldrett', '2023-04-22', 'n/a', 'The Daily Gazette', 'Iowa', 'Progressive Party', 24);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Alexandr McVeigh', '2023-11-14', 'Real Estate Investment Trusts', 'Morning Herald Post', 'Massachusetts', 'Unity Party', 25);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Beverlie Fifield', '2024-03-17', 'Investment Bankers/Brokers/Service', 'Sunrise News Journal', 'Ohio', 'Liberty Party', 26);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Aubert North', '2022-12-01', 'Telecommunications Equipment', 'Evening News Sentinel', 'California', 'Justice Party', 27);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Alethea Cisar', '2023-07-21', 'Other Specialty Stores', 'Evening News Sentinel', 'California', 'Unity Party', 28);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Maggy Branch', '2023-05-07', 'Biotechnology: Laboratory Analytical Instruments', 'Evening News Sentinel', 'Indiana', 'Liberty Party', 29);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Dewie Brecher', '2022-07-04', 'Medical Specialities', 'City Times Herald', 'Kentucky', 'Unity Party', 30);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Tanya Sugar', '2024-04-17', 'n/a', 'Evening News Sentinel', 'Alabama', 'Equality Party', 31);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Rebecka Adamovitz', '2024-05-21', 'Hospital/Nursing Management', 'Metro News Express', 'North Carolina', 'Liberty Party', 32);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Arney Keasy', '2023-01-21', 'n/a', 'Sunrise News Journal', 'Indiana', 'Unity Party', 33);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Garrot Clavering', '2024-03-30', 'Natural Gas Distribution', 'The Weekly Observer', 'Ohio', 'Liberty Party', 34);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Marchall Minter', '2022-10-18', 'Biotechnology: In Vitro & In Vivo Diagnostic Substances', 'The Daily Gazette', 'Colorado', 'Unity Party', 35);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Casandra Compston', '2023-01-15', 'Business Services', 'Metro News Express', 'Minnesota', 'Equality Party', 36);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Thorin Greenwell', '2022-06-26', 'Precious Metals', 'Metro News Express', 'Minnesota', 'Equality Party', 37);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Elston Duffan', '2022-08-11', 'n/a', 'Sunrise News Journal', 'Ohio', 'Justice Party', 38);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Anderea Braunston', '2023-10-23', 'Auto Manufacturing', 'The Daily Gazette', 'Texas', 'Unity Party', 39);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Ramsey Wealleans', '2024-02-29', 'n/a', 'The Sunday Times', 'California', 'Progressive Party', 40);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Andreana Mumm', '2022-09-15', 'Semiconductors', 'Morning Star Tribune', 'Nevada', 'Equality Party', 41);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Marja Pinyon', '2024-04-01', 'n/a', 'City Times Herald', 'California', 'Liberty Party', 42);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Serene Lammers', '2022-11-16', 'n/a', 'Morning Star Tribune', 'Indiana', 'Progressive Party', 43);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Marcy Rawls', '2024-04-28', 'Restaurants', 'Morning Herald Post', 'Indiana', 'Progressive Party', 44);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Sebastian Haliburn', '2023-01-27', 'Major Pharmaceuticals', 'Metro News Express', 'District of Columbia', 'Unity Party', 45);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Gabriell Benedikt', '2023-10-07', 'Newspapers/Magazines', 'The Weekly Observer', 'Alabama', 'Equality Party', 46);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Brook Iskowitz', '2023-02-03', 'Telecommunications Equipment', 'Daily Sun Chronicle', 'Maryland', 'Equality Party', 47);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Calli Heinritz', '2024-01-16', 'Biotechnology: In Vitro & In Vivo Diagnostic Substances', 'Daily Sun Chronicle', 'California', 'Unity Party', 48);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Brandy West', '2024-03-07', 'n/a', 'The Weekly Observer', 'New York', 'Justice Party', 49);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Fonz Adamov', '2022-12-26', 'Clothing/Shoe/Accessory Stores', 'Daily Sun Chronicle', 'Louisiana', 'Unity Party', 50);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Em Rotter', '2024-03-17', 'Marine Transportation', 'Metro News Express', 'Texas', 'Progressive Party', 51);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Kaylee Dumphreys', '2023-07-01', 'Military/Government/Technical', 'Daily Sun Chronicle', 'Florida', 'Equality Party', 52);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Emeline Maymand', '2023-02-07', 'Forest Products', 'Daily Sun Chronicle', 'Virginia', 'Justice Party', 53);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('D''arcy Kareman', '2024-01-31', 'Containers/Packaging', 'Sunrise News Journal', 'Missouri', 'Progressive Party', 54);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Victoria Hoyt', '2022-08-01', 'n/a', 'Morning Star Tribune', 'California', 'Equality Party', 55);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Caritta Avramovsky', '2024-05-05', 'n/a', 'Evening News Sentinel', 'Michigan', 'Justice Party', 56);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Xylina Bettanay', '2023-11-26', 'Restaurants', 'Daily Sun Chronicle', 'Utah', 'Equality Party', 57);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Mickey Bester', '2024-04-12', 'Medical/Nursing Services', 'Morning Herald Post', 'Missouri', 'Unity Party', 58);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Hersh Beart', '2023-03-23', 'Medical/Nursing Services', 'City Times Herald', 'California', 'Equality Party', 59);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Dani Frammingham', '2023-09-24', 'Major Banks', 'Morning Herald Post', 'Texas', 'Progressive Party', 60);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Giselbert Busek', '2022-12-24', 'n/a', 'The Daily Gazette', 'Arkansas', 'Equality Party', 61);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Maribel Laxson', '2024-03-23', 'Investment Managers', 'City Times Herald', 'Colorado', 'Progressive Party', 62);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Abel Currey', '2022-07-05', 'n/a', 'Morning Star Tribune', 'Texas', 'Equality Party', 63);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Kevin Suatt', '2023-05-01', 'Real Estate Investment Trusts', 'Morning Herald Post', 'Louisiana', 'Equality Party', 64);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Fons Hylands', '2023-10-20', 'n/a', 'Morning Star Tribune', 'District of Columbia', 'Progressive Party', 65);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Maure Meindl', '2024-01-23', 'Industrial Specialties', 'City Times Herald', 'California', 'Progressive Party', 66);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Eduino Bonnin', '2024-04-19', 'Homebuilding', 'The Weekly Observer', 'South Carolina', 'Unity Party', 67);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Karney Tunaclift', '2024-04-03', 'Auto Parts:O.E.M.', 'Morning Star Tribune', 'Colorado', 'Justice Party', 68);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Katharyn Massimo', '2022-09-26', 'Major Banks', 'City Times Herald', 'California', 'Unity Party', 69);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Nettle Heggison', '2024-04-23', 'Major Pharmaceuticals', 'Evening News Sentinel', 'South Dakota', 'Progressive Party', 70);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Farris Tant', '2022-11-02', 'Oil & Gas Production', 'The Weekly Observer', 'Texas', 'Liberty Party', 71);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Norris Sammes', '2023-10-03', 'Specialty Chemicals', 'City Times Herald', 'North Carolina', 'Progressive Party', 72);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Melantha Knowller', '2023-07-25', 'Other Consumer Services', 'The Sunday Times', 'California', 'Equality Party', 73);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Dulci Ramiro', '2022-11-29', 'Beverages (Production/Distribution)', 'Morning Herald Post', 'New Mexico', 'Justice Party', 74);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Andy Normabell', '2024-03-28', 'Packaged Foods', 'Daily Sun Chronicle', 'Kansas', 'Unity Party', 75);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Diego Pedwell', '2023-09-15', 'Automotive Aftermarket', 'Morning Herald Post', 'Texas', 'Justice Party', 76);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Corby Clancey', '2023-12-03', 'Finance: Consumer Services', 'Metro News Express', 'California', 'Progressive Party', 77);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Diannne Deddum', '2023-08-02', 'n/a', 'Metro News Express', 'Texas', 'Liberty Party', 78);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Jenny de Almeida', '2024-04-08', 'Clothing/Shoe/Accessory Stores', 'Evening News Sentinel', 'California', 'Progressive Party', 79);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Gretel Aleksic', '2024-04-29', 'n/a', 'The Weekly Observer', 'Texas', 'Progressive Party', 80);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Del Jeduch', '2023-09-21', 'Major Banks', 'Metro News Express', 'Louisiana', 'Unity Party', 81);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Rosa Jozaitis', '2022-12-16', 'Major Banks', 'The Daily Gazette', 'Wisconsin', 'Unity Party', 82);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Randall Gallienne', '2024-03-09', 'Apparel', 'Daily Sun Chronicle', 'Colorado', 'Justice Party', 83);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Cleopatra Larmour', '2024-05-08', 'n/a', 'Sunrise News Journal', 'Louisiana', 'Liberty Party', 84);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Julietta Heistermann', '2023-03-22', 'Professional Services', 'The Daily Gazette', 'Florida', 'Unity Party', 85);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Otes Roseburgh', '2022-08-04', 'Beverages (Production/Distribution)', 'Evening News Sentinel', 'South Carolina', 'Progressive Party', 86);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Camala McGahern', '2023-01-28', 'Medical/Dental Instruments', 'The Daily Gazette', 'Illinois', 'Unity Party', 87);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Alvira Aggas', '2022-11-19', 'n/a', 'The Weekly Observer', 'Minnesota', 'Equality Party', 88);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Odessa Pren', '2023-12-24', 'n/a', 'The Daily Gazette', 'Nevada', 'Justice Party', 89);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Howey Gorges', '2023-10-11', 'Oil & Gas Production', 'Morning Herald Post', 'Indiana', 'Liberty Party', 90);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Kellsie Sellars', '2023-05-27', 'Building Products', 'Evening News Sentinel', 'Texas', 'Progressive Party', 91);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Gonzalo Kettlewell', '2023-11-11', 'Trucking Freight/Courier Services', 'The Sunday Times', 'California', 'Unity Party', 92);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Dwight Tolemache', '2024-05-24', 'n/a', 'The Weekly Observer', 'Montana', 'Progressive Party', 93);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Lowrance Grangier', '2023-08-19', 'Banks', 'Morning Herald Post', 'Tennessee', 'Liberty Party', 94);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Margalit Bartkiewicz', '2022-06-12', 'Power Generation', 'Sunrise News Journal', 'Tennessee', 'Progressive Party', 95);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Ola Noury', '2022-11-09', 'n/a', 'Daily Sun Chronicle', 'Colorado', 'Progressive Party', 96);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Shandra Prigmore', '2023-11-11', 'Computer Software: Prepackaged Software', 'Morning Herald Post', 'Rhode Island', 'Unity Party', 97);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Zebedee Ormston', '2023-01-22', 'n/a', 'Morning Star Tribune', 'Illinois', 'Unity Party', 98);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Zonda Faccini', '2023-12-05', 'Medical/Dental Instruments', 'The Sunday Times', 'Illinois', 'Unity Party', 99);
insert into journalist (name, created_at, expert_industry, company, state, party, id) values ('Cosetta Glynn', '2023-11-01', 'Major Pharmaceuticals', 'Daily Sun Chronicle', 'California', 'Unity Party', 100);

-- insert into stock (curr_price, company, ticker, id) values (472.91, 'Barings Participation Investors', 'MPV', 1);
-- insert into stock (curr_price, company, ticker, id) values (356.17, 'PennantPark Investment Corporation', 'PNTA.CL', 2);
-- insert into stock (curr_price, company, ticker, id) values (677.63, 'GDS Holdings Limited', 'GDS', 3);
-- insert into stock (curr_price, company, ticker, id) values (497.91, 'NMI Holdings Inc', 'NMIH', 4);
-- insert into stock (curr_price, company, ticker, id) values (282.79, 'Tocagen Inc.', 'TOCA', 5);
-- insert into stock (curr_price, company, ticker, id) values (765.84, 'Ocera Therapeutics, Inc.', 'OCRX', 6);
-- insert into stock (curr_price, company, ticker, id) values (765.34, 'AllianzGI Convertible & Income Fund II', 'NCZ', 7);
-- insert into stock (curr_price, company, ticker, id) values (812.29, 'CECO Environmental Corp.', 'CECE', 8);
-- insert into stock (curr_price, company, ticker, id) values (420.56, 'Mannatech, Incorporated', 'MTEX', 9);
-- insert into stock (curr_price, company, ticker, id) values (995.03, 'Mattel, Inc.', 'MAT', 10);
-- insert into stock (curr_price, company, ticker, id) values (445.53, 'Aldeyra Therapeutics, Inc.', 'ALDX', 11);
-- insert into stock (curr_price, company, ticker, id) values (498.27, 'Taylor Morrison Home Corporation', 'TMHC', 12);
-- insert into stock (curr_price, company, ticker, id) values (327.47, 'Amaya Inc.', 'AYA', 13);
-- insert into stock (curr_price, company, ticker, id) values (80.73, 'Philip Morris International Inc', 'PM', 14);
-- insert into stock (curr_price, company, ticker, id) values (359.67, 'Bridgford Foods Corporation', 'BRID', 15);
-- insert into stock (curr_price, company, ticker, id) values (902.06, 'PowerShares DWA Energy Momentum Portfolio', 'PXI', 16);
-- insert into stock (curr_price, company, ticker, id) values (36.63, 'Rocket Fuel Inc.', 'FUEL', 17);
-- insert into stock (curr_price, company, ticker, id) values (555.84, 'IDACORP, Inc.', 'IDA', 18);
-- insert into stock (curr_price, company, ticker, id) values (346.73, 'Ocular Therapeutix, Inc.', 'OCUL', 19);
-- insert into stock (curr_price, company, ticker, id) values (997.5, 'Seadrill Partners LLC', 'SDLP', 20);
-- insert into stock (curr_price, company, ticker, id) values (289.94, 'China Life Insurance Company Limited', 'LFC', 21);
-- insert into stock (curr_price, company, ticker, id) values (78.42, 'iShares iBoxx $ High Yield ex Oil & Gas Corporate Bond ETF', 'HYXE', 22);
-- insert into stock (curr_price, company, ticker, id) values (365.54, 'Advanced Emissions Solutions, Inc.', 'ADES', 23);
-- insert into stock (curr_price, company, ticker, id) values (846.53, 'Planet Fitness, Inc.', 'PLNT', 24);
-- insert into stock (curr_price, company, ticker, id) values (505.16, 'FIRST REPUBLIC BANK', 'FRC^C', 25);
-- insert into stock (curr_price, company, ticker, id) values (976.97, 'Flaherty & Crumrine Total Return Fund Inc', 'FLC', 26);
-- insert into stock (curr_price, company, ticker, id) values (225.77, 'The Navigators Group, Inc.', 'NAVG', 27);
-- insert into stock (curr_price, company, ticker, id) values (549.49, 'Frankly, Inc.', 'FKLYU', 28);
-- insert into stock (curr_price, company, ticker, id) values (934.34, 'Ormat Technologies, Inc.', 'ORA', 29);
-- insert into stock (curr_price, company, ticker, id) values (149.66, 'Pimco Corporate & Income Stategy Fund', 'PCN', 30);
-- insert into stock (curr_price, company, ticker, id) values (228.46, 'Janus Henderson Group plc', 'JHG', 31);
-- insert into stock (curr_price, company, ticker, id) values (814.65, 'LINE Corporation', 'LN', 32);
-- insert into stock (curr_price, company, ticker, id) values (128.77, 'Orchid Island Capital, Inc.', 'ORC', 33);
-- insert into stock (curr_price, company, ticker, id) values (66.05, 'NICE Ltd', 'NICE', 34);
-- insert into stock (curr_price, company, ticker, id) values (204.46, 'New York Mortgage Trust, Inc.', 'NYMTO', 35);
-- insert into stock (curr_price, company, ticker, id) values (12.52, 'Tableau Software, Inc.', 'DATA', 36);
-- insert into stock (curr_price, company, ticker, id) values (131.26, 'Bank of America Corporation', 'BAC^Y', 37);
-- insert into stock (curr_price, company, ticker, id) values (696.72, 'Tuttle Tactical Management U.S. Core ETF', 'TUTT', 38);
-- insert into stock (curr_price, company, ticker, id) values (352.29, 'Upland Software, Inc.', 'UPLD', 39);
-- insert into stock (curr_price, company, ticker, id) values (407.96, 'Invesco Mortgage Capital Inc.', 'IVR^A', 40);
-- insert into stock (curr_price, company, ticker, id) values (809.04, 'Kayne Anderson Acquisition Corp.', 'KAAC', 41);
-- insert into stock (curr_price, company, ticker, id) values (490.3, 'Rosetta Genomics Ltd.', 'ROSG', 42);
-- insert into stock (curr_price, company, ticker, id) values (563.5, 'Weatherford International plc', 'WFT', 43);
-- insert into stock (curr_price, company, ticker, id) values (300.4, 'Cedar Fair, L.P.', 'FUN', 44);
-- insert into stock (curr_price, company, ticker, id) values (489.57, 'Scudder Strategic Municiple Income Trust', 'KSM', 45);
-- insert into stock (curr_price, company, ticker, id) values (367.77, 'Southern California Edison Company', 'SCE^H', 46);
-- insert into stock (curr_price, company, ticker, id) values (947.31, 'Dreyfus Municipal Bond Infrastructure Fund, Inc.', 'DMB', 47);
-- insert into stock (curr_price, company, ticker, id) values (351.72, 'Canadian Natural Resources Limited', 'CNQ', 48);
-- insert into stock (curr_price, company, ticker, id) values (146.47, 'PVH Corp.', 'PVH', 49);
-- insert into stock (curr_price, company, ticker, id) values (160.2, 'Vanguard Total International Stock ETF', 'VXUS', 50);
-- insert into stock (curr_price, company, ticker, id) values (208.14, 'Eaton Vance Risk-Managed Diversified Equity Income Fund', 'ETJ', 51);
-- insert into stock (curr_price, company, ticker, id) values (910.0, 'Rambus, Inc.', 'RMBS', 52);
-- insert into stock (curr_price, company, ticker, id) values (96.48, 'Neurocrine Biosciences, Inc.', 'NBIX', 53);
-- insert into stock (curr_price, company, ticker, id) values (480.65, 'Weyerhaeuser Company', 'WY', 54);
-- insert into stock (curr_price, company, ticker, id) values (185.76, 'Sportsman''s Warehouse Holdings, Inc.', 'SPWH', 55);
-- insert into stock (curr_price, company, ticker, id) values (368.7, 'Microsoft Corporation', 'MSFT', 56);
-- insert into stock (curr_price, company, ticker, id) values (106.77, 'Interactive Brokers Group, Inc.', 'IBKR', 57);
-- insert into stock (curr_price, company, ticker, id) values (973.8, 'Modern Media Acquisition Corp.', 'MMDMU', 58);
-- insert into stock (curr_price, company, ticker, id) values (919.08, 'RSP Permian, Inc.', 'RSPP', 59);
-- insert into stock (curr_price, company, ticker, id) values (47.23, 'American Express Company', 'AXP', 60);
-- insert into stock (curr_price, company, ticker, id) values (692.49, 'Navistar International Corporation', 'NAV^D', 61);
-- insert into stock (curr_price, company, ticker, id) values (58.79, 'Nuveen Select Tax Free Income Portfolio III', 'NXR', 62);
-- insert into stock (curr_price, company, ticker, id) values (614.85, 'Microvision, Inc.', 'MVIS', 63);
-- insert into stock (curr_price, company, ticker, id) values (256.29, 'Flaherty & Crumrine Total Return Fund Inc', 'FLC', 64);
-- insert into stock (curr_price, company, ticker, id) values (408.15, 'Scudder Strategic Income Trust', 'KST', 65);
-- insert into stock (curr_price, company, ticker, id) values (685.73, 'First Trust South Korea AlphaDEX Fund', 'FKO', 66);
-- insert into stock (curr_price, company, ticker, id) values (338.33, 'Gores Holdings II, Inc.', 'GSHT', 67);
-- insert into stock (curr_price, company, ticker, id) values (251.76, 'Winmark Corporation', 'WINA', 68);
-- insert into stock (curr_price, company, ticker, id) values (792.09, 'PowerShares BuyBack Achievers Portfolio', 'PKW', 69);
-- insert into stock (curr_price, company, ticker, id) values (450.2, 'Diodes Incorporated', 'DIOD', 70);
-- insert into stock (curr_price, company, ticker, id) values (240.32, 'Playa Hotels & Resorts N.V.', 'PLYAW', 71);
-- insert into stock (curr_price, company, ticker, id) values (83.77, 'CSW Industrials, Inc.', 'CSWI', 72);
-- insert into stock (curr_price, company, ticker, id) values (67.17, 'City Office REIT, Inc.', 'CIO', 73);
-- insert into stock (curr_price, company, ticker, id) values (160.61, 'Helen of Troy Limited', 'HELE', 74);
-- insert into stock (curr_price, company, ticker, id) values (98.15, 'Gabelli Dividend', 'GDV^D', 75);
-- insert into stock (curr_price, company, ticker, id) values (325.71, 'Pathfinder Bancorp, Inc.', 'PBHC', 76);
-- insert into stock (curr_price, company, ticker, id) values (352.81, 'Eltek Ltd.', 'ELTK', 77);
-- insert into stock (curr_price, company, ticker, id) values (816.91, 'National General Holdings Corp', 'NGHCO', 78);
-- insert into stock (curr_price, company, ticker, id) values (923.82, 'Endurance International Group Holdings, Inc.', 'EIGI', 79);
-- insert into stock (curr_price, company, ticker, id) values (468.59, 'Iridium Communications Inc', 'IRDM', 80);
-- insert into stock (curr_price, company, ticker, id) values (990.08, 'VeriSign, Inc.', 'VRSN', 81);
-- insert into stock (curr_price, company, ticker, id) values (559.31, 'Heartland Financial USA, Inc.', 'HTLF', 82);
-- insert into stock (curr_price, company, ticker, id) values (995.19, 'Catalyst Pharmaceuticals, Inc.', 'CPRX', 83);
-- insert into stock (curr_price, company, ticker, id) values (983.79, 'Goldman Sachs Group, Inc. (The)', 'GS^C', 84);
-- insert into stock (curr_price, company, ticker, id) values (772.91, 'Asia Pacific Wire & Cable Corporation Limited', 'APWC', 85);
-- insert into stock (curr_price, company, ticker, id) values (947.78, 'Moog Inc.', 'MOG.A', 86);
-- insert into stock (curr_price, company, ticker, id) values (795.06, 'Aflac Incorporated', 'AFSD', 87);
-- insert into stock (curr_price, company, ticker, id) values (153.57, 'Dynagas LNG Partners LP', 'DLNG', 88);
-- insert into stock (curr_price, company, ticker, id) values (354.93, 'Semiconductor  Manufacturing International Corporation', 'SMI', 89);
-- insert into stock (curr_price, company, ticker, id) values (525.24, 'CoBiz Financial Inc.', 'COBZ', 90);
-- insert into stock (curr_price, company, ticker, id) values (964.62, 'WPP plc', 'WPPGY', 91);
-- insert into stock (curr_price, company, ticker, id) values (379.45, 'Realty Income Corporation', 'O', 92);
-- insert into stock (curr_price, company, ticker, id) values (979.34, 'Cempra, Inc.', 'CEMP', 93);
-- insert into stock (curr_price, company, ticker, id) values (220.75, 'Dreyfus Strategic Municipals, Inc.', 'LEO', 94);
-- insert into stock (curr_price, company, ticker, id) values (844.5, 'Diageo plc', 'DEO', 95);
-- insert into stock (curr_price, company, ticker, id) values (349.98, 'First Trust Large Cap Growth AlphaDEX Fund', 'FTC', 96);
-- insert into stock (curr_price, company, ticker, id) values (778.86, 'Triumph Group, Inc.', 'TGI', 97);
-- insert into stock (curr_price, company, ticker, id) values (205.77, 'Delaware Enhanced Global Dividend', 'DEX', 98);
-- insert into stock (curr_price, company, ticker, id) values (988.13, 'Hi-Crush Partners LP', 'HCLP', 99);
-- insert into stock (curr_price, company, ticker, id) values (780.26, 'China Jo-Jo Drugstores, Inc.', 'CJJD', 100);


-- Sample data for investor_order table
-- insert into investor_order (price, buy, stock_id, investor_id, volume, date, id) values
--  (51162, 0, 1, 1, 21.77, '2023-06-27', 1),
--  (18686, 1, 2, 2, 5.92, '2023-11-24', 2),
--  (83341, 0, 3, 3, 27.16, '2022-10-31', 3),
--  (30599, 0, 4, 4, 27.83, '2024-04-02', 4),
--  (81941, 0, 5, 5, 27.15, '2023-01-19', 5),
--  (94406, 1, 6, 6, 24.8, '2023-11-08', 6),
--  (57576, 1, 7, 7, 4.13, '2022-08-26', 7),
--  (82904, 1, 8, 8, 25.37, '2024-04-11', 8),
--  (86369, 0, 9, 9, 17.84, '2022-12-29', 9),
--  (27535, 1, 10, 10, 2.98, '2024-03-13', 10),
--  (11345, 1, 11, 11, 23.92, '2022-09-24', 11),
--  (73095, 0, 12, 12, 14.07, '2023-05-06', 12),
--  (37832, 1, 13, 13, 13.48, '2023-11-16', 13),
--  (76062, 0, 14, 14, 19.31, '2022-11-18', 14),
--  (2581, 0, 15, 15, 10.22, '2022-09-17', 15),
--  (74876, 1, 16, 16, 27.54, '2024-04-07', 16),
--  (46238, 1, 17, 17, 11.36, '2024-05-26', 17),
--  (6323, 1, 18, 18, 4.57, '2022-07-04', 18),
--  (66576, 0, 19, 19, 14.01, '2023-09-11', 19),
--  (65484, 1, 20, 20, 20.53, '2023-10-30', 20),
--  (49736, 1, 21, 21, 7.75, '2023-07-25', 21);

-- insert into politician_list (name, party, state, manager_id, id) values
--  ('Britni Gullick', 'Democrat', 'Indiana', 33, 1),
--  ('Jewell Ondrus', 'Republican', 'Georgia', 2, 2),
--  ('Hall MacAnespie', 'Democrat', 'Indiana', 35, 3),
--  ('Stepha Szabo', 'Democrat', 'Texas', 33, 4),
--  ('Guilbert Giovannoni', 'Democrat', 'California', 14, 5),
--  ('Brenda MacKaig', 'Democrat', 'Idaho', 6, 6),
--  ('Frieda Izak', 'Democrat', 'New York', 43, 7),
--  ('Jasmina Bohan', 'Democrat', 'Texas', 22, 8),
--  ('Nils Pehrsson', 'Democrat', 'District of Columbia', 37, 9),
--  ('Edward Woodgate', 'Democrat', 'California', 20, 10),
--  ('Gordon Glandfield', 'Republican', 'Virginia', 4, 11),
--  ('Adler Upcott', 'Republican', 'Connecticut', 17, 12),
--  ('Samaria Bance', 'Republican', 'New York', 39, 13),
--  ('Darya Tarry', 'Democrat', 'Georgia', 3, 14),
--  ('Jason Mamwell', 'Democrat', 'Kansas', 20, 15),
--  ('Eula Aumerle', 'Democrat', 'Florida', 40, 16),
--  ('Joline Ritch', 'Republican', 'Kansas', 12, 17),
--  ('Venus Dykes', 'Democrat', 'Pennsylvania', 30, 18),
--  ('Kacy Hallward', 'Democrat', 'Texas', 32, 19),
--  ('Jere Forbes', 'Democrat', 'Utah', 1, 20),
--  ('Yetty Polglase', 'Republican', 'Oklahoma', 37, 21),
--  ('Percival Standell', 'Republican', 'California', 13, 22),
--  ('Silva Whatson', 'Republican', 'Florida', 10, 23),
--  ('Zonnya Twallin', 'Republican', 'South Carolina', 34, 24),
--  ('Miguela Oldham', 'Democrat', 'Minnesota', 42, 25),
--  ('Billye Swetland', 'Republican', 'Alabama', 6, 26),
--  ('Cacilie Goullee', 'Republican', 'Texas', 41, 27),
--  ('Keith O''Corr', 'Democrat', 'Indiana', 31, 28),
--  ('Orsa Pilkington', 'Republican', 'Colorado', 38, 29),
--  ('Neile Pfeffel', 'Republican', 'Oregon', 22, 30),
--  ('Harcourt Catterick', 'Republican', 'Kentucky', 20, 31),
--  ('Sax Whithorn', 'Republican', 'West Virginia', 12, 32),
--  ('Constancia Knutton', 'Democrat', 'Florida', 19, 33),
--  ('Loree Cranna', 'Republican', 'Georgia', 18, 34),
--  ('Marcile Cabrara', 'Republican', 'Pennsylvania', 8, 35),
--  ('Cynthia Leeming', 'Democrat', 'Alabama', 4, 36),
--  ('Daniele Shaw', 'Republican', 'Florida', 42, 37),
--  ('Nehemiah Turnbull', 'Republican', 'California', 45, 38),
--  ('Christiana Cobbe', 'Democrat', 'Connecticut', 25, 39),
--  ('Nicolina Tweddell', 'Republican', 'Pennsylvania', 36, 40),
--  ('Lesley Bravey', 'Democrat', 'California', 31, 41),
--  ('Vivyan Doumic', 'Republican', 'California', 40, 42),
--  ('Ulrich Jodkowski', 'Democrat', 'Ohio', 28, 43),
--  ('Waldemar Stancer', 'Republican', 'California', 7, 44),
--  ('Idell Serot', 'Republican', 'Florida', 25, 45),
--  ('Ursola Sawell', 'Democrat', 'Kentucky', 7, 46),
--  ('Lana Tattersdill', 'Democrat', 'Michigan', 23, 47),
--  ('Vivian Alway', 'Republican', 'Florida', 34, 48),
--  ('Sybille Luetkemeyers', 'Democrat', 'Ohio', 47, 49),
--  ('Paolina Rospars', 'Republican', 'Virginia', 35, 50),
--  ('Alyse Urion', 'Republican', 'California', 14, 51),
--  ('Ruthann Gaven', 'Democrat', 'Ohio', 20, 52),
--  ('Johnath Chadbourn', 'Republican', 'North Carolina', 9, 53),
--  ('Darnell Greenacre', 'Democrat', 'New York', 25, 54),
--  ('Avigdor Clougher', 'Democrat', 'Virginia', 13, 55),
--  ('Elora Pauel', 'Democrat', 'Connecticut', 7, 56),
--  ('Julianne Milroy', 'Democrat', 'Connecticut', 38, 57),
--  ('Ida Bownass', 'Democrat', 'Tennessee', 37, 58),
--  ('Angelico Ambrosoli', 'Democrat', 'Ohio', 4, 59),
--  ('Gunar Sammon', 'Republican', 'District of Columbia', 26, 60),
--  ('Francisco Molder', 'Republican', 'California', 6, 61),
--  ('Tabbie Clout', 'Republican', 'Tennessee', 19, 62),
--  ('Bernete Cunliffe', 'Democrat', 'Indiana', 15, 63),
--  ('Dugald Pretor', 'Democrat', 'Illinois', 20, 64),
--  ('Vernor Doran', 'Democrat', 'Florida', 3, 65),
--  ('Kirstyn Castilljo', 'Republican', 'North Carolina', 15, 66),
--  ('Bunni Golbourn', 'Republican', 'Virginia', 45, 67),
--  ('Bobinette Owens', 'Democrat', 'Vermont', 36, 68),
--  ('Consalve Lecky', 'Republican', 'Michigan', 30, 69),
--  ('Danyette Jerdan', 'Democrat', 'California', 4, 70),
--  ('Trixie Crisp', 'Republican', 'California', 41, 71),
--  ('Niki Ferrero', 'Democrat', 'Texas', 22, 72),
--  ('Charyl Parres', 'Democrat', 'Idaho', 42, 73),
--  ('Violet Beggini', 'Democrat', 'California', 23, 74),
--  ('Abey Trustram', 'Republican', 'Florida', 20, 75),
--  ('Berrie Bownd', 'Democrat', 'Pennsylvania', 9, 76),
--  ('Minne Sollime', 'Democrat', 'Texas', 29, 77),
--  ('Stuart Schooling', 'Democrat', 'Florida', 17, 78),
--  ('Hiram Penberthy', 'Democrat', 'Illinois', 41, 79),
--  ('Gunther Farnworth', 'Republican', 'Oklahoma', 50, 80),
--  ('Lothario Thow', 'Republican', 'Texas', 44, 81),
--  ('Georgie Loffill', 'Republican', 'Pennsylvania', 44, 82),
--  ('Elsy Alldread', 'Democrat', 'South Dakota', 50, 83),
--  ('Ciel Wardrope', 'Republican', 'South Carolina', 25, 84),
--  ('Freeland Pinshon', 'Democrat', 'Maryland', 7, 85),
--  ('Jolynn Wittman', 'Democrat', 'New York', 2, 86),
--  ('Ruben Wilding', 'Republican', 'Louisiana', 43, 87),
--  ('Erin Grime', 'Democrat', 'Michigan', 26, 88),
--  ('Cordie Littlecote', 'Democrat', 'Florida', 31, 89),
--  ('Lindon Shiel', 'Republican', 'Colorado', 11, 90),
--  ('Sigismond Ianizzi', 'Democrat', 'Utah', 27, 91),
--  ('Alvinia Silkston', 'Democrat', 'West Virginia', 25, 92),
--  ('Bryon Mulroy', 'Republican', 'Florida', 43, 93),
--  ('Dorice McKaile', 'Republican', 'Arizona', 25, 94),
--  ('Luigi Wallbutton', 'Democrat', 'Missouri', 21, 95),
--  ('Chad Christaeas', 'Republican', 'Florida', 19, 96),
--  ('Krissie Habbal', 'Republican', 'Oklahoma', 28, 97),
--  ('Gilli Stutely', 'Republican', 'Missouri', 9, 98),
--  ('Pincas Saket', 'Republican', 'New York', 17, 99),
--  ('Rutherford Bjorkan', 'Democrat', 'Texas', 11, 100);

-- -- REPLACE Sample data for politician_order table
--  insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (201.43, 1, 1, 1, 38, '2023-12-17', 1);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (492.96, 1, 2, 2, 51, '2023-08-22', 2);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (694.57, 0, 3, 3, 98, '2023-09-30', 3);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (26.59, 0, 4, 4, 29, '2024-01-18', 4);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (743.84, 0, 5, 5, 71, '2024-03-13', 5);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (822.39, 0, 6, 6, 56, '2023-10-08', 6);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (314.11, 1, 7, 7, 64, '2023-07-28', 7);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (437.94, 0, 8, 8, 75, '2024-05-18', 8);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (809.23, 1, 9, 9, 84, '2023-09-15', 9);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (274.81, 1, 10, 10, 58, '2024-01-24', 10);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (769.48, 0, 11, 11, 2, '2024-03-31', 11);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (367.72, 0, 12, 12, 82, '2023-10-05', 12);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (607.22, 1, 13, 13, 13, '2024-03-31', 13);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (448.8, 0, 14, 14, 44, '2023-07-09', 14);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (533.08, 1, 15, 15, 81, '2023-11-29', 15);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (703.07, 1, 16, 16, 37, '2023-09-16', 16);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (107.12, 0, 17, 17, 51, '2023-10-26', 17);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (166.94, 0, 18, 18, 27, '2023-08-17', 18);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (38.89, 0, 19, 19, 12, '2024-05-02', 19);
-- insert into politician_order (price, buy, stock_id, politician_id, volume, date, id) values (363.77, 1, 20, 20, 90, '2024-02-03', 20);

-- -- Sample data for investor_politician_order table
-- insert into investor_politician_order (created_at, investor_id, politician_order_id) values
--  ('2022-12-23', 1, 1),
--  ('2022-07-23', 2, 2),
--  ('2023-07-22', 3, 3),
--  ('2023-01-04', 4, 4),
--  ('2022-10-06', 5, 5),
--  ('2023-08-11', 6, 6),
--  ('2023-02-24', 7, 7),
--  ('2022-08-28', 8, 8),
--  ('2024-04-24', 9, 9),
--  ('2024-02-27', 10, 10),
--  ('2024-01-12', 11, 11),
--  ('2022-06-19', 12, 12),
--  ('2024-05-23', 13, 13),
--  ('2022-12-15', 14, 14),
--  ('2024-04-18', 15, 15),
--  ('2023-06-17', 16, 16),
--  ('2024-03-04', 17, 17),
--  ('2023-05-30', 18, 18),
--  ('2023-01-26', 19, 19),
--  ('2022-06-22', 20, 20);

-- insert into investor_stock (created_at, investor_id, stock_id) values
--  ('2022-12-27', 1, 1),
--  ('2023-12-23', 2, 2),
--  ('2023-05-25', 3, 3),
--  ('2024-04-15', 4, 4),
--  ('2022-07-13', 5, 5),
--  ('2024-03-09', 6, 6),
--  ('2023-08-03', 7, 7),
--  ('2023-05-26', 8, 8),
--  ('2024-06-03', 9,9),
--  ('2022-08-12', 10, 10),
--  ('2023-06-17', 11, 11),
--  ('2023-12-12', 12, 12),
--  ('2023-06-01', 13, 13),
--  ('2023-09-22', 14, 14),
--  ('2024-01-18', 15, 15),
--  ('2023-05-30', 16, 16),
--  ('2024-02-19', 17, 17),
--  ('2023-11-05', 18, 18),
--  ('2022-10-10', 19, 19),
--  ('2022-07-04', 20, 20);

-- insert into legislation (title, date, pass, active, sector, id) values ('The Internet Privacy Act', '2023-06-16', 0, 1, 'Consumer Services', 1);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Consumer Protection Act', '2023-12-11', 1, 1, 'Capital Goods', 2);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Criminal Justice Reform Act', '2023-12-12', 1, 0, 'n/a', 3);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Consumer Protection Act', '2024-04-26', 1, 0, 'Consumer Services', 4);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Cybersecurity Enhancement Act', '2024-06-04', 1, 0, 'Health Care', 5);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Criminal Justice Reform Act', '2023-09-01', 0, 1, 'Finance', 6);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Renewable Energy Act', '2024-02-17', 1, 0, 'Health Care', 7);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Criminal Justice Reform Act', '2024-01-18', 1, 0, 'Health Care', 8);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Drug Price Regulation Act', '2023-11-21', 1, 1, 'n/a', 9);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Drug Price Regulation Act', '2023-08-29', 1, 1, 'Consumer Services', 10);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Immigration Reform Act', '2023-07-08', 1, 1, 'Consumer Durables', 11);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Consumer Protection Act', '2023-08-19', 0, 0, 'Health Care', 12);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Affordable Housing Act', '2024-02-21', 1, 0, 'Consumer Services', 13);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Clean Air Act', '2023-12-22', 1, 1, 'n/a', 14);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Criminal Justice Reform Act', '2023-08-25', 1, 1, 'Health Care', 15);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Affordable Housing Act', '2023-12-13', 0, 0, 'Health Care', 16);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Affordable Housing Act', '2023-08-27', 0, 1, 'Health Care', 17);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Criminal Justice Reform Act', '2023-09-29', 1, 0, 'Energy', 18);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Consumer Protection Act', '2023-11-29', 0, 1, 'n/a', 19);
-- insert into legislation (title, date, pass, active, sector, id) values ('The Renewable Energy Act', '2023-10-12', 1, 1, 'n/a', 20);

-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2022-08-24', 1, 1);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-12-09', 2, 2);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-06-24', 3, 3);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2022-10-25', 4, 4);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-08-12', 5, 5);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2024-01-30', 6, 6);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-10-13', 7, 7);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2022-08-02', 8, 8);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2024-02-26', 9, 9);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2024-03-12', 10, 10);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-07-10', 11, 11);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2024-05-11', 12, 12);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2022-07-11', 13, 13);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-08-04', 14, 14);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-10-03', 15, 15);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-02-15', 16, 16);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-02-11', 17, 17);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2022-09-21', 18, 18);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-11-27', 19, 19);
-- insert into journalist_legislation (created_at, journalist_id, legislation_id) values ('2023-10-08', 20, 20);

-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2022-10-02', 1, 1);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-11-18', 2, 2);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-02-05', 3, 3);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2022-10-30', 4, 4);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-06-16', 5, 5);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-06-15', 6, 6);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-10-25', 7, 7);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-02-29', 8, 8);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-05-22', 9, 9);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-10-05', 10, 10);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-06-23', 11, 11);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-05-16', 12, 12);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-01-03', 13, 13);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2022-11-17', 14, 14);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2022-11-15', 15, 15);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-10-10', 16, 16);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-05-03', 17, 17);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2024-03-03', 18, 18);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2022-11-26', 19, 19);
-- insert into journalist_politician (created_at, journalist_id, politician_id) values ('2023-09-08', 20, 20);

-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-07-01', 1, 1);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-10-23', 2, 2);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-07-05', 3, 3);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-04-13', 4, 4);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-02-26', 5, 5);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-03-11', 6, 6);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-09-20', 7, 7);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-08-06', 8, 8);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-02-10', 9, 9);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-01-09', 10, 10);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-02-02', 11, 11);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-07-23', 12, 12);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-04-14', 13, 13);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-02-18', 14, 14);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-01-26', 15, 15);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-05-27', 16, 16);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2024-02-04', 17, 17);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-11-24', 18, 18);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-08-03', 19, 19);
-- insert into politician_legislation (created_at, legislation_id, politician_id) values ('2023-07-26', 20, 20);

-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-02-03', 1, 1);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-03-12', 2, 2);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-03-10', 3, 3);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-09-08', 4, 4);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-01-23', 5, 5);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-08-18', 6, 6);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-05-01', 7, 7);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-05-02', 8, 8);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-12-21', 9, 9);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-10-13', 10, 10);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-06-13', 11, 11);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-09-08', 12, 12);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-08-21', 13, 13);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-02-24', 14, 14);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-02-19', 15, 15);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-10-20', 16, 16);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-03-07', 17, 17);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2024-04-02', 18, 18);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-06-06', 19, 19);
-- insert into politician_investor (created_at, investor_id, politician_id) values ('2023-08-08', 20, 20);

-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-10-04', 1, 1);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-07-05', 2, 2);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2024-03-07', 3, 3);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2024-02-28', 4, 4);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-03-09', 5, 5);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-11-03', 6, 6);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2024-05-27', 7, 7);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-03-23', 8, 8);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-01-23', 9, 9);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2024-04-09', 10, 10);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-01-23', 11, 11);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-02-05', 12, 12);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-08-18', 13, 13);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-02-12', 14, 14);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-10-14', 15, 15);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-12-12', 16, 16);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-11-05', 17, 17);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-06-08', 18, 18);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2023-12-10', 19, 19);
-- insert into politician_manager (created_at, manager_id, politician_id) values ('2022-11-02', 20, 20);

-- insert into legislation_politician_ids (legislation_id, politician_id) values (1, 1);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (2, 2);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (3, 3);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (4, 4);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (5, 5);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (6, 6);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (7, 7);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (8, 8);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (9, 9);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (10, 10);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (11, 11);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (12, 12);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (13, 13);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (14, 14);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (15, 15);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (16, 16);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (17, 17);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (18, 18);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (19, 19);
-- insert into legislation_politician_ids (legislation_id, politician_id) values (20, 20);


