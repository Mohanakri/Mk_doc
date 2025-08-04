# Confusing Things in SQL - A Clear Guide

## Table of Contents
1. [NULL Handling - The Biggest Confusion](#null-handling---the-biggest-confusion)
2. [JOINs and Their Unexpected Results](#joins-and-their-unexpected-results)
3. [WHERE vs HAVING - When to Use What](#where-vs-having---when-to-use-what)
4. [GROUP BY Rules and Gotchas](#group-by-rules-and-gotchas)
5. [Subqueries vs EXISTS vs IN](#subqueries-vs-exists-vs-in)
6. [Window Functions Confusion](#window-functions-confusion)
7. [UNION vs UNION ALL vs INTERSECT](#union-vs-union-all-vs-intersect)
8. [Date and Time Handling](#date-and-time-handling)
9. [String Comparisons and Collations](#string-comparisons-and-collations)
10. [Aggregate Functions Behavior](#aggregate-functions-behavior)
11. [CASE Statement Pitfalls](#case-statement-pitfalls)
12. [Database-Specific Differences](#database-specific-differences)

---

## NULL Handling - The Biggest Confusion

### The Three-Valued Logic Problem
SQL uses three-valued logic: TRUE, FALSE, and UNKNOWN (NULL)

```sql
-- These might not work as expected!
SELECT * FROM employees WHERE salary = NULL;        -- Returns nothing!
SELECT * FROM employees WHERE salary != NULL;       -- Returns nothing!
SELECT * FROM employees WHERE salary <> NULL;       -- Returns nothing!

-- Correct way
SELECT * FROM employees WHERE salary IS NULL;
SELECT * FROM employees WHERE salary IS NOT NULL;
```

### NULL in Arithmetic Operations
```sql
-- All these return NULL!
SELECT 5 + NULL;      -- NULL
SELECT 5 * NULL;      -- NULL  
SELECT NULL / 0;      -- NULL (not error!)

-- Example with employee data
SELECT name, salary + bonus as total_compensation
FROM employees;
-- If bonus is NULL, total_compensation will be NULL even if salary has value!

-- Fix with COALESCE or ISNULL
SELECT name, salary + COALESCE(bonus, 0) as total_compensation
FROM employees;
```

### NULL in Comparisons
```sql
-- Confusing behavior
SELECT * FROM employees WHERE salary > 50000;  -- Excludes NULL salaries
SELECT * FROM employees WHERE salary <= 50000; -- Also excludes NULL salaries!

-- NULL comparisons always return UNKNOWN
SELECT 
    NULL = NULL,     -- NULL (not TRUE!)
    NULL <> NULL,    -- NULL (not FALSE!)
    NULL > 5,        -- NULL
    NULL < 5;        -- NULL
```

### NULL in Aggregations
```sql
-- COUNT behaves differently with NULLs
SELECT 
    COUNT(*),           -- Counts all rows including NULLs
    COUNT(salary),      -- Counts only non-NULL salaries
    COUNT(DISTINCT salary), -- Counts distinct non-NULL salaries
    AVG(salary),        -- Averages only non-NULL values
    SUM(salary)         -- Sums only non-NULL values
FROM employees;

-- Empty result sets
SELECT AVG(salary) FROM employees WHERE 1=0;  -- Returns NULL, not 0!
SELECT COUNT(*) FROM employees WHERE 1=0;     -- Returns 0
```

### NULL in ORDER BY
```sql
-- NULL sorting behavior varies by database
SELECT * FROM employees ORDER BY bonus;
-- PostgreSQL: NULLs last by default
-- MySQL: NULLs first by default
-- SQL Server: NULLs first by default

-- Explicit control
SELECT * FROM employees ORDER BY bonus NULLS FIRST;
SELECT * FROM employees ORDER BY bonus NULLS LAST;
```

---

## JOINs and Their Unexpected Results

### The Dreaded Cartesian Product
```sql
-- Accidentally creates Cartesian product!
SELECT e.name, d.dept_name
FROM employees e, departments d;  -- Missing JOIN condition!

-- This returns employees × departments rows
-- 10 employees × 5 departments = 50 rows!
```

### LEFT JOIN Confusion
```sql
-- Setup
Employees: id=1,name='John',dept_id=NULL
          id=2,name='Jane',dept_id=1
Departments: id=1,name='IT'

-- This query
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
WHERE d.dept_name = 'IT';

-- Expected: John (with NULL dept), Jane (with IT)
-- Actual: Only Jane! 
-- Why? WHERE clause filters out NULLs from LEFT JOIN
```

### RIGHT JOIN Rarely Used (and Confusing)
```sql
-- These are equivalent but RIGHT JOIN is confusing
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;

-- Better: Use LEFT JOIN with tables swapped
SELECT e.name, d.dept_name
FROM departments d
LEFT JOIN employees e ON e.dept_id = d.id;
```

### FULL OUTER JOIN Pitfalls
```sql
-- Returns all employees and all departments
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.id;

-- Results in:
-- John, NULL (employee without department)
-- Jane, IT   (matched)
-- NULL, HR   (department without employees)
```

### Multiple JOINs Order Matters
```sql
-- These can give different results!
SELECT *
FROM a
LEFT JOIN b ON a.id = b.a_id
LEFT JOIN c ON b.id = c.b_id;  -- c joins to b

SELECT *
FROM a
LEFT JOIN b ON a.id = b.a_id
LEFT JOIN c ON a.id = c.a_id;  -- c joins to a
```

---

## WHERE vs HAVING - When to Use What

### The Fundamental Difference
```sql
-- WHERE filters ROWS before grouping
SELECT dept_id, AVG(salary)
FROM employees
WHERE salary > 50000  -- Filters individual employees first
GROUP BY dept_id;

-- HAVING filters GROUPS after grouping
SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 60000;  -- Filters departments by average
```

### Common Mistakes
```sql
-- ❌ WRONG: Can't use aggregate in WHERE
SELECT dept_id, AVG(salary)
FROM employees
WHERE AVG(salary) > 60000  -- ERROR!
GROUP BY dept_id;

-- ❌ WRONG: Using HAVING without GROUP BY (works but inefficient)
SELECT * FROM employees
HAVING salary > 50000;  -- Should use WHERE instead

-- ✅ CORRECT: Combine both
SELECT dept_id, AVG(salary)
FROM employees
WHERE hire_date > '2020-01-01'  -- Filter rows first
GROUP BY dept_id
HAVING COUNT(*) > 5;            -- Filter groups after
```

---

## GROUP BY Rules and Gotchas

### The SELECT and GROUP BY Rule
```sql
-- ❌ WRONG: All non-aggregate columns must be in GROUP BY
SELECT dept_id, name, AVG(salary)  -- name not in GROUP BY!
FROM employees
GROUP BY dept_id;

-- ✅ CORRECT: Options
SELECT dept_id, AVG(salary)       -- Only aggregates and grouped columns
FROM employees
GROUP BY dept_id;

SELECT dept_id, name, salary      -- All columns in GROUP BY
FROM employees
GROUP BY dept_id, name, salary;
```

### GROUP BY with NULLs
```sql
-- NULLs are treated as a single group
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id;

-- Results:
-- 1     5    (dept_id = 1)
-- 2     3    (dept_id = 2)  
-- NULL  2    (dept_id is NULL - all NULLs grouped together!)
```

### GROUP BY Order Doesn't Matter (Usually)
```sql
-- These are equivalent
GROUP BY dept_id, salary
GROUP BY salary, dept_id

-- But in some databases, GROUP BY affects ORDER BY
SELECT dept_id, COUNT(*)
FROM employees  
GROUP BY dept_id;
-- Might be ordered by dept_id in some databases
```

---

## Subqueries vs EXISTS vs IN

### IN vs EXISTS Performance
```sql
-- IN - transfers all values
SELECT * FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE location = 'NYC');

-- EXISTS - stops at first match (often faster)
SELECT * FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d 
              WHERE d.id = e.dept_id AND d.location = 'NYC');
```

### IN with NULLs - The Nightmare
```sql
-- Setup: departments has values (1, 2, NULL)
SELECT * FROM employees WHERE dept_id IN (1, 2, NULL);
-- Returns employees with dept_id 1 or 2, but NOT NULL!

SELECT * FROM employees WHERE dept_id NOT IN (1, 2, NULL);
-- Returns NOTHING! Because NULL comparison always returns UNKNOWN

-- Safer alternatives
SELECT * FROM employees WHERE dept_id IN (1, 2) OR dept_id IS NULL;
SELECT * FROM employees WHERE COALESCE(dept_id, -1) NOT IN (1, 2, -1);
```

### Correlated vs Non-Correlated Subqueries
```sql
-- Non-correlated (runs once)
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated (runs for each row - slower!)
SELECT * FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 
                WHERE e2.dept_id = e1.dept_id);
```

---

## Window Functions Confusion

### ROW_NUMBER vs RANK vs DENSE_RANK
```sql
-- Sample data with ties
Salaries: 100, 90, 90, 80, 70

SELECT salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,  -- 1,2,3,4,5
    RANK() OVER (ORDER BY salary DESC) as rank_val,       -- 1,2,2,4,5
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank -- 1,2,2,3,4
FROM employees;
```

### PARTITION BY Confusion
```sql
-- This partitions by department, not filters by it!
SELECT name, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) as dept_rank
FROM employees;
-- Still returns ALL employees, but ranks within each department
```

### Frame Specifications (ROWS vs RANGE)
```sql
-- ROWS - physical rows
SELECT name, salary,
    SUM(salary) OVER (ORDER BY hire_date ROWS 2 PRECEDING) as sum_3_rows
FROM employees;

-- RANGE - logical range (same values grouped)
SELECT name, salary,
    SUM(salary) OVER (ORDER BY salary RANGE BETWEEN 1000 PRECEDING AND CURRENT ROW)
FROM employees;
```

---

## UNION vs UNION ALL vs INTERSECT

### UNION Removes Duplicates (And Sorts!)
```sql
-- UNION removes duplicates and may sort results
SELECT name FROM employees WHERE dept_id = 1
UNION
SELECT name FROM employees WHERE salary > 50000;

-- UNION ALL keeps duplicates (faster)
SELECT name FROM employees WHERE dept_id = 1
UNION ALL
SELECT name FROM employees WHERE salary > 50000;
```

### Column Compatibility Rules
```sql
-- ❌ WRONG: Different number of columns
SELECT name, salary FROM employees
UNION
SELECT dept_name FROM departments;  -- ERROR!

-- ❌ WRONG: Incompatible data types
SELECT name FROM employees      -- VARCHAR
UNION
SELECT salary FROM employees;   -- DECIMAL - might cause implicit conversion
```

### INTERSECT and EXCEPT Confusion
```sql
-- INTERSECT - common rows
SELECT name FROM employees WHERE dept_id = 1
INTERSECT
SELECT name FROM employees WHERE salary > 50000;
-- Returns names that are in BOTH result sets

-- EXCEPT/MINUS - difference
SELECT name FROM employees WHERE dept_id = 1
EXCEPT
SELECT name FROM employees WHERE salary > 50000;
-- Returns names in first set but NOT in second set
```

---

## Date and Time Handling

### Date Arithmetic Confusion
```sql
-- Different databases, different syntax
-- MySQL
SELECT DATE_ADD(hire_date, INTERVAL 30 DAY) FROM employees;

-- PostgreSQL
SELECT hire_date + INTERVAL '30 days' FROM employees;

-- SQL Server
SELECT DATEADD(day, 30, hire_date) FROM employees;
```

### Date Comparisons with Time
```sql
-- Dangerous! Time component matters
SELECT * FROM orders WHERE order_date = '2023-01-01';
-- Only matches '2023-01-01 00:00:00', not '2023-01-01 14:30:00'!

-- Better approaches
SELECT * FROM orders WHERE DATE(order_date) = '2023-01-01';
SELECT * FROM orders WHERE order_date >= '2023-01-01' 
                      AND order_date < '2023-01-02';
```

### Timezone Confusion
```sql
-- DATETIME vs TIMESTAMP behavior differs
-- DATETIME: No timezone conversion
-- TIMESTAMP: Converts based on timezone settings

-- Current time functions vary
SELECT NOW();           -- Current timestamp
SELECT CURRENT_DATE;    -- Current date only
SELECT CURRENT_TIME;    -- Current time only
```

---

## String Comparisons and Collations

### Case Sensitivity Varies
```sql
-- Might be case-sensitive or not depending on database/collation
SELECT * FROM users WHERE name = 'John';
SELECT * FROM users WHERE name = 'JOHN';
-- These might return different results!

-- Explicit case handling
SELECT * FROM users WHERE UPPER(name) = UPPER('John');
SELECT * FROM users WHERE LOWER(name) = 'john';
```

### LIKE Pattern Matching Gotchas
```sql
-- Underscore is a wildcard!
SELECT * FROM products WHERE code LIKE 'A_1';  
-- Matches 'A11', 'AB1', 'A@1', etc.

-- To match literal underscore
SELECT * FROM products WHERE code LIKE 'A\_1' ESCAPE '\';

-- Percent at the beginning kills performance
SELECT * FROM products WHERE name LIKE '%phone%';  -- Full table scan!
```

### Trailing Spaces
```sql
-- CHAR vs VARCHAR behavior with spaces
INSERT INTO test_table (char_col, varchar_col) 
VALUES ('hello   ', 'hello   ');

-- Comparisons might behave differently
SELECT * FROM test_table WHERE char_col = 'hello';     -- Might match
SELECT * FROM test_table WHERE varchar_col = 'hello';  -- Might not match
```

---

## Aggregate Functions Behavior

### COUNT Variations
```sql
SELECT 
    COUNT(*),           -- Counts all rows (including NULLs)
    COUNT(column),      -- Counts non-NULL values in column
    COUNT(DISTINCT column), -- Counts distinct non-NULL values
    COUNT(1),           -- Same as COUNT(*) - common confusion
    COUNT(0)            -- Also same as COUNT(*)
FROM table_name;
```

### MIN/MAX with Strings
```sql
-- MIN/MAX work on strings too (alphabetical order)
SELECT MIN(name), MAX(name) FROM employees;
-- Returns first and last names alphabetically

-- Date comparisons
SELECT MIN(hire_date), MAX(hire_date) FROM employees;
-- Returns earliest and latest dates
```

### GROUP_CONCAT/STRING_AGG Differences
```sql
-- MySQL
SELECT dept_id, GROUP_CONCAT(name) FROM employees GROUP BY dept_id;

-- PostgreSQL/SQL Server
SELECT dept_id, STRING_AGG(name, ', ') FROM employees GROUP BY dept_id;

-- Result ordering within groups
SELECT dept_id, GROUP_CONCAT(name ORDER BY salary DESC) 
FROM employees GROUP BY dept_id;
```

---

## CASE Statement Pitfalls

### CASE is an Expression, Not a Statement
```sql
-- ❌ WRONG: Treating CASE like IF-ELSE
SELECT name,
CASE 
    WHEN salary > 80000 
        UPDATE employees SET bonus = 5000;  -- ERROR!
    ELSE 
        UPDATE employees SET bonus = 1000;  -- ERROR!
END
FROM employees;

-- ✅ CORRECT: CASE returns a value
SELECT name,
CASE 
    WHEN salary > 80000 THEN 'High'
    WHEN salary > 50000 THEN 'Medium'
    ELSE 'Low'
END as salary_grade
FROM employees;
```

### Data Type Consistency in CASE
```sql
-- All WHEN branches must return compatible types
SELECT name,
CASE dept_id
    WHEN 1 THEN 'HR'
    WHEN 2 THEN 'IT' 
    ELSE dept_id     -- ERROR: mixing VARCHAR and INT
END
FROM employees;

-- Fix with CAST
SELECT name,
CASE dept_id
    WHEN 1 THEN 'HR'
    WHEN 2 THEN 'IT'
    ELSE CAST(dept_id AS VARCHAR)
END
FROM employees;
```

### NULL in CASE Conditions
```sql
-- CASE doesn't handle NULL the way you might expect
SELECT name,
CASE dept_id
    WHEN NULL THEN 'No Department'  -- This never matches!
    ELSE 'Has Department'
END
FROM employees;

-- Correct way
SELECT name,
CASE 
    WHEN dept_id IS NULL THEN 'No Department'
    ELSE 'Has Department'
END
FROM employees;
```

---

## Database-Specific Differences

### Limit/Offset Syntax
```sql
-- MySQL, PostgreSQL
SELECT * FROM employees LIMIT 10 OFFSET 20;

-- SQL Server (2012+)
SELECT * FROM employees ORDER BY id OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;

-- SQL Server (older)
SELECT TOP 10 * FROM employees WHERE id NOT IN (SELECT TOP 20 id FROM employees ORDER BY id) ORDER BY id;

-- Oracle
SELECT * FROM (
    SELECT rownum r, e.* FROM employees e WHERE rownum <= 30
) WHERE r > 20;
```

### String Concatenation
```sql
-- MySQL
SELECT CONCAT(first_name, ' ', last_name) FROM employees;

-- PostgreSQL, SQLite
SELECT first_name || ' ' || last_name FROM employees;

-- SQL Server
SELECT first_name + ' ' + last_name FROM employees;
-- Or: SELECT CONCAT(first_name, ' ', last_name) FROM employees;
```

### Date Functions
```sql
-- Current date/time
-- MySQL: NOW(), CURDATE(), CURTIME()
-- PostgreSQL: NOW(), CURRENT_DATE, CURRENT_TIME
-- SQL Server: GETDATE(), GETUTCDATE()
-- Oracle: SYSDATE, CURRENT_DATE

-- Date formatting
-- MySQL: DATE_FORMAT(date, '%Y-%m-%d')
-- PostgreSQL: TO_CHAR(date, 'YYYY-MM-DD')
-- SQL Server: FORMAT(date, 'yyyy-MM-dd')
```

### Auto-increment Columns
```sql
-- MySQL
CREATE TABLE test (id INT AUTO_INCREMENT PRIMARY KEY);

-- PostgreSQL
CREATE TABLE test (id SERIAL PRIMARY KEY);
-- Or: CREATE TABLE test (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY);

-- SQL Server
CREATE TABLE test (id INT IDENTITY(1,1) PRIMARY KEY);

-- Oracle
CREATE TABLE test (id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY);
```

---

## Pro Tips to Avoid Confusion

### 1. Always Be Explicit About NULLs
```sql
-- Instead of this ambiguous query
SELECT * FROM employees WHERE bonus != 1000;

-- Be explicit about NULL handling
SELECT * FROM employees 
WHERE (bonus != 1000 OR bonus IS NULL);
```

### 2. Use Table Aliases Consistently
```sql
-- Avoid ambiguity
SELECT e.name, d.name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

### 3. Parenthesize Complex Conditions
```sql
-- Unclear precedence
SELECT * FROM employees 
WHERE dept_id = 1 OR dept_id = 2 AND salary > 50000;

-- Clear with parentheses
SELECT * FROM employees 
WHERE (dept_id = 1 OR dept_id = 2) AND salary > 50000;
```

### 4. Test Edge Cases
Always test your queries with:
- Empty result sets
- NULL values
- Duplicate data
- Single row results
- Very large datasets

### 5. Use EXPLAIN/ANALYZE
Understand what your database is actually doing:
```sql
EXPLAIN SELECT * FROM employees WHERE name LIKE '%john%';
EXPLAIN ANALYZE SELECT * FROM employees e JOIN departments d ON e.dept_id = d.id;
```

### 6. Be Database-Aware
Know which database you're working with and its specific behaviors, especially for:
- NULL sorting
- String comparison rules
- Date/time handling
- Limit/offset syntax
- Data type behaviors

Remember: SQL might look simple, but the devil is in the details. When in doubt, test with sample data that includes edge cases!