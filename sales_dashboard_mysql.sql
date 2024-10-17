CREATE DATABASE sales_dashboard;
use sales_dashboard;
CREATE TABLE sales_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    region VARCHAR(255) NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL,
    quantity_sold INT NOT NULL
);
SHOW TABLES;
DESCRIBE sales_data;
INSERT INTO sales_data (date, product_name, region, revenue, quantity_sold) 
VALUES 
('2024-01-01', 'Laptop', 'North', 1500.00, 10),
('2024-01-02', 'Mobile', 'West', 1000.00, 8),
('2024-01-03', 'Tablet', 'East', 1200.00, 12);
SELECT * FROM sales_data;
SELECT region, SUM(revenue) AS total_revenue 
FROM sales_data 
GROUP BY region;
SELECT product_name, SUM(quantity_sold) AS total_sold 
FROM sales_data 
GROUP BY product_name;
SELECT DATE_FORMAT(date, '%Y-%m') AS month, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY month;
SELECT * FROM sales_data;
SELECT * FROM sales_data WHERE region = 'South';
SELECT DISTINCT region FROM sales_data WHERE region IS NULL OR region = '';
use sales_dashboard;
SHOW TABLES;
DESCRIBE sales_data;
SELECT * FROM sales_data;
use sales_dashboard;
select * from sales_data;



