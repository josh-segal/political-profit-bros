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


-- ChatGPT data for testing, trash later:

-- Sample data for investor table
INSERT INTO investor (name, created_at, amount_invested, id) 
VALUES 
('John Doe', '2024-06-03 00:00:00', 10000.00, 1),
('Alice Smith', '2024-06-03 00:00:00', 15000.00, 2);

INSERT INTO stock (curr_price, company, industry, id) 
VALUES
(10, 'apple', 'technology', 1),
(100, 'Health House', 'BS', 2);








