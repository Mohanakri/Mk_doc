# SQL Complete Study Notes

## Table of Contents

1. [Introduction to SQL](#introduction-to-sql)
2. [Data Types](#data-types)
3. [DDL Commands](#ddl-commands)
4. [DML Commands](#dml-commands)
5. [DQL Commands](#dql-commands)
6. [Functions](#functions)
7. [Joins](#joins)
8. [Constraints](#constraints)
9. [Sub Queries](#sub-queries)
10. [Views](#views)
11. [Indexes](#indexes)
12. [Advanced Topics](#advanced-topics)

## Introduction to SQL

### What is SQL?
**SQL (Structured Query Language)** is a non-procedural language used to operate all relational database products.

### Types of Database Languages in Oracle
1. **SQL** - Structured Query Language (Non-procedural)
2. **PL/SQL** - Procedural Language extension of SQL
3. **Dynamic SQL** (Optional)

### SQL Sub-Languages
SQL is divided into 5 sub-languages:

| Sub-Language | Commands | Purpose |
|--------------|----------|---------|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE, RENAME | Define database structure |
| **DML** (Data Manipulation Language) | INSERT, UPDATE, DELETE, MERGE | Manipulate data |
| **DRL/DQL** (Data Retrieval/Query Language) | SELECT | Query data |
| **TCL** (Transaction Control Language) | COMMIT, ROLLBACK, SAVEPOINT | Control transactions |
| **DCL** (Data Control Language) | GRANT, REVOKE | Control access |

## Data Types

Oracle supports three main data types:

### 1. Number Data Type
```sql
-- Syntax: columnname NUMBER(precision, scale)
-- precision: total number of digits
-- scale: digits after decimal point

CREATE TABLE test(sno NUMBER(7,2));
INSERT INTO test VALUES(12345.67); -- Valid
INSERT INTO test VALUES(123456.7); -- Error: exceeds precision
```

### 2. Character Data Types

#### CHAR
- **Fixed-length** character data
- Maximum: **2000 bytes**
- **Blank padded** (fills remaining space with blanks)

```sql
columnname CHAR(size)
```

#### VARCHAR2
- **Variable-length** character data
- Maximum: **4000 bytes**
- **Not blank padded**

```sql
columnname VARCHAR2(maxsize)
```

### 3. Date Data Type
- Stores dates in Oracle date format
- Default format: **DD-MON-YY**

```sql
columnname DATE
```

## DDL Commands

### CREATE
Creates database objects like tables, views, sequences, indexes.

```sql
-- Basic syntax
CREATE TABLE tablename(
    column1 datatype(size),
    column2 datatype(size)
);

-- Example
CREATE TABLE emp(
    empno NUMBER(10),
    ename VARCHAR2(20),
    sal NUMBER(10,2),
    hiredate DATE
);
```

### ALTER
Modifies existing table structure.

```sql
-- Add column
ALTER TABLE tablename ADD (columnname datatype(size));

-- Modify column
ALTER TABLE tablename MODIFY (columnname datatype(size));

-- Drop column
ALTER TABLE tablename DROP COLUMN columnname;

-- Rename column (Oracle 9i+)
ALTER TABLE tablename RENAME COLUMN oldname TO newname;
```

### DROP
Removes database objects.

```sql
-- Drop table (Oracle 10g+ has recycle bin)
DROP TABLE tablename;

-- Drop permanently
DROP TABLE tablename PURGE;

-- Recover from recycle bin
FLASHBACK TABLE tablename TO BEFORE DROP;
```

### TRUNCATE
Permanently deletes all data from table.

```sql
TRUNCATE TABLE tablename;
```

!!! note "TRUNCATE vs DELETE"
    - **TRUNCATE**: Permanent deletion, cannot rollback, DDL command
    - **DELETE**: Can be rolled back, DML command

## DML Commands

### INSERT
Adds data to tables.

```sql
-- Method 1: Direct values
INSERT INTO tablename VALUES(value1, value2, ...);

-- Method 2: Using substitution operator
INSERT INTO tablename VALUES(&col1, '&col2');

-- Method 3: Specific columns
INSERT INTO tablename(col1, col2) VALUES(value1, value2);
```

### UPDATE
Modifies existing data.

```sql
UPDATE tablename 
SET columnname = newvalue 
WHERE condition;

-- Example
UPDATE emp SET sal = 5000 WHERE ename = 'SMITH';
```

### DELETE
Removes data from tables.

```sql
-- Delete specific rows
DELETE FROM tablename WHERE condition;

-- Delete all rows
DELETE FROM tablename;
```

## DQL Commands

### SELECT Statement Structure
```sql
SELECT column1, column2, ...
FROM tablename
WHERE condition
GROUP BY columnname
HAVING condition
ORDER BY columnname [ASC|DESC];
```

### WHERE Clause Operators

#### Arithmetic Operators
- `+`, `-`, `*`, `/`

#### Relational Operators
- `=`, `<`, `<=`, `>`, `>=`, `<>`, `!=`

#### Logical Operators
- `AND`, `OR`, `NOT`

#### Special Operators

##### IN Operator
```sql
SELECT * FROM emp WHERE deptno IN(10, 20, 30);
```

##### BETWEEN Operator
```sql
SELECT * FROM emp WHERE sal BETWEEN 2000 AND 5000;
```

##### LIKE Operator
- `%` - Group of characters
- `_` - Single character

```sql
-- Names starting with 'M'
SELECT * FROM emp WHERE ename LIKE 'M%';

-- Second letter is 'L'
SELECT * FROM emp WHERE ename LIKE '_L%';
```

##### IS NULL / IS NOT NULL
```sql
SELECT * FROM emp WHERE comm IS NULL;
SELECT * FROM emp WHERE comm IS NOT NULL;
```

## Functions

### Single Row Functions

#### Number Functions
```sql
-- ABS: Absolute value
SELECT ABS(-50) FROM DUAL; -- Returns 50

-- MOD: Remainder
SELECT MOD(10,5) FROM DUAL; -- Returns 0

-- ROUND: Rounding
SELECT ROUND(1.235, 2) FROM DUAL; -- Returns 1.24

-- TRUNC: Truncate
SELECT TRUNC(1.789, 2) FROM DUAL; -- Returns 1.78

-- GREATEST/LEAST
SELECT GREATEST(3,5,8,9) FROM DUAL; -- Returns 9
SELECT LEAST(3,5,8,9) FROM DUAL; -- Returns 3
```

#### Character Functions
```sql
-- Case conversion
SELECT UPPER('hello') FROM DUAL; -- HELLO
SELECT LOWER('HELLO') FROM DUAL; -- hello
SELECT INITCAP('hello world') FROM DUAL; -- Hello World

-- String manipulation
SELECT LENGTH('ABCDEF') FROM DUAL; -- 6
SELECT SUBSTR('ABCDEF', 2, 3) FROM DUAL; -- BCD
SELECT INSTR('ABCDEF', 'CD') FROM DUAL; -- 3

-- Padding
SELECT LPAD('ABC', 10, '#') FROM DUAL; -- #######ABC
SELECT RPAD('ABC', 10, '#') FROM DUAL; -- ABC#######

-- Trimming
SELECT LTRIM('XXABC', 'X') FROM DUAL; -- ABC
SELECT RTRIM('ABCXX', 'X') FROM DUAL; -- ABC
SELECT TRIM('X' FROM 'XABCX') FROM DUAL; -- ABC

-- Replace/Translate
SELECT REPLACE('HELLO', 'LL', 'XX') FROM DUAL; -- HEXXO
SELECT TRANSLATE('HELLO', 'ELO', '123') FROM DUAL; -- H1223
```

#### Date Functions
```sql
-- Current date
SELECT SYSDATE FROM DUAL;

-- Add months
SELECT ADD_MONTHS(SYSDATE, 6) FROM DUAL;

-- Last day of month
SELECT LAST_DAY(SYSDATE) FROM DUAL;

-- Next day
SELECT NEXT_DAY(SYSDATE, 'MONDAY') FROM DUAL;

-- Months between
SELECT MONTHS_BETWEEN(SYSDATE, hiredate) FROM emp;
```

#### Conversion Functions
```sql
-- TO_CHAR: Convert date/number to string
SELECT TO_CHAR(SYSDATE, 'DD/MM/YYYY') FROM DUAL;
SELECT TO_CHAR(1234, '9,999') FROM DUAL;

-- TO_DATE: Convert string to date
SELECT TO_DATE('15-JUN-05', 'DD-MON-YY') FROM DUAL;

-- TO_NUMBER: Convert string to number
SELECT TO_NUMBER('123.45') FROM DUAL;
```

### Group Functions
```sql
-- COUNT: Count rows
SELECT COUNT(*) FROM emp;
SELECT COUNT(comm) FROM emp; -- Excludes NULLs

-- SUM: Total
SELECT SUM(sal) FROM emp;

-- AVG: Average
SELECT AVG(sal) FROM emp;

-- MAX/MIN: Maximum/Minimum
SELECT MAX(sal) FROM emp;
SELECT MIN(sal) FROM emp;
```

### GROUP BY and HAVING
```sql
-- Group employees by department
SELECT deptno, COUNT(*), AVG(sal)
FROM emp
GROUP BY deptno;

-- Filter groups with HAVING
SELECT deptno, AVG(sal)
FROM emp
GROUP BY deptno
HAVING AVG(sal) > 2000;
```

!!! warning "GROUP BY Rules"
    - All non-aggregate columns in SELECT must be in GROUP BY
    - Cannot use GROUP BY with aggregate functions in WHERE clause
    - Use HAVING to filter groups

## Joins

### Types of Joins

#### 1. Equi Join (Inner Join)
```sql
-- Oracle 8i syntax
SELECT e.ename, e.sal, d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno;

-- Oracle 9i ANSI syntax
SELECT e.ename, e.sal, d.dname
FROM emp e JOIN dept d ON e.deptno = d.deptno;

-- Using clause (when column names are same)
SELECT ename, sal, dname
FROM emp JOIN dept USING(deptno);
```

#### 2. Outer Joins
```sql
-- Left Outer Join
SELECT e.ename, d.dname
FROM emp e LEFT OUTER JOIN dept d ON e.deptno = d.deptno;

-- Right Outer Join
SELECT e.ename, d.dname
FROM emp e RIGHT OUTER JOIN dept d ON e.deptno = d.deptno;

-- Full Outer Join
SELECT e.ename, d.dname
FROM emp e FULL OUTER JOIN dept d ON e.deptno = d.deptno;

-- Oracle 8i Outer Join (+)
SELECT e.ename, d.dname
FROM emp e, dept d
WHERE e.deptno(+) = d.deptno; -- Right outer join
```

#### 3. Self Join
```sql
-- Employee and their managers
SELECT e1.ename "Employee", e2.ename "Manager"
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno;
```

#### 4. Natural Join
```sql
-- Automatically joins on common columns
SELECT ename, sal, dname
FROM emp NATURAL JOIN dept;
```

## Constraints

Constraints prevent invalid data entry into tables.

### Types of Constraints

#### 1. NOT NULL
```sql
CREATE TABLE test(
    sno NUMBER(10) NOT NULL,
    name VARCHAR2(20)
);
```

#### 2. UNIQUE
```sql
-- Column level
CREATE TABLE test(
    sno NUMBER(10) UNIQUE,
    name VARCHAR2(20)
);

-- Table level
CREATE TABLE test(
    sno NUMBER(10),
    name VARCHAR2(20),
    UNIQUE(sno, name)
);
```

#### 3. PRIMARY KEY
```sql
-- Column level
CREATE TABLE test(
    sno NUMBER(10) PRIMARY KEY,
    name VARCHAR2(20)
);

-- Table level
CREATE TABLE test(
    sno NUMBER(10),
    name VARCHAR2(20),
    PRIMARY KEY(sno)
);

-- Composite primary key
CREATE TABLE test(
    sno NUMBER(10),
    name VARCHAR2(20),
    PRIMARY KEY(sno, name)
);
```

#### 4. FOREIGN KEY
```sql
-- Column level
CREATE TABLE child(
    sno NUMBER(10) REFERENCES parent(sno),
    name VARCHAR2(20)
);

-- Table level
CREATE TABLE child(
    sno NUMBER(10),
    name VARCHAR2(20),
    FOREIGN KEY(sno) REFERENCES parent(sno)
);

-- With CASCADE options
CREATE TABLE child(
    sno NUMBER(10) REFERENCES parent(sno) ON DELETE CASCADE,
    name VARCHAR2(20)
);

CREATE TABLE child(
    sno NUMBER(10) REFERENCES parent(sno) ON DELETE SET NULL,
    name VARCHAR2(20)
);
```

#### 5. CHECK
```sql
-- Column level
CREATE TABLE test(
    sal NUMBER(10) CHECK(sal > 5000),
    name VARCHAR2(20)
);

-- Table level
CREATE TABLE test(
    sal NUMBER(10),
    name VARCHAR2(20),
    CHECK(sal > 5000 AND name = UPPER(name))
);
```

### User-Defined Constraint Names
```sql
CREATE TABLE test(
    sno NUMBER(10) CONSTRAINT pk_test PRIMARY KEY,
    name VARCHAR2(20) CONSTRAINT nn_name NOT NULL
);
```

### Adding/Dropping Constraints
```sql
-- Add constraint
ALTER TABLE test ADD CONSTRAINT pk_test PRIMARY KEY(sno);

-- Drop constraint
ALTER TABLE test DROP CONSTRAINT pk_test;

-- Drop primary key with cascade
ALTER TABLE test DROP PRIMARY KEY CASCADE;
```

## Sub Queries

A query within another query.

### Types of Sub Queries

#### 1. Single Row Sub Query
```sql
-- Find employees with salary > average salary
SELECT * FROM emp 
WHERE sal > (SELECT AVG(sal) FROM emp);

-- Find employee in same department as SMITH
SELECT * FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'SMITH');
```

#### 2. Multiple Row Sub Query
```sql
-- Find employees with maximum salary in each department
SELECT * FROM emp 
WHERE sal IN (SELECT MAX(sal) FROM emp GROUP BY deptno);

-- Using ALL operator
SELECT * FROM emp 
WHERE sal > ALL (SELECT sal FROM emp WHERE job = 'CLERK');

-- Using ANY operator
SELECT * FROM emp 
WHERE sal > ANY (SELECT sal FROM emp WHERE job = 'CLERK');
```

#### 3. Multiple Column Sub Query
```sql
-- Find employees with same job and manager as SCOTT
SELECT * FROM emp 
WHERE (job, mgr) IN (SELECT job, mgr FROM emp WHERE ename = 'SCOTT');
```

#### 4. Correlated Sub Query
```sql
-- Find employees earning more than average in their department
SELECT * FROM emp e1 
WHERE sal > (SELECT AVG(sal) FROM emp e2 WHERE e2.deptno = e1.deptno);

-- Find second highest salary
SELECT * FROM emp e1 
WHERE 2 = (SELECT COUNT(DISTINCT sal) FROM emp e2 WHERE e2.sal >= e1.sal);
```

#### 5. EXISTS Operator
```sql
-- Find departments with employees
SELECT * FROM dept d 
WHERE EXISTS (SELECT 1 FROM emp WHERE deptno = d.deptno);

-- Find departments without employees
SELECT * FROM dept d 
WHERE NOT EXISTS (SELECT 1 FROM emp WHERE deptno = d.deptno);
```

### Analytical Functions
```sql
-- ROW_NUMBER: Assigns unique numbers
SELECT empno, ename, sal,
       ROW_NUMBER() OVER (ORDER BY sal DESC) as rn
FROM emp;

-- RANK: Assigns same rank for ties, skips next rank
SELECT empno, ename, sal,
       RANK() OVER (ORDER BY sal DESC) as rank
FROM emp;

-- DENSE_RANK: Assigns same rank for ties, doesn't skip
SELECT empno, ename, sal,
       DENSE_RANK() OVER (ORDER BY sal DESC) as dense_rank
FROM emp;

-- Partition by department
SELECT empno, ename, sal, deptno,
       ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal DESC) as dept_rank
FROM emp;
```

## Views

Views are virtual tables that don't store data.

### Simple Views
```sql
-- Create view
CREATE OR REPLACE VIEW emp_view AS
SELECT empno, ename, sal, deptno
FROM emp
WHERE deptno = 10;

-- Query view
SELECT * FROM emp_view;
```

### Complex Views
```sql
-- Join view
CREATE OR REPLACE VIEW emp_dept_view AS
SELECT e.ename, e.sal, d.dname, d.loc
FROM emp e, dept d
WHERE e.deptno = d.deptno;
```

### Special Views

#### Read-Only Views
```sql
CREATE OR REPLACE VIEW emp_readonly AS
SELECT * FROM emp
WITH READ ONLY;
```

#### Check Option Views
```sql
CREATE OR REPLACE VIEW emp_check AS
SELECT * FROM emp
WHERE deptno = 10
WITH CHECK OPTION;
```

#### Force Views
```sql
-- Create view even if base table doesn't exist
CREATE OR REPLACE FORCE VIEW future_view AS
SELECT * FROM future_table;
```

### Materialized Views
```sql
-- Create materialized view
CREATE MATERIALIZED VIEW emp_mv AS
SELECT * FROM emp;

-- Refresh materialized view
EXEC DBMS_MVIEW.REFRESH('emp_mv');

-- Fast refresh materialized view (requires MV log)
CREATE MATERIALIZED VIEW LOG ON emp;

CREATE MATERIALIZED VIEW emp_fast_mv
REFRESH FAST
AS SELECT * FROM emp;
```

## Indexes

Indexes improve query performance.

### Types of Indexes

#### B-Tree Index (Default)
```sql
-- Create index
CREATE INDEX emp_name_idx ON emp(ename);

-- Unique index
CREATE UNIQUE INDEX emp_empno_idx ON emp(empno);

-- Composite index
CREATE INDEX emp_dept_sal_idx ON emp(deptno, sal);
```

#### Function-Based Index
```sql
-- Index on function
CREATE INDEX emp_upper_name_idx ON emp(UPPER(ename));

-- Query using function will use index
SELECT * FROM emp WHERE UPPER(ename) = 'SMITH';
```

#### Bitmap Index
```sql
-- For low cardinality columns
CREATE BITMAP INDEX emp_job_idx ON emp(job);
```

### Index Guidelines
- Create indexes on frequently queried columns
- Avoid too many indexes on frequently updated tables
- Consider composite indexes for multiple column queries
- Drop unused indexes

## Advanced Topics

### Sequences
```sql
-- Create sequence
CREATE SEQUENCE emp_seq
START WITH 1
INCREMENT BY 1
MAXVALUE 9999
CACHE 20;

-- Use sequence
INSERT INTO emp(empno, ename) 
VALUES(emp_seq.NEXTVAL, 'JOHN');

-- Current value
SELECT emp_seq.CURRVAL FROM DUAL;
```

### Synonyms
```sql
-- Create synonym
CREATE SYNONYM e FOR emp;

-- Public synonym (requires privilege)
CREATE PUBLIC SYNONYM employees FOR hr.emp;
```

### Set Operators
```sql
-- UNION: Combine results, remove duplicates
SELECT ename FROM emp WHERE deptno = 10
UNION
SELECT ename FROM emp WHERE deptno = 20;

-- UNION ALL: Include duplicates
SELECT ename FROM emp WHERE deptno = 10
UNION ALL
SELECT ename FROM emp WHERE deptno = 20;

-- INTERSECT: Common records
SELECT ename FROM emp WHERE deptno = 10
INTERSECT
SELECT ename FROM emp WHERE job = 'CLERK';

-- MINUS: Records in first query but not in second
SELECT ename FROM emp WHERE deptno = 10
MINUS
SELECT ename FROM emp WHERE job = 'CLERK';
```

### CASE Statements
```sql
-- Simple CASE
SELECT ename, sal,
       CASE deptno
           WHEN 10 THEN 'Accounting'
           WHEN 20 THEN 'Research'
           WHEN 30 THEN 'Sales'
           ELSE 'Other'
       END as department
FROM emp;

-- Searched CASE
SELECT ename, sal,
       CASE
           WHEN sal < 1000 THEN 'Low'
           WHEN sal BETWEEN 1000 AND 3000 THEN 'Medium'
           WHEN sal > 3000 THEN 'High'
           ELSE 'Unknown'
       END as salary_grade
FROM emp;
```

### DECODE Function
```sql
-- Similar to CASE but Oracle-specific
SELECT ename, sal,
       DECODE(deptno, 
              10, 'Accounting',
              20, 'Research', 
              30, 'Sales',
              'Other') as department
FROM emp;
```

### Hierarchical Queries
```sql
-- Display organizational hierarchy
SELECT LEVEL, LPAD(' ', 2*(LEVEL-1)) || ename as employee_hierarchy
FROM emp
START WITH mgr IS NULL
CONNECT BY PRIOR empno = mgr
ORDER SIBLINGS BY ename;

-- Show path
SELECT LEVEL, SYS_CONNECT_BY_PATH(ename, '/') as path
FROM emp
START WITH mgr IS NULL
CONNECT BY PRIOR empno = mgr;
```

### Transaction Control
```sql
-- Savepoint
SAVEPOINT sp1;
UPDATE emp SET sal = sal * 1.1;
SAVEPOINT sp2;
DELETE FROM emp WHERE deptno = 30;

-- Rollback to savepoint
ROLLBACK TO sp1;

-- Commit all changes
COMMIT;
```

### User Management & Security
```sql
-- Create user
CREATE USER john IDENTIFIED BY password123;

-- Grant privileges
GRANT CONNECT, RESOURCE TO john;
GRANT SELECT, INSERT ON emp TO john;

-- Create role
CREATE ROLE developer_role;
GRANT CREATE TABLE, CREATE VIEW TO developer_role;
GRANT developer_role TO john;

-- Revoke privileges
REVOKE SELECT ON emp FROM john;
```

## Best Practices

### Performance Tips
1. **Use indexes** on frequently queried columns
2. **Avoid SELECT \*** - specify needed columns
3. **Use LIMIT/ROWNUM** for large result sets
4. **Optimize WHERE clauses** - most selective conditions first
5. **Use EXISTS** instead of IN for correlated queries

### Security Best Practices
1. **Use parameterized queries** to prevent SQL injection
2. **Grant minimum required privileges**
3. **Use views** to restrict data access
4. **Regularly review and revoke unused privileges**

### Code Quality
1. **Use meaningful names** for tables and columns
2. **Format SQL** consistently for readability
3. **Add comments** for complex queries
4. **Use constraints** to maintain data integrity
5. **Handle NULLs** explicitly

---

!!! tip "Study Tips"
    - Practice with sample data regularly
    - Understand execution plans for complex queries
    - Learn to read Oracle documentation
    - Master joins before moving to advanced topics
    - Always test queries with edge cases