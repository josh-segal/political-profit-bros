DROP DATABASE IF EXISTS JoshProject;
CREATE DATABASE IF NOT EXISTS JoshProject;

USE JoshProject;

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

CREATE TABLE IF NOT EXISTS politician
(
    name VARCHAR(50) NOT NULL,
    party VARCHAR(50),
    state VARCHAR(50),
    chamber VARCHAR(80),
    manager_id INT,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (manager_id) REFERENCES manager (id)
);

CREATE TABLE IF NOT EXISTS legislation
(
    title VARCHAR(80),
    date DATETIME,
    pass TINYINT(1),
    active TINYINT(1),
    sector VARCHAR(80),
    # multi-value attribute politician-ids
    id INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS stock
(
    curr_price FLOAT,
    company VARCHAR(80),
    industry VARCHAR(80),
    id INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS politician_order
(
    price FLOAT,
    buy TINYINT(1),
    stock_id INT,
    politician_id INT,
    volume FLOAT,
    date DATETIME,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (stock_id) REFERENCES stock (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS investor_order
(
    price FLOAT,
    buy TINYINT(1),
    stock_id INT,
    investor_id INT,
    volume FLOAT,
    date DATETIME,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (stock_id) REFERENCES stock (id),
    FOREIGN KEY (investor_id) REFERENCES investor (id)
);

CREATE TABLE IF NOT EXISTS politician_search_history
(
  investor_id INT,
  politician_id INT,
  date DATETIME,
  id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (investor_id) REFERENCES investor (id),
  FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS stock_search_history
(
    investor_id INT,
    stock_id INT,
    date DATETIME,
    id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (stock_id) REFERENCES stock (id)
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
    politician_id INT,
    PRIMARY KEY (journalist_id, politician_id),
    FOREIGN KEY (journalist_id) REFERENCES journalist (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS politician_legislation
(
    created_at DATETIME,
    legislation_id INT,
    politician_id INT,
    PRIMARY KEY (legislation_id, politician_id),
    FOREIGN KEY (legislation_id) REFERENCES legislation (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS politician_manager
(
    created_at DATETIME,
    manager_id INT,
    politician_id INT,
    PRIMARY KEY (manager_id, politician_id),
    FOREIGN KEY (manager_id) REFERENCES manager (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS politician_investor
(
    created_at DATETIME,
    investor_id INT,
    politician_id INT,
    PRIMARY KEY (investor_id, politician_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);

CREATE TABLE IF NOT EXISTS investor_stock
(
    created_at DATETIME,
    investor_id INT,
    stock_id INT,
    PRIMARY KEY (investor_id, stock_id),
    FOREIGN KEY (investor_id) REFERENCES investor (id),
    FOREIGN KEY (stock_id) REFERENCES stock (id)
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
    politician_id INT,
    PRIMARY KEY (legislation_id, politician_id),
    FOREIGN KEY (legislation_id) REFERENCES legislation (id),
    FOREIGN KEY (politician_id) REFERENCES politician (id)
);


--ChatGPT data for testing, trash later:

-- Sample data for investor table
INSERT INTO investor (name, created_at, amount_invested, id) 
VALUES 
('John Doe', '2024-06-03 00:00:00', 10000.00, 1),
('Alice Smith', '2024-06-03 00:00:00', 15000.00, 2);

-- Sample data for journalist table
INSERT INTO journalist (name, created_at, expert_industry, company, state, party, id) 
VALUES 
('Emma Brown', '2024-06-03 00:00:00', 'Politics', 'ABC News', 'New York', 'Independent', 1),
('Mike Johnson', '2024-06-03 00:00:00', 'Finance', 'XYZ Times', 'California', 'Democratic', 2);

-- Sample data for manager table
INSERT INTO manager (name, created_at, party, id) 
VALUES 
('Tom Smith', '2024-06-03 00:00:00', 'Republican', 1),
('Sarah Johnson', '2024-06-03 00:00:00', 'Democratic', 2);

-- Sample data for politician table
INSERT INTO politician (name, party, state, chamber, manager_id, id) 
VALUES 
('John Smith', 'Republican', 'Texas', 'House', 1, 1),
('Alice Johnson', 'Democratic', 'California', 'Senate', 2, 2);

-- Sample data for legislation table
INSERT INTO legislation (title, date, pass, active, sector, id) 
VALUES 
('Tax Reform Bill', '2024-06-03 00:00:00', 1, 1, 'Finance', 1),
('Healthcare Bill', '2024-06-03 00:00:00', 0, 1, 'Healthcare', 2);

-- Sample data for stock table
INSERT INTO stock (curr_price, company, industry, id) 
VALUES 
(100.00, 'ABC Inc.', 'Technology', 1),
(50.00, 'XYZ Corp.', 'Finance', 2);

-- Sample data for politician_order table
INSERT INTO politician_order (price, buy, stock_id, politician_id, volume, date, id) 
VALUES 
(110.00, 1, 1, 1, 10, '2024-06-03 00:00:00', 1),
(60.00, 0, 2, 2, 20, '2024-06-03 00:00:00', 2);

-- Sample data for investor_order table
INSERT INTO investor_order (price, buy, stock_id, investor_id, volume, date, id) 
VALUES 
(105.00, 1, 1, 1, 5, '2024-06-03 00:00:00', 1),
(55.00, 0, 2, 2, 10, '2024-06-03 00:00:00', 2);

-- Sample data for politician_search_history table
INSERT INTO politician_search_history (investor_id, politician_id, date, id) 
VALUES 
(1, 1, '2024-06-03 00:00:00', 1),
(2, 2, '2024-06-03 00:00:00', 2);

-- Sample data for stock_search_history table
INSERT INTO stock_search_history (investor_id, stock_id, date, id) 
VALUES 
(1, 1, '2024-06-03 00:00:00', 1),
(2, 2, '2024-06-03 00:00:00', 2);

-- Sample data for journalist_legislation table
INSERT INTO journalist_legislation (created_at, journalist_id, legislation_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for journalist_politician table
INSERT INTO journalist_politician (created_at, journalist_id, politician_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for politician_legislation table
INSERT INTO politician_legislation (created_at, legislation_id, politician_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for politician_manager table
INSERT INTO politician_manager (created_at, manager_id, politician_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for politician_investor table
INSERT INTO politician_investor (created_at, investor_id, politician_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for investor_stock table
INSERT INTO investor_stock (created_at, investor_id, stock_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for investor_politician_order table
INSERT INTO investor_politician_order (created_at, investor_id, politician_order_id) 
VALUES 
('2024-06-03 00:00:00', 1, 1),
('2024-06-03 00:00:00', 2, 2);

-- Sample data for legislation_politician_ids table
INSERT INTO legislation_politician_ids (legislation_id, politician_id) 
VALUES 
(1, 1),
(2, 2);










