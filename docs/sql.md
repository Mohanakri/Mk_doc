# SQL Reference Notes

## Table of Contents
1. [Basic Concepts](#basic-concepts)
2. [Data Types](#data-types)
3. [Basic Queries](#basic-queries)
4. [Filtering & Conditions](#filtering--conditions)
5. [Sorting & Grouping](#sorting--grouping)
6. [Joins](#joins)
7. [Subqueries](#subqueries)
8. [Data Modification](#data-modification)
9. [Table Operations](#table-operations)
10. [Functions](#functions)
11. [Advanced Concepts](#advanced-concepts)

## Basic Concepts

**SQL (Structured Query Language)** is used to communicate with databases. It's divided into several categories:
- **DDL (Data Definition Language)**: CREATE, ALTER, DROP
- **DML (Data Manipulation Language)**: SELECT, INSERT, UPDATE, DELETE
- **DCL (Data Control Language)**: GRANT, REVOKE
- **TCL (Transaction Control Language)**: COMMIT, ROLLBACK

## Data Types

### Common Data Types
```sql
-- Numeric
INT, INTEGER          -- Whole numbers
DECIMAL(p,s)         -- Fixed-point numbers
FLOAT, REAL          -- Floating-point numbers
BIGINT               -- Large integers

-- String/Text
CHAR(n)              -- Fixed-length string
VARCHAR(n)           -- Variable-length string
TEXT                 -- Large text blocks

-- Date/Time
DATE                 -- Date (YYYY-MM-DD)
TIME                 -- Time (HH:MM:SS)
DATETIME, TIMESTAMP  -- Date and time
YEAR                 -- Year value

-- Boolean
BOOLEAN, BOOL        -- True/False values
```

## Basic Queries

### SELECT Statement Structure
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column
LIMIT number;
```

### Basic Examples
```sql
-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- Select with alias
SELECT first_name AS "First Name", salary * 12 AS "Annual Salary"
FROM employees;

-- Distinct values
SELECT DISTINCT department FROM employees;
```

## Filtering & Conditions

### WHERE Clause Operators
```sql
-- Comparison operators
=, !=, <>, <, >, <=, >=

-- Logical operators
AND, OR, NOT

-- Pattern matching
LIKE '%pattern%'     -- Contains pattern
LIKE 'pattern%'      -- Starts with pattern
LIKE '%pattern'      -- Ends with pattern
LIKE '_pattern'      -- Single character wildcard

-- Range and list
BETWEEN value1 AND value2
IN (value1, value2, value3)
NOT IN (value1, value2)

-- Null checks
IS NULL
IS NOT NULL
```

### Examples
```sql
-- Basic filtering
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM employees 
WHERE department = 'IT' AND salary BETWEEN 40000 AND 80000;

-- Pattern matching
SELECT * FROM employees WHERE first_name LIKE 'J%';

-- Null handling
SELECT * FROM employees WHERE phone IS NOT NULL;
```

## Sorting & Grouping

### ORDER BY
```sql
-- Single column
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple columns
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

### GROUP BY & HAVING
```sql
-- Basic grouping
SELECT department, COUNT(*) as employee_count
FROM employees
GROUP BY department;

-- Grouping with conditions
SELECT department, AVG(salary) as avg_salary
FROM employees
WHERE salary > 30000
GROUP BY department
HAVING AVG(salary) > 50000;
```

## Joins

### Types of Joins
```sql
-- INNER JOIN (only matching records)
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- LEFT JOIN (all records from left table)
SELECT e.first_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- RIGHT JOIN (all records from right table)
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;

-- FULL OUTER JOIN (all records from both tables)
SELECT e.first_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;

-- CROSS JOIN (Cartesian product)
SELECT e.first_name, d.department_name
FROM employees e
CROSS JOIN departments d;
```

### Self Join
```sql
-- Find employees and their managers
SELECT e1.first_name as employee, e2.first_name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

## Subqueries

### Types of Subqueries
```sql
-- Scalar subquery (returns single value)
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery
SELECT * FROM employees e1
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e2.department_id = e1.department_id
);

-- Subquery with IN
SELECT * FROM employees
WHERE department_id IN (
    SELECT id FROM departments WHERE location = 'New York'
);

-- Subquery with EXISTS
SELECT * FROM employees e
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.employee_id = e.id
);
```

## Data Modification

### INSERT
```sql
-- Insert single row
INSERT INTO employees (first_name, last_name, salary, department_id)
VALUES ('John', 'Doe', 55000, 1);

-- Insert multiple rows
INSERT INTO employees (first_name, last_name, salary, department_id)
VALUES 
    ('Jane', 'Smith', 60000, 2),
    ('Bob', 'Johnson', 45000, 1);

-- Insert from another table
INSERT INTO archived_employees
SELECT * FROM employees WHERE hire_date < '2020-01-01';
```

### UPDATE
```sql
-- Update single record
UPDATE employees 
SET salary = 65000 
WHERE id = 1;

-- Update multiple records
UPDATE employees 
SET salary = salary * 1.1 
WHERE department_id = 2;

-- Update with JOIN
UPDATE employees e
SET salary = salary * 1.05
FROM departments d
WHERE e.department_id = d.id AND d.name = 'IT';
```

### DELETE
```sql
-- Delete specific records
DELETE FROM employees WHERE id = 1;

-- Delete with condition
DELETE FROM employees WHERE hire_date < '2015-01-01';

-- Delete all records (but keep table structure)
DELETE FROM employees;
```

## Table Operations

### CREATE TABLE
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2) DEFAULT 0,
    hire_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

### ALTER TABLE
```sql
-- Add column
ALTER TABLE employees ADD COLUMN phone VARCHAR(15);

-- Modify column
ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12,2);

-- Drop column
ALTER TABLE employees DROP COLUMN phone;

-- Add constraint
ALTER TABLE employees ADD CONSTRAINT fk_dept 
FOREIGN KEY (department_id) REFERENCES departments(id);
```

### DROP TABLE
```sql
DROP TABLE employees;
```

## Functions

### Aggregate Functions
```sql
COUNT(*)            -- Count all rows
COUNT(column)       -- Count non-null values
SUM(column)         -- Sum of values
AVG(column)         -- Average value
MAX(column)         -- Maximum value
MIN(column)         -- Minimum value
```

### String Functions
```sql
CONCAT(str1, str2)      -- Concatenate strings
UPPER(string)           -- Convert to uppercase
LOWER(string)           -- Convert to lowercase
LENGTH(string)          -- String length
SUBSTRING(str, pos, len) -- Extract substring
TRIM(string)            -- Remove leading/trailing spaces
REPLACE(str, old, new)  -- Replace text
```

### Date Functions
```sql
NOW()                   -- Current date and time
CURDATE()              -- Current date
YEAR(date)             -- Extract year
MONTH(date)            -- Extract month
DAY(date)              -- Extract day
DATEDIFF(date1, date2) -- Difference in days
DATE_ADD(date, INTERVAL value unit) -- Add time interval
```

### Mathematical Functions
```sql
ROUND(number, decimals) -- Round number
CEIL(number)           -- Round up
FLOOR(number)          -- Round down
ABS(number)            -- Absolute value
POWER(base, exponent)  -- Power function
SQRT(number)           -- Square root
```

## Advanced Concepts

### Window Functions
```sql
-- Row number
SELECT first_name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- Ranking
SELECT first_name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;

-- Running totals
SELECT first_name, salary,
       SUM(salary) OVER (ORDER BY hire_date) as running_total
FROM employees;

-- Partition by
SELECT first_name, department_id, salary,
       AVG(salary) OVER (PARTITION BY department_id) as dept_avg
FROM employees;
```

### Common Table Expressions (CTE)
```sql
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 70000
),
department_stats AS (
    SELECT department_id, COUNT(*) as emp_count
    FROM high_earners
    GROUP BY department_id
)
SELECT * FROM department_stats;
```

### CASE Statements
```sql
SELECT first_name, salary,
    CASE 
        WHEN salary < 40000 THEN 'Low'
        WHEN salary BETWEEN 40000 AND 70000 THEN 'Medium'
        ELSE 'High'
    END as salary_category
FROM employees;
```

### Indexes
```sql
-- Create index
CREATE INDEX idx_employee_lastname ON employees(last_name);

-- Composite index
CREATE INDEX idx_dept_salary ON employees(department_id, salary);

-- Unique index
CREATE UNIQUE INDEX idx_employee_email ON employees(email);

-- Drop index
DROP INDEX idx_employee_lastname;
```

### Views
```sql
-- Create view
CREATE VIEW employee_summary AS
SELECT e.first_name, e.last_name, d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Use view
SELECT * FROM employee_summary WHERE salary > 50000;

-- Drop view
DROP VIEW employee_summary;
```

### Transactions
```sql
-- Start transaction
BEGIN TRANSACTION;

-- Perform operations
UPDATE employees SET salary = salary * 1.1 WHERE department_id = 1;
INSERT INTO audit_log (action, table_name) VALUES ('salary_update', 'employees');

-- Commit or rollback
COMMIT;        -- Save changes
-- OR
ROLLBACK;      -- Undo changes
```

## Best Practices

1. **Use meaningful table and column names**
2. **Always specify column names in INSERT statements**
3. **Use appropriate data types and constraints**
4. **Create indexes on frequently queried columns**
5. **Use JOINs instead of subqueries when possible for better performance**
6. **Avoid SELECT * in production code**
7. **Use parameterized queries to prevent SQL injection**
8. **Normalize your database design**
9. **Use transactions for data consistency**
10. **Regular backups and maintenance**