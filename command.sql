

SELECT DISTINCT(MONTH(expense_date)) ,  SUM(expense_amount)  from expenses 
GROUP BY MONTH(expense_date);



-- ai 
SELECT 
    MONTHNAME(expense_date) AS Month,
    SUM(expense_amount) AS TotalSpend
FROM expenses
GROUP BY Month;
-- ORDER BY MIN(expense_date);


USE expenses;

TRUNCATE TABLE expenses;

-- START HERE ...............

--create table 
CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT ,
    expense_name VARCHAR(25) NOT NULL,
    expense_date DATE NOT NULL,
    expense_amount DECIMAL(10,2) NOT NULL
)

-- DELETE FROM expenses;

SELECT * FROM expenses;

-- INSERT INTO expenses(expense_name,expense_date,expense_amount) VALUES('Rent','2022-01-01', 1000.00),('Rent','2022-01-01', 16600.00);
-- INSERT INTO expenses(expense_name,expense_date,expense_amount) VALUES('Rent','2022-01-01', 1000.00),('Rent','2022-01-01', 16600.00);
-- SELECT * FROM ;




-- SELECT * FROM expenses 
-- WHERE expense_date like "2025-10-%";



-- ************** MASS INSERT *********
-- CAN write a python function to get this data , month entries : 40 - 50 , 12 * 5 * 60 = 2400 entries 

-- LEGIT DATA 11 MONTHS 
-- January 2025 (12 entries)
INSERT INTO expenses (expense_name, expense_date, expense_amount) VALUES 
('Rent', '2025-01-01', 1200.00) ,
('Groceries', '2025-01-03', 180.45),
('Utilities', '2025-01-05', 95.20),
('Transport', '2025-01-07', 42.00),
('Insurance', '2025-01-09', 210.00),
('Dining Out', '2025-01-11', 56.75),
('Healthcare', '2025-01-13', 35.90),
('Internet', '2025-01-15', 40.00),
('Mobile', '2025-01-17', 22.50),
('Entertainment', '2025-01-19', 30.00),
('Education', '2025-01-21', 120.00),
('Savings', '2025-01-23', 300.00),
-- February 2025 (12 entries)
('Rent', '2025-02-01', 1200.00),
('Groceries', '2025-02-02', 172.30),
('Utilities', '2025-02-04', 88.60),
('Transport', '2025-02-06', 38.25),
('Insurance', '2025-02-08', 210.00),
('Dining Out', '2025-02-10', 49.80),
('Healthcare', '2025-02-12', 28.50),
('Internet', '2025-02-14', 40.00),
('Mobile', '2025-02-16', 22.50),
('Entertainment', '2025-02-18', 27.40),
('Education', '2025-02-20', 115.00),
('Savings', '2025-02-22', 300.00),
-- March 2025 (12 entries)
('Rent', '2025-03-01', 1200.00),
('Groceries', '2025-03-03', 185.10),
('Utilities', '2025-03-05', 93.00),
('Transport', '2025-03-07', 45.50),
('Insurance', '2025-03-09', 210.00),
('Dining Out', '2025-03-11', 62.30),
('Healthcare', '2025-03-13', 31.20),
('Internet', '2025-03-15', 40.00),
('Mobile', '2025-03-17', 22.50),
('Entertainment', '2025-03-19', 36.80),
('Education', '2025-03-21', 130.00),
('Savings', '2025-03-23', 300.00),
-- April 2025 (12 entries)
('Rent', '2025-04-01', 1200.00),
('Groceries', '2025-04-02', 176.40),
('Utilities', '2025-04-04', 87.90),
('Transport', '2025-04-06', 39.95),
('Insurance', '2025-04-08', 210.00),
('Dining Out', '2025-04-10', 55.40),
('Healthcare', '2025-04-12', 29.75),
('Internet', '2025-04-14', 40.00),
('Mobile', '2025-04-16', 22.50),
('Entertainment', '2025-04-18', 28.60),
('Education', '2025-04-20', 118.00),
('Savings', '2025-04-22', 300.00),
-- May 2025 (12 entries)
('Rent', '2025-05-01', 1200.00),
('Groceries', '2025-05-03', 190.25),
('Utilities', '2025-05-05', 96.10),
('Transport', '2025-05-07', 47.20),
('Insurance', '2025-05-09', 210.00),
('Dining Out', '2025-05-11', 64.85),
('Healthcare', '2025-05-13', 34.10),
-- INSERT INTO expenses (expense_name, expense_date, expense_amount) VALUES 
('Internet', '2025-05-15', 40.00),
('Mobile', '2025-05-17', 22.50),
('Entertainment', '2025-05-19', 38.50),
('Education', '2025-05-21', 135.00),
('Savings', '2025-05-23', 300.00),-- June 2025 (12 entries)
('Rent', '2025-06-01', 1200.00),
('Groceries', '2025-06-02', 181.60),
('Utilities', '2025-06-04', 90.40),
('Transport', '2025-06-06', 41.10),
('Insurance', '2025-06-08', 210.00),
('Dining Out', '2025-06-10', 57.60),
('Healthcare', '2025-06-12', 30.45),
('Internet', '2025-06-14', 40.00),
('Mobile', '2025-06-16', 22.50),
('Entertainment', '2025-06-18', 31.70),
('Education', '2025-06-20', 122.00),
('Savings', '2025-06-22', 300.00),
-- July 2025 (12 entries)
('Rent', '2025-07-01', 1200.00),
('Groceries', '2025-07-03', 188.70),
('Utilities', '2025-07-05', 92.30),
('Transport', '2025-07-07', 44.00),
('Insurance', '2025-07-09', 210.00),
('Dining Out', '2025-07-11', 61.20),
('Healthcare', '2025-07-13', 33.30),
('Internet', '2025-07-15', 40.00),
('Mobile', '2025-07-17', 22.50),
('Entertainment', '2025-07-19', 37.10),
('Education', '2025-07-21', 128.00),
('Savings', '2025-07-23', 300.00),
-- August 2025 (12 entries)
('Rent', '2025-08-01', 1200.00),
('Groceries', '2025-08-02', 179.90),
('Utilities', '2025-08-04', 89.80),
('Transport', '2025-08-06', 40.30),
('Insurance', '2025-08-08', 210.00),
('Dining Out', '2025-08-10', 53.75),
('Healthcare', '2025-08-12', 29.20),
('Internet', '2025-08-14', 40.00),
('Mobile', '2025-08-16', 22.50),
('Entertainment', '2025-08-18', 29.90),
('Education', '2025-08-20', 119.00),
('Savings', '2025-08-22', 300.00),
-- September 2025 (12 entries)
('Rent', '2025-09-01', 1200.00),
('Groceries', '2025-09-03', 186.40),
('Utilities', '2025-09-05', 91.50),
('Transport', '2025-09-07', 42.80),
('Insurance', '2025-09-09', 210.00),
('Dining Out', '2025-09-11', 58.90),
('Healthcare', '2025-09-13', 31.80),
('Internet', '2025-09-15', 40.00),
('Mobile', '2025-09-17', 22.50),
('Entertainment', '2025-09-19', 33.00),
('Education', '2025-09-21', 124.00),
('Savings', '2025-09-23', 300.00),
-- October 2025 (12 entries)
('Rent', '2025-10-01', 1200.00),
('Groceries', '2025-10-02', 178.55),
('Utilities', '2025-10-04', 88.10),
('Transport', '2025-10-06', 39.40),
('Insurance', '2025-10-08', 210.00),
('Dining Out', '2025-10-10', 52.20),
('Healthcare', '2025-10-12', 28.80),
('Internet', '2025-10-14', 40.00),
('Mobile', '2025-10-16', 22.50),
('Entertainment', '2025-10-18', 28.20),
('Education', '2025-10-20', 117.00),
('Savings', '2025-10-22', 300.00),
-- November 2025 (12 entries)
-- INSERT INTO expenses (expense_name, expense_date, expense_amount) VALUES 
('Rent', '2025-11-01', 1200.00),
('Groceries', '2025-11-03', 191.30),
('Utilities', '2025-11-05', 96.90),
('Transport', '2025-11-07', 47.80),
('Insurance', '2025-11-09', 210.00),
('Dining Out', '2025-11-11', 65.40),
('Healthcare', '2025-11-13', 34.70),
('Internet', '2025-11-15', 40.00),
('Mobile', '2025-11-17', 22.50),
('Entertainment', '2025-11-19', 39.20),
('Education', '2025-11-21', 136.00),
('Savings', '2025-11-23', 300.00);



-- LEGIT DATA OVER 

-- DIVERSIFYING THOSE EXPENSES AS AI IS STUPID 
UPDATE expenses 
SET expense_amount = expense_amount + FLOOR(RAND() * 100);
-- DIVERSIFYING 2  

UPDATE expenses 
SET expense_amount = expense_amount + FLOOR(RAND() * 200) - 60;
-- WHERE expense_date like "2025-%-01";


-- 1st entry is outlier and ruining the charts 
UPDATE expenses 
SET expense_amount = 50 + FLOOR(RAND() * 300)
WHERE expense_date like "2025-%-01";







