# SQL Interview Questions & Answers

## Table of Contents
1. [Basic Level Questions](#basic-level-questions)
2. [Intermediate Level Questions](#intermediate-level-questions)
3. [Advanced Level Questions](#advanced-level-questions)
4. [Practical Coding Challenges](#practical-coding-challenges)
5. [Database Design Questions](#database-design-questions)
6. [Performance & Optimization](#performance--optimization)

---

## Basic Level Questions

### 1. What is SQL and what are its main components?
**Answer:** SQL (Structured Query Language) is a standard language for managing relational databases. Its main components are:
- **DDL (Data Definition Language)**: CREATE, ALTER, DROP, TRUNCATE
- **DML (Data Manipulation Language)**: SELECT, INSERT, UPDATE, DELETE
- **DCL (Data Control Language)**: GRANT, REVOKE
- **TCL (Transaction Control Language)**: COMMIT, ROLLBACK, SAVEPOINT

### 2. What's the difference between DELETE, DROP, and TRUNCATE?
**Answer:**
- **DELETE**: Removes rows from a table based on conditions. Can be rolled back. Triggers fire.
- **DROP**: Removes the entire table structure and data. Cannot be rolled back.
- **TRUNCATE**: Removes all rows from a table quickly. Cannot be rolled back. Triggers don't fire.

### 3. What are Primary Key and Foreign Key?
**Answer:**
- **Primary Key**: Uniquely identifies each row in a table. Cannot be NULL. Only one per table.
- **Foreign Key**: Links two tables together. References the primary key of another table. Can have duplicates and NULLs.

### 4. What's the difference between INNER JOIN and LEFT JOIN?
**Answer:**
- **INNER JOIN**: Returns only matching records from both tables
- **LEFT JOIN**: Returns all records from the left table and matching records from the right table. Non-matching right records show as NULL.

```sql
-- INNER JOIN
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

### 5. What is a UNIQUE constraint?
**Answer:** UNIQUE constraint ensures that all values in a column are different. Unlike PRIMARY KEY, a table can have multiple UNIQUE constraints, and UNIQUE columns can contain NULL values (but only one NULL per column).

### 6. What's the difference between WHERE and HAVING?
**Answer:**
- **WHERE**: Filters rows before grouping. Cannot use aggregate functions.
- **HAVING**: Filters groups after GROUP BY. Can use aggregate functions.

```sql
-- WHERE (filters rows)
SELECT * FROM employees WHERE salary > 50000;

-- HAVING (filters groups)
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 60000;
```

---

## Intermediate Level Questions

### 7. Explain different types of JOINs with examples
**Answer:**
```sql
-- Sample tables
Employees: id, name, dept_id
Departments: id, dept_name

-- INNER JOIN - only matching records
SELECT e.name, d.dept_name
FROM employees e INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN - all from left, matching from right
SELECT e.name, d.dept_name
FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;

-- RIGHT JOIN - all from right, matching from left
SELECT e.name, d.dept_name
FROM employees e RIGHT JOIN departments d ON e.dept_id = d.id;

-- FULL OUTER JOIN - all records from both tables
SELECT e.name, d.dept_name
FROM employees e FULL OUTER JOIN departments d ON e.dept_id = d.id;

-- CROSS JOIN - Cartesian product
SELECT e.name, d.dept_name
FROM employees e CROSS JOIN departments d;
```

### 8. What are Subqueries? Types of subqueries?
**Answer:** A subquery is a query nested inside another query.

**Types:**
1. **Scalar Subquery**: Returns single value
2. **Row Subquery**: Returns single row
3. **Column Subquery**: Returns single column
4. **Table Subquery**: Returns multiple rows and columns

```sql
-- Scalar subquery
SELECT * FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery
SELECT * FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 
                WHERE e2.dept_id = e1.dept_id);

-- Subquery with EXISTS
SELECT * FROM employees e
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.emp_id = e.id);
```

### 9. What are Window Functions?
**Answer:** Window functions perform calculations across a set of rows related to the current row without collapsing the result set.

```sql
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,
       RANK() OVER (ORDER BY salary DESC) as rank_val,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank_val
FROM employees;

-- Running totals
SELECT name, salary,
       SUM(salary) OVER (ORDER BY hire_date) as running_total
FROM employees;

-- Partition by department
SELECT name, dept_id, salary,
       AVG(salary) OVER (PARTITION BY dept_id) as dept_avg_salary
FROM employees;
```

### 10. What's the difference between RANK() and DENSE_RANK()?
**Answer:**
- **RANK()**: Leaves gaps in ranking after ties (1, 2, 2, 4, 5)
- **DENSE_RANK()**: No gaps in ranking after ties (1, 2, 2, 3, 4)

### 11. What are CTEs (Common Table Expressions)?
**Answer:** CTEs are temporary named result sets that exist within the scope of a single statement.

```sql
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 80000
),
dept_summary AS (
    SELECT dept_id, COUNT(*) as count, AVG(salary) as avg_sal
    FROM high_earners
    GROUP BY dept_id
)
SELECT * FROM dept_summary WHERE count > 5;
```

### 12. Explain CASE statement with example
**Answer:**
```sql
SELECT name, salary,
    CASE 
        WHEN salary < 40000 THEN 'Low'
        WHEN salary BETWEEN 40000 AND 80000 THEN 'Medium'
        WHEN salary > 80000 THEN 'High'
        ELSE 'Unknown'
    END as salary_grade
FROM employees;

-- Simple CASE
SELECT name,
    CASE dept_id
        WHEN 1 THEN 'HR'
        WHEN 2 THEN 'IT'
        WHEN 3 THEN 'Finance'
        ELSE 'Other'
    END as department
FROM employees;
```

---

## Advanced Level Questions

### 13. What are Indexes? Types of Indexes?
**Answer:** Indexes are database objects that improve query performance by creating shortcuts to data.

**Types:**
- **Clustered Index**: Physically orders table data. One per table.
- **Non-Clustered Index**: Logical ordering. Multiple per table.
- **Unique Index**: Ensures uniqueness
- **Composite Index**: Multiple columns
- **Partial Index**: Subset of rows

```sql
-- Create indexes
CREATE INDEX idx_employee_name ON employees(last_name);
CREATE UNIQUE INDEX idx_employee_email ON employees(email);
CREATE INDEX idx_composite ON employees(dept_id, salary);
```

### 14. What is Database Normalization? Explain Normal Forms.
**Answer:** Normalization eliminates data redundancy and ensures data integrity.

**Normal Forms:**
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies
- **3NF**: 2NF + no transitive dependencies
- **BCNF**: 3NF + every determinant is a candidate key

### 15. What are Triggers? Types of Triggers?
**Answer:** Triggers are special stored procedures that automatically execute in response to database events.

**Types:**
- **BEFORE Triggers**: Execute before the triggering event
- **AFTER Triggers**: Execute after the triggering event
- **INSTEAD OF Triggers**: Replace the triggering event (mainly for views)

```sql
CREATE TRIGGER audit_employee_changes
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (emp_id, old_salary, new_salary, change_date)
    VALUES (NEW.id, OLD.salary, NEW.salary, NOW());
END;
```

### 16. Explain ACID Properties
**Answer:**
- **Atomicity**: Transaction is all-or-nothing
- **Consistency**: Database remains in valid state
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed changes are permanent

### 17. What are Views? Advantages and Disadvantages?
**Answer:** Views are virtual tables based on SQL queries.

**Advantages:**
- Security (hide sensitive columns)
- Simplify complex queries
- Data abstraction
- Consistent interface

**Disadvantages:**
- Performance overhead
- Limited DML operations
- Dependency management

```sql
CREATE VIEW employee_summary AS
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE e.active = 1;
```

---

## Practical Coding Challenges

### 18. Find the second highest salary
```sql
-- Method 1: Using subquery
SELECT MAX(salary) as second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 2: Using ROW_NUMBER()
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 2;

-- Method 3: Using LIMIT/OFFSET
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

### 19. Find employees earning more than their manager
```sql
SELECT e1.name as employee, e1.salary as emp_salary,
       e2.name as manager, e2.salary as mgr_salary
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.id
WHERE e1.salary > e2.salary;
```

### 20. Find departments with no employees
```sql
SELECT d.dept_name
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id
WHERE e.dept_id IS NULL;

-- Alternative using NOT EXISTS
SELECT dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1 FROM employees e WHERE e.dept_id = d.id
);
```

### 21. Find running total of salaries
```sql
SELECT name, salary,
       SUM(salary) OVER (ORDER BY hire_date ROWS UNBOUNDED PRECEDING) as running_total
FROM employees
ORDER BY hire_date;
```

### 22. Find top 3 earners in each department
```sql
SELECT dept_id, name, salary
FROM (
    SELECT dept_id, name, salary,
           ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn <= 3;
```

### 23. Find employees hired in last 30 days
```sql
SELECT name, hire_date
FROM employees
WHERE hire_date >= DATEADD(day, -30, GETDATE())  -- SQL Server
-- WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)  -- MySQL
-- WHERE hire_date >= CURRENT_DATE - INTERVAL '30 days'     -- PostgreSQL
```

### 24. Find duplicate records
```sql
-- Find duplicate emails
SELECT email, COUNT(*) as count
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;

-- Delete duplicates keeping one record
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as rn
    FROM employees
)
DELETE FROM CTE WHERE rn > 1;
```

### 25. Pivot data example
```sql
-- Convert rows to columns
SELECT 
    SUM(CASE WHEN dept_id = 1 THEN salary ELSE 0 END) as HR_Total,
    SUM(CASE WHEN dept_id = 2 THEN salary ELSE 0 END) as IT_Total,
    SUM(CASE WHEN dept_id = 3 THEN salary ELSE 0 END) as Finance_Total
FROM employees;
```

---

## Database Design Questions

### 26. Design a database for a library management system
```sql
-- Books table
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(13) UNIQUE,
    publication_year INT,
    category_id INT,
    total_copies INT DEFAULT 1
);

-- Members table
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address TEXT,
    membership_date DATE,
    status ENUM('Active', 'Inactive') DEFAULT 'Active'
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    issue_date DATE,
    due_date DATE,
    return_date DATE,
    fine_amount DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
```

### 27. Design tables for an e-commerce system
```sql
-- Users table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled'),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Order items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## Performance & Optimization

### 28. How would you optimize a slow query?
**Answer:**
1. **Analyze execution plan**
2. **Add appropriate indexes**
3. **Rewrite subqueries as JOINs**
4. **Use LIMIT to reduce result set**
5. **Optimize WHERE conditions**
6. **Consider partitioning for large tables**
7. **Update table statistics**

### 29. When would you use a stored procedure vs a view?
**Answer:**
- **Stored Procedure**: Complex business logic, multiple operations, parameters needed
- **View**: Simplify complex queries, provide security layer, consistent data access

### 30. Explain query execution order
**Answer:**
```sql
-- SQL Query Order
SELECT column_list        -- 5
FROM table_name          -- 1
WHERE condition          -- 2
GROUP BY column_list     -- 3
HAVING condition         -- 4
ORDER BY column_list     -- 6
LIMIT number;            -- 7
```

### 31. What is a deadlock and how to prevent it?
**Answer:** A deadlock occurs when two or more transactions wait for each other indefinitely.

**Prevention:**
- Access tables in consistent order
- Keep transactions short
- Use appropriate isolation levels
- Implement timeout mechanisms
- Use proper indexing

### 32. Explain different isolation levels
**Answer:**
- **READ UNCOMMITTED**: Lowest isolation, allows dirty reads
- **READ COMMITTED**: Prevents dirty reads, allows non-repeatable reads
- **REPEATABLE READ**: Prevents dirty and non-repeatable reads, allows phantom reads
- **SERIALIZABLE**: Highest isolation, prevents all phenomena

---

## Quick Fire Questions

### 33. What's the difference between UNION and UNION ALL?
**Answer:** UNION removes duplicates and sorts results. UNION ALL keeps duplicates and doesn't sort (faster).

### 34. What is a Composite Key?
**Answer:** A primary key consisting of multiple columns that together uniquely identify a row.

### 35. What's the difference between Clustered and Non-Clustered Index?
**Answer:** Clustered index physically orders table data (one per table). Non-clustered index creates separate structure pointing to data rows (multiple allowed).

### 36. What is Referential Integrity?
**Answer:** Ensures relationships between tables remain consistent. Foreign key values must exist in referenced table or be NULL.

### 37. What are Aggregate Functions?
**Answer:** Functions that perform calculations on multiple rows: COUNT(), SUM(), AVG(), MAX(), MIN().

### 38. What is the purpose of GROUP BY?
**Answer:** Groups rows with same values in specified columns, typically used with aggregate functions.

### 39. Can you use aggregate functions in WHERE clause?
**Answer:** No, use HAVING clause instead. WHERE filters rows before grouping, HAVING filters groups after aggregation.

### 40. What is the difference between CHAR and VARCHAR?
**Answer:** CHAR is fixed-length (padded with spaces), VARCHAR is variable-length (uses only needed space).

---

## Sample Database for Practice

```sql
-- Create sample tables for practice
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10,2),
    dept_id INT,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- Sample data
INSERT INTO departments VALUES 
(1, 'Human Resources', 'New York'),
(2, 'Information Technology', 'San Francisco'),
(3, 'Finance', 'Chicago'),
(4, 'Marketing', 'Los Angeles');

INSERT INTO employees VALUES 
(1, 'John', 'Doe', 'john.doe@company.com', '2020-01-15', 75000, 2, NULL),
(2, 'Jane', 'Smith', 'jane.smith@company.com', '2019-03-20', 85000, 2, 1),
(3, 'Bob', 'Johnson', 'bob.johnson@company.com', '2021-06-10', 65000, 1, NULL),
(4, 'Alice', 'Brown', 'alice.brown@company.com', '2020-09-05', 70000, 3, NULL);
```

## Tips for SQL Interviews

1. **Understand the problem completely** before writing queries
2. **Think about edge cases** (NULL values, empty results)
3. **Optimize for readability** first, then performance
4. **Explain your approach** and reasoning
5. **Test your queries** mentally with sample data
6. **Know your database system** specifics (MySQL, PostgreSQL, SQL Server)
7. **Practice on real datasets** and coding platforms
8. **Be familiar with execution plans** and query optimization