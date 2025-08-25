# Oracle Database Practice Questions - OT Sample Database

## Database Overview
The OT (Oracle Tutorial) sample database represents a global computer hardware company with the following tables:

- **REGIONS** (4 records) - Regional divisions
- **COUNTRIES** (25 records) - Country information
- **LOCATIONS** (23 records) - Warehouse locations
- **WAREHOUSES** (9 records) - Storage facilities
- **EMPLOYEES** (107 records) - Staff information
- **PRODUCT_CATEGORIES** (5 records) - Product classifications
- **PRODUCTS** (288 records) - Hardware products
- **CUSTOMERS** (319 records) - Customer master data
- **CONTACTS** (319 records) - Customer contact persons
- **ORDERS** (105 records) - Order headers
- **ORDER_ITEMS** (665 records) - Order line items
- **INVENTORIES** (1112 records) - Stock information

---

## BEGINNER LEVEL QUESTIONS

### 1. Basic SELECT Operations

**Q1:** Display all region names from the REGIONS table.
```sql
-- Answer:
SELECT region_name FROM regions;
```

**Q2:** Show the first 10 products with their names and list prices.
```sql
-- Answer:
SELECT product_name, list_price 
FROM products 
WHERE ROWNUM <= 10;
```

**Q3:** Find all employees whose first name is 'John'.
```sql
-- Answer:
SELECT employee_id, first_name, last_name, email
FROM employees
WHERE first_name = 'John';
```

### 2. Basic WHERE Conditions

**Q4:** List all customers with a credit limit greater than 10000.
```sql
-- Answer:
SELECT customer_id, name, credit_limit
FROM customers
WHERE credit_limit > 10000;
```

**Q5:** Show products that cost less than $100 (list_price).
```sql
-- Answer:
SELECT product_name, list_price
FROM products
WHERE list_price < 100;
```

**Q6:** Find all orders placed in 2017.
```sql
-- Answer:
SELECT order_id, customer_id, order_date, status
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2017;
```

### 3. Basic Sorting and DISTINCT

**Q7:** Display all unique job titles from the employees table.
```sql
-- Answer:
SELECT DISTINCT job_title FROM employees;
```

**Q8:** List all products ordered by their list price (highest first).
```sql
-- Answer:
SELECT product_name, list_price
FROM products
ORDER BY list_price DESC;
```

**Q9:** Show customer names in alphabetical order.
```sql
-- Answer:
SELECT name FROM customers ORDER BY name;
```

### 4. Basic Aggregate Functions

**Q10:** Count the total number of products in the database.
```sql
-- Answer:
SELECT COUNT(*) as total_products FROM products;
```

**Q11:** Find the average credit limit of all customers.
```sql
-- Answer:
SELECT AVG(credit_limit) as avg_credit_limit FROM customers;
```

**Q12:** What is the highest list price among all products?
```sql
-- Answer:
SELECT MAX(list_price) as highest_price FROM products;
```

---

## INTERMEDIATE LEVEL QUESTIONS

### 1. JOIN Operations

**Q13:** Display customer names with their contact person's full name and email.
```sql
-- Answer:
SELECT c.name as customer_name, 
       con.first_name || ' ' || con.last_name as contact_name,
       con.email
FROM customers c
INNER JOIN contacts con ON c.customer_id = con.customer_id;
```

**Q14:** List all products with their category names.
```sql
-- Answer:
SELECT p.product_name, pc.category_name, p.list_price
FROM products p
INNER JOIN product_categories pc ON p.category_id = pc.category_id
ORDER BY pc.category_name, p.product_name;
```

**Q15:** Show employee names with their manager's names.
```sql
-- Answer:
SELECT e.first_name || ' ' || e.last_name as employee_name,
       m.first_name || ' ' || m.last_name as manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
```

### 2. GROUP BY and HAVING

**Q16:** Count the number of products in each category.
```sql
-- Answer:
SELECT pc.category_name, COUNT(p.product_id) as product_count
FROM product_categories pc
LEFT JOIN products p ON pc.category_id = p.category_id
GROUP BY pc.category_name
ORDER BY product_count DESC;
```

**Q17:** Find customers who have placed more than 2 orders.
```sql
-- Answer:
SELECT c.name, COUNT(o.order_id) as order_count
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 2
ORDER BY order_count DESC;
```

**Q18:** Show the average list price for each product category, but only for categories with an average price above $500.
```sql
-- Answer:
SELECT pc.category_name, ROUND(AVG(p.list_price), 2) as avg_price
FROM product_categories pc
INNER JOIN products p ON pc.category_id = p.category_id
GROUP BY pc.category_name
HAVING AVG(p.list_price) > 500
ORDER BY avg_price DESC;
```

### 3. Subqueries

**Q19:** Find products that are more expensive than the average product price.
```sql
-- Answer:
SELECT product_name, list_price
FROM products
WHERE list_price > (SELECT AVG(list_price) FROM products)
ORDER BY list_price DESC;
```

**Q20:** List customers who have never placed an order.
```sql
-- Answer:
SELECT name, customer_id
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

**Q21:** Find the top 3 most expensive products in each category.
```sql
-- Answer:
SELECT category_name, product_name, list_price
FROM (
    SELECT pc.category_name, p.product_name, p.list_price,
           ROW_NUMBER() OVER (PARTITION BY pc.category_name ORDER BY p.list_price DESC) as rn
    FROM products p
    INNER JOIN product_categories pc ON p.category_id = pc.category_id
) 
WHERE rn <= 3
ORDER BY category_name, list_price DESC;
```

### 4. Date Functions and CASE Statements

**Q22:** Classify orders by their age: 'Recent' (within 1 year), 'Old' (1-2 years), 'Very Old' (more than 2 years).
```sql
-- Answer:
SELECT order_id, order_date,
    CASE 
        WHEN order_date >= ADD_MONTHS(SYSDATE, -12) THEN 'Recent'
        WHEN order_date >= ADD_MONTHS(SYSDATE, -24) THEN 'Old'
        ELSE 'Very Old'
    END as order_age_category
FROM orders
ORDER BY order_date DESC;
```

**Q23:** Find employees hired in each month of the year and count them.
```sql
-- Answer:
SELECT TO_CHAR(hire_date, 'Month') as hire_month,
       COUNT(*) as employees_hired
FROM employees
GROUP BY TO_CHAR(hire_date, 'Month'), TO_CHAR(hire_date, 'MM')
ORDER BY TO_CHAR(hire_date, 'MM');
```

---

## ADVANCED LEVEL QUESTIONS

### 1. Complex JOINs and Analytics

**Q24:** Calculate the running total of order amounts by customer.
```sql
-- Answer:
SELECT c.name as customer_name, o.order_date, o.order_id,
       oi.total_amount,
       SUM(oi.total_amount) OVER (
           PARTITION BY c.customer_id 
           ORDER BY o.order_date 
           ROWS UNBOUNDED PRECEDING
       ) as running_total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN (
    SELECT order_id, SUM(quantity * unit_price) as total_amount
    FROM order_items
    GROUP BY order_id
) oi ON o.order_id = oi.order_id
ORDER BY c.name, o.order_date;
```

**Q25:** Find the month-over-month sales growth percentage.
```sql
-- Answer:
WITH monthly_sales AS (
    SELECT TO_CHAR(o.order_date, 'YYYY-MM') as order_month,
           SUM(oi.quantity * oi.unit_price) as monthly_total
    FROM orders o
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY TO_CHAR(o.order_date, 'YYYY-MM')
)
SELECT order_month, monthly_total,
       LAG(monthly_total) OVER (ORDER BY order_month) as prev_month_total,
       ROUND(
           ((monthly_total - LAG(monthly_total) OVER (ORDER BY order_month)) / 
            LAG(monthly_total) OVER (ORDER BY order_month)) * 100, 2
       ) as growth_percentage
FROM monthly_sales
ORDER BY order_month;
```

### 2. Advanced Subqueries and CTEs

**Q26:** Find customers who have ordered products from at least 3 different categories.
```sql
-- Answer:
WITH customer_categories AS (
    SELECT c.customer_id, c.name,
           COUNT(DISTINCT p.category_id) as category_count
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.product_id
    GROUP BY c.customer_id, c.name
)
SELECT name, category_count
FROM customer_categories
WHERE category_count >= 3
ORDER BY category_count DESC;
```

**Q27:** Identify top-selling products that generate 80% of total revenue (Pareto Analysis).
```sql
-- Answer:
WITH product_revenue AS (
    SELECT p.product_id, p.product_name,
           SUM(oi.quantity * oi.unit_price) as product_revenue
    FROM products p
    INNER JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name
),
total_revenue AS (
    SELECT SUM(product_revenue) as total_rev FROM product_revenue
),
ranked_products AS (
    SELECT pr.product_name, pr.product_revenue,
           SUM(pr.product_revenue) OVER (ORDER BY pr.product_revenue DESC) as cumulative_revenue,
           tr.total_rev,
           (SUM(pr.product_revenue) OVER (ORDER BY pr.product_revenue DESC) / tr.total_rev) * 100 as cumulative_percentage
    FROM product_revenue pr
    CROSS JOIN total_revenue tr
)
SELECT product_name, product_revenue, cumulative_percentage
FROM ranked_products
WHERE cumulative_percentage <= 80
ORDER BY product_revenue DESC;
```

### 3. Advanced Window Functions

**Q28:** Rank employees by their tenure within each job title.
```sql
-- Answer:
SELECT first_name || ' ' || last_name as employee_name,
       job_title, hire_date,
       DENSE_RANK() OVER (
           PARTITION BY job_title 
           ORDER BY hire_date
       ) as tenure_rank,
       ROUND(SYSDATE - hire_date) as days_employed
FROM employees
ORDER BY job_title, tenure_rank;
```

**Q29:** Find products whose sales in the current quarter exceed the previous quarter by more than 20%.
```sql
-- Answer:
WITH quarterly_sales AS (
    SELECT p.product_id, p.product_name,
           TO_CHAR(o.order_date, 'YYYY-Q') as quarter,
           SUM(oi.quantity * oi.unit_price) as quarterly_revenue
    FROM products p
    INNER JOIN order_items oi ON p.product_id = oi.product_id
    INNER JOIN orders o ON oi.order_id = o.order_id
    GROUP BY p.product_id, p.product_name, TO_CHAR(o.order_date, 'YYYY-Q')
),
quarterly_comparison AS (
    SELECT product_name, quarter, quarterly_revenue,
           LAG(quarterly_revenue) OVER (
               PARTITION BY product_id 
               ORDER BY quarter
           ) as prev_quarter_revenue
    FROM quarterly_sales
)
SELECT product_name, quarter, quarterly_revenue, prev_quarter_revenue,
       ROUND(((quarterly_revenue - prev_quarter_revenue) / prev_quarter_revenue) * 100, 2) as growth_percentage
FROM quarterly_comparison
WHERE prev_quarter_revenue IS NOT NULL
  AND ((quarterly_revenue - prev_quarter_revenue) / prev_quarter_revenue) > 0.20
ORDER BY growth_percentage DESC;
```

### 4. Complex Business Logic

**Q30:** Create a comprehensive customer analysis report including: customer tier (based on total orders), preferred categories, and loyalty score.
```sql
-- Answer:
WITH customer_metrics AS (
    SELECT c.customer_id, c.name,
           COUNT(DISTINCT o.order_id) as total_orders,
           SUM(oi.quantity * oi.unit_price) as total_spent,
           COUNT(DISTINCT p.category_id) as categories_purchased,
           ROUND(AVG(oi.quantity * oi.unit_price), 2) as avg_order_value,
           MIN(o.order_date) as first_order_date,
           MAX(o.order_date) as last_order_date
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.product_id
    GROUP BY c.customer_id, c.name
),
customer_tiers AS (
    SELECT *,
        CASE 
            WHEN total_spent > 50000 THEN 'Platinum'
            WHEN total_spent > 20000 THEN 'Gold'
            WHEN total_spent > 5000 THEN 'Silver'
            ELSE 'Bronze'
        END as customer_tier,
        -- Loyalty score based on multiple factors
        ROUND(
            (total_orders * 0.3) + 
            (categories_purchased * 0.2) + 
            (CASE WHEN SYSDATE - last_order_date <= 90 THEN 2 ELSE 0 END) +
            (LEAST(total_spent / 1000, 10) * 0.5), 2
        ) as loyalty_score
    FROM customer_metrics
)
SELECT name, customer_tier, total_orders, total_spent, 
       avg_order_value, categories_purchased, loyalty_score,
       ROUND(SYSDATE - last_order_date) as days_since_last_order
FROM customer_tiers
ORDER BY loyalty_score DESC, total_spent DESC;
```

---

## PRACTICE EXERCISES

### Data Modification Challenges

**Exercise 1:** Create a stored procedure to automatically update inventory levels when an order is shipped.

**Exercise 2:** Write a trigger that prevents orders from being placed if the total amount exceeds the customer's credit limit.

**Exercise 3:** Develop a function that calculates the optimal reorder point for each product based on historical sales data.

### Performance Optimization

**Exercise 4:** Analyze and optimize the query performance for finding the top 10 customers by revenue in the last 6 months.

**Exercise 5:** Create appropriate indexes for the most frequently used queries in the system.

### Reporting Challenges

**Exercise 6:** Build a comprehensive sales dashboard query that shows:
- Monthly sales trends
- Top-performing products and categories
- Regional performance comparison
- Customer segmentation analysis

**Exercise 7:** Create a query to identify potential inventory issues (overstocking/understocking) by analyzing sales velocity and current stock levels.

---

## TIPS FOR PRACTICE

1. **Start Simple**: Begin with single-table queries before moving to joins
2. **Understand the Data**: Study the relationships between tables carefully
3. **Test Incrementally**: Build complex queries step by step
4. **Use Aliases**: Make your queries more readable with meaningful aliases
5. **Practice Regularly**: Try to solve each question without looking at the answer first
6. **Experiment**: Modify the queries to explore different scenarios
7. **Optimize**: Always consider performance implications of your queries

Happy practicing with Oracle SQL!