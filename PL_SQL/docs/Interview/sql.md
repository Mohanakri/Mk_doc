
---

markdown
# Oracle SQL Interview Questions & Answers

---

## 1. Basic SQL Questions

### Q1. Difference between DELETE, TRUNCATE, and DROP  
- **DELETE**: DML, can delete all or specific rows, slower, rollback possible.  
- **TRUNCATE**: DDL, removes all rows at once, faster, rollback not possible.  
- **DROP**: Removes the table definition and all data permanently.  

---

### Q2. Difference between CHAR and VARCHAR2  
- **CHAR(n)**: Fixed length, always allocates `n` characters (pads with spaces).  
- **VARCHAR2(n)**: Variable length, stores only actual characters.  

---

### Q3. Difference between DATE and TIMESTAMP  
- **DATE**: Stores date and time (to the second).  
- **TIMESTAMP**: Stores date, time, and fractional seconds (up to microseconds).  

---

### Q4. Difference between SUBSTR and INSTR  
- **SUBSTR**: Extracts part of a string.  
```sql
SELECT SUBSTR('welcome',1,3) FROM dual; -- wel
```
- **INSTR**: Finds position of a character or substring.  
```sql
SELECT INSTR('welcome','e',1,1) FROM dual; -- 2
```

---

### Q5. What are constraints in Oracle SQL?  
- **NOT NULL** – Column must have a value.  
- **UNIQUE** – All values must be unique.  
- **PRIMARY KEY** – Combination of NOT NULL + UNIQUE.  
- **FOREIGN KEY** – Enforces referential integrity.  
- **CHECK** – Ensures condition on column values.  
- **DEFAULT** – Assigns default value if not provided.  

---

### Q6. Difference between VIEW and MATERIALIZED VIEW  
- **VIEW**: Logical representation of a query, always shows live data.  
- **MATERIALIZED VIEW**: Stores data physically, can be refreshed manually or on schedule.  

---

### Q7. UNION vs UNION ALL  
- **UNION**: Removes duplicates, sorts results.  
- **UNION ALL**: Keeps duplicates, faster.  

---

### Q8. How to delete duplicate records?  
```sql
DELETE FROM emp e1
WHERE ROWID > (
  SELECT MIN(ROWID)
  FROM emp e2
  WHERE e2.emp_id = e1.emp_id
);

-- To display duplicates
SELECT emp_id, COUNT(*)
FROM emp
GROUP BY emp_id
HAVING COUNT(*) > 1;
```

---

### Q9. RANK vs DENSE_RANK  
- **RANK**: Assigns rank, skips numbers if duplicates exist.  
- **DENSE_RANK**: Assigns rank without gaps, consecutive numbers.  

---

### Q10. Right Join vs Left Join  
- **LEFT JOIN**: All rows from left table + matched rows from right.  
- **RIGHT JOIN**: All rows from right table + matched rows from left.  

---

### Q11. Why do we use Joins? Types?  
We use joins to combine rows from multiple tables based on related columns.  

Types:  
- Equi join  
- Non-Equi join  
- Cross join  
- Inner join  
- Left Outer join  
- Right Outer join  
- Full Outer join  
- Self join  

---

## 2. Intermediate SQL Questions

### Q12. What are indexes? Types of indexes in Oracle?  
- Indexes speed up query performance.  
Types:  
- B-tree (default, balanced structure).  
- Bitmap (good for low-cardinality columns).  
- Function-based index.  
- Composite index (multiple columns).  
- Unique and Non-Unique indexes.  

---

### Q13. What are aggregate and analytic functions?  
- **Aggregate functions**: Perform calculations on groups. (SUM, AVG, COUNT, MAX, MIN).  
- **Analytic functions**: Work on sets of rows and return values per row.  
```sql
SELECT emp_id, salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

---

### Q14. What are subqueries and correlated subqueries?  
- **Subquery**: A query inside another query, executes once.  
```sql
SELECT name FROM employees
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'IT');
```  
- **Correlated Subquery**: Executes once for each row of the outer query.  
```sql
SELECT name FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
```

---

## 3. Advanced SQL Questions

### Q15. What is ROWNUM vs ROW_NUMBER()?  
- **ROWNUM**: Pseudocolumn, assigned before ORDER BY.  
- **ROW_NUMBER()**: Analytic function, assigns number after ORDER BY.  

---

### Q16. What is the difference between EXISTS and IN?  
- **IN**: Compares value with a list or subquery result.  
- **EXISTS**: Returns TRUE if subquery returns at least one row, often faster with correlated queries.  
```sql
-- Using IN
SELECT name FROM employees WHERE dept_id IN (SELECT dept_id FROM departments);

-- Using EXISTS
SELECT name FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.dept_id = e.dept_id);
```

---

### Q17. How to find the 2nd highest salary?  
```sql
-- Using Subquery
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Using Analytic Function
SELECT * FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) WHERE rnk = 2;
```

---

### Q18. Difference between DELETE with WHERE and Trigger with Cascade Delete  
- **DELETE with WHERE**: Deletes only specified rows.  
- **Cascade Delete (via Trigger/Constraint)**: Automatically deletes child rows when parent row is deleted.  

---

### Q19. How to improve SQL performance? (Tuning)  
- Use `EXPLAIN PLAN` or `DBMS_XPLAN` to check execution.  
- Create proper indexes.  
- Avoid `SELECT *`, fetch only needed columns.  
- Use bind variables.  
- Partition large tables.  
- Rewrite queries for efficiency.  
- Use bulk operations for large datasets.  

---

### Q20. What is a CTE (WITH clause)?  
A Common Table Expression improves readability and reusability.  
```sql
WITH dept_avg AS (
   SELECT dept_id, AVG(salary) AS avg_sal
   FROM employees
   GROUP BY dept_id
)
SELECT e.name, e.salary, d.avg_sal
FROM employees e
JOIN dept_avg d ON e.dept_id = d.dept_id;
```

---

### Q21. Explain MERGE statement  
Used for **UPSERT** (Insert or Update in one statement).  
```sql
MERGE INTO employees e
USING new_employees n
ON (e.emp_id = n.emp_id)
WHEN MATCHED THEN
   UPDATE SET e.salary = n.salary
WHEN NOT MATCHED THEN
   INSERT (emp_id, name, salary) VALUES (n.emp_id, n.name, n.salary);
```

---

### Q22. Difference between PRIMARY KEY and UNIQUE  
- **PRIMARY KEY**: Only one per table, enforces uniqueness + NOT NULL.  
- **UNIQUE**: Allows one NULL, multiple unique constraints allowed.  

---

### Q23. What are Global Temporary Tables (GTT)?  
- Data is session/transaction-specific, structure is permanent.  
```sql
CREATE GLOBAL TEMPORARY TABLE temp_emp (
   id NUMBER, name VARCHAR2(50)
) ON COMMIT DELETE ROWS;
```

---

### Q24. What are Sequences in Oracle?  
- Object used to generate unique numbers automatically.  
```sql
CREATE SEQUENCE emp_seq START WITH 1 INCREMENT BY 1;
INSERT INTO employees VALUES (emp_seq.NEXTVAL, 'Mohan', 5000);
```

---

### Q25. How do you handle Hierarchical Queries in Oracle?  
Using `CONNECT BY`.  
```sql
SELECT employee_id, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
```

---


---

