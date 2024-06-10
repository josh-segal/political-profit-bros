USE JoshProject;

CREATE TABLE stock_unique AS SELECT DISTINCT ticker, company FROM stocks;
ALTER TABLE stock_unique ADD PRIMARY KEY (ticker);

ALTER TABLE stock_search_history ADD FOREIGN KEY (stock_id) REFERENCES stock_unique (ticker);

ALTER TABLE investor_stock ADD FOREIGN KEY (stock_id) REFERENCES stock_unique (ticker)