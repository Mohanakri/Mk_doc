
---

````markdown
# Oracle PL/SQL Interview Questions & Answers (Concept → Scenario)

---

### Q1. Procedure vs Function
**Concept:**  
- A **procedure** performs actions and may/may not return a value. Used for tasks like DML and workflows. Cannot be called directly in SQL.  
- A **function** must return a single value and can be used inside SQL (SELECT, WHERE). Expected to be computation-focused.  

**Scenario:**  
I used a procedure to process monthly payroll (insert/update salary records). I built a function to calculate employee tax % and called it inside a SELECT query for reports.

---

### Q2. Cursors — implicit, explicit, REF, `FOR UPDATE` / `WHERE CURRENT OF`, BULK COLLECT & FORALL
**Concept:**  
- **Implicit cursors**: Oracle manages automatically for single-row queries/DML.  
- **Explicit cursors**: Declared explicitly with `OPEN`, `FETCH`, `CLOSE`.  
- **REF cursors**: Cursor variables for dynamic queries (strong/weak).  
- `FOR UPDATE` locks rows, `WHERE CURRENT OF` updates/deletes current row.  
- **BULK COLLECT** fetches multiple rows in one go; **FORALL** performs mass DML with collections.  

**Scenario:**  
I fetched 10k rows with BULK COLLECT and used FORALL for inserts in ETL. It reduced processing time from hours to minutes.

---

### Q3. %TYPE vs %ROWTYPE
**Concept:**  
- `%TYPE`: Variable inherits datatype of a column/variable.  
- `%ROWTYPE`: Record variable representing all columns of a table/cursor row.  

**Scenario:**  
I used `%TYPE` for salary variable (`v_sal employees.salary%TYPE`). For full row fetch, I used `%ROWTYPE` to get all employee details at once.

---

### Q4. Triggers — DML, DDL, Database, INSTEAD OF, Row vs Statement
**Concept:**  
- **DML Triggers** → Fire on INSERT/UPDATE/DELETE. Row-level (`FOR EACH ROW`) or statement-level.  
- **DDL Triggers** → Fire on CREATE, ALTER, DROP.  
- **Database/System Triggers** → Fire on LOGON, LOGOFF, STARTUP, SHUTDOWN.  
- **INSTEAD OF triggers** → Allow DML on views.  

**Scenario:**  
I used a row-level DML trigger to log salary changes into an audit table. For reporting, I created an INSTEAD OF INSERT trigger on a view to insert into multiple normalized tables.

---

### Q5. Mutating Table Error
**Concept:**  
Occurs when a row-level trigger queries/updates the same table that fired it. Oracle blocks this to avoid inconsistent reads.  

**Fixes:**  
- Use statement-level or compound triggers.  
- Use package collections or temp tables.  
- Use PRAGMA AUTONOMOUS_TRANSACTION only for logging.  

**Scenario:**  
In a banking project, a trigger on `accounts` caused mutating error. I fixed it using a compound trigger with package-level variables.

---

### Q6. Packages — spec & body, advantages
**Concept:**  
- **Spec**: Public declarations (procedures, functions, variables).  
- **Body**: Implementation.  
- Advantages: Encapsulation, modularity, reusability, better performance.  

**Scenario:**  
I created a `payroll_pkg` with procedures for salary, bonus, and tax. This improved reusability across modules.

---

### Q7. PRAGMA AUTONOMOUS_TRANSACTION
**Concept:**  
Runs as an independent transaction with its own COMMIT/ROLLBACK. Common for logging, auditing.  

**Scenario:**  
I wrote a logging procedure with AUTONOMOUS_TRANSACTION so error logs were committed even if the main transaction rolled back.

---

### Q8. Exception Handling & RAISE_APPLICATION_ERROR
**Concept:**  
- Handle runtime errors with `EXCEPTION` blocks.  
- **Predefined exceptions**: NO_DATA_FOUND, TOO_MANY_ROWS, ZERO_DIVIDE.  
- **User-defined exceptions**: Declared/raised explicitly.  
- `RAISE_APPLICATION_ERROR(-20001, 'msg')` for custom errors.  

**Scenario:**  
On data load, I trapped `NO_DATA_FOUND` and logged it. For business rule violations (like salary < 0), I raised application errors with meaningful messages.

---

### Q9. Dynamic SQL — `EXECUTE IMMEDIATE` vs `DBMS_SQL`
**Concept:**  
- `EXECUTE IMMEDIATE`: Simple, supports binds, RETURNING INTO.  
- `DBMS_SQL`: Advanced, for unknown SQL at runtime.  
- **Security**: Always use bind variables, validate identifiers with `DBMS_ASSERT` to prevent SQL injection.  

**Scenario:**  
I built a reporting module with dynamic filters using EXECUTE IMMEDIATE and bind variables to avoid SQL injection.

---

### Q10. Collections — Associative Arrays, Nested Tables, VARRAY
**Concept:**  
- **Associative arrays**: In-memory key-value, best for lookups.  
- **Nested tables**: Unordered set, can be stored in DB columns.  
- **VARRAY**: Bounded, ordered array.  

**Scenario:**  
I cached product prices using associative arrays. For multi-value attributes, I used nested tables. For fixed small lists (e.g., weekdays), I used VARRAYs.

---

### Q11. BULK COLLECT & FORALL (Performance)
**Concept:**  
- **BULK COLLECT**: Fetch multiple rows into collection in one call.  
- **FORALL**: Execute DML in bulk using a collection.  
- Use `LIMIT` to avoid memory overload.  

**Scenario:**  
I rewrote row-by-row ETL into BULK COLLECT + FORALL, cutting runtime from 3 hours to 20 minutes.

---

### Q12. Performance Tuning — Techniques
**Concept:**  
- Minimize context switches (use bulk ops).  
- Avoid SELECT *, fetch only required columns.  
- Use indexes and partitioning.  
- Analyze execution plans.  
- Prefer set-based SQL over loops.  

**Scenario:**  
I replaced a row-by-row update with a MERGE statement — execution improved drastically.

---

### Q13. Indexing
**Concept:**  
- **B-Tree**: Default, good for high-cardinality.  
- **Bitmap**: Good for low-cardinality (DW), not OLTP.  
- **Function-based**: Indexes expressions.  
- **Composite**: Multi-column index.  

**Scenario:**  
For a reporting query, I created a composite index `(customer_id, txn_date)` which reduced query runtime significantly.

---

### Q14. Execution Plans
**Concept:**  
- Use `EXPLAIN PLAN` / `DBMS_XPLAN.DISPLAY_CURSOR` to check joins, access paths.  
- Watch for full scans, nested loops on large data, missing indexes.  

**Scenario:**  
I fixed a slow join by adding an index, which changed plan from nested loop to hash join, improving performance.

---

### Q15. Tracing & Debugging
**Concept / Tools:**  
- `DBMS_OUTPUT` for debugging.  
- `DBMS_PROFILER` for performance profiling.  
- `DBMS_UTILITY.FORMAT_ERROR_BACKTRACE` for error line info.  
- `SQL_TRACE` / TKPROF for SQL-level analysis.  

**Scenario:**  
I used DBMS_PROFILER to detect a function bottleneck and rewrote it in set-based SQL.

---

### Q16. SQL & PL/SQL Interaction
**Concept:**  
- SQL inside PL/SQL causes context switches.  
- Minimize with BULK operations, set-based queries.  
- Use bind variables for better execution plans.  

**Scenario:**  
Instead of 1000 small queries, I used a single bulk query with BULK COLLECT — performance improved massively.

---

### Q17. Joins & Subqueries
**Concept:**  
- Joins are usually more efficient than correlated subqueries.  
- Correlated subqueries run once per row, can be slow.  
- Replace with joins or analytic functions where possible.  

**Scenario:**  
I replaced a correlated subquery with a pre-aggregated CTE and join, reducing query time from minutes to seconds.

---

### Q18. Analytic Functions — ROW_NUMBER, RANK, LAG, LEAD
**Concept:**  
- **ROW_NUMBER**: Deduplication, pagination.  
- **RANK / DENSE_RANK**: Ranking with/without gaps.  
- **LAG/LEAD**: Compare with previous/next row.  

**Scenario:**  
I used LAG to compare current month spend with previous month to detect unusual spikes in customer activity.

---

### Q19. Bulk Data Loading — SQL*Loader
**Concept:**  
Oracle utility to load bulk data from external files (CSV, TXT) into tables using control files.  

**Scenario:**  
I used SQL*Loader in a retail project to load daily sales CSV into staging tables. Control file handled column mapping and skipping invalid rows.

---

### Q20. Real-World Problem Scenarios
**ETL Performance:** Replaced row-by-row load with BULK COLLECT + FORALL, runtime cut by hours.  
**Mutating Trigger:** Fixed using compound trigger with package variables.  
**Deadlocks:** Used `FOR UPDATE SKIP LOCKED` and optimized commits.  

---

### Q21. Code Standards & Best Practices
**Concept:**  
- Clear naming conventions (`pkg_`, `proc_`).  
- Encapsulation via packages.  
- Avoid hard-coded literals.  
- Always handle exceptions.  
- Unit testing and peer reviews.  

**Scenario:**  
I enforced package naming standards and code checks in CI pipeline — reduced production issues.

---

### Q22. Security in PL/SQL
**Concept:**  
- Prevent SQL injection: use bind variables, `DBMS_ASSERT`.  
- Apply least privilege principle.  
- Definer vs Invoker rights (`AUTHID`).  
- Handle sensitive data carefully (masking, encryption).  

**Scenario:**  
I secured dynamic SQL by using bind variables and DBMS_ASSERT. Also restructured schema privileges for least privilege.

---

### Q23. Testing & Deployment
**Concept:**  
- Use version control for scripts.  
- Automate deployments with rollback options.  
- Test in lower envs before production.  

**Scenario:**  
I created rollback-capable deployment scripts and added automated unit tests before promoting to prod — deployment issues reduced.

---

### Q24. Useful Quick Snippets

**FOR UPDATE / WHERE CURRENT OF**
```plsql
OPEN c FOR SELECT id, balance FROM accounts WHERE status='A' FOR UPDATE;
FETCH c INTO v_id, v_balance;
UPDATE accounts SET balance = v_balance - 100 WHERE CURRENT OF c;
CLOSE c;
```

**RAISE_APPLICATION_ERROR**
```plsql
IF salary < 0 THEN
  RAISE_APPLICATION_ERROR(-20001, 'Salary cannot be negative');
END IF;
```

**BULK COLLECT + FORALL**
```plsql
SELECT id, amount BULK COLLECT INTO l_recs FROM txns WHERE batch_id = v_batch;
FORALL i IN 1..l_recs.COUNT
  UPDATE accounts SET balance = balance + l_recs(i).amount WHERE id = l_recs(i).id;
```

---


---

