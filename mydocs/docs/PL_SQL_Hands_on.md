# PL/SQL Questions & Answers Based on Oracle Sample Database (OT)

## Database Schema Overview

The Oracle sample database (OT) contains 12 tables:
- **CUSTOMERS** (319 records) - Customer information
- **CONTACTS** (319 records) - Customer contact persons
- **EMPLOYEES** (107 records) - Employee information
- **PRODUCTS** (288 records) - Product catalog
- **PRODUCT_CATEGORIES** (5 records) - Product categories
- **ORDERS** (105 records) - Order headers
- **ORDER_ITEMS** (665 records) - Order line items
- **INVENTORIES** (1112 records) - Product inventory by warehouse
- **WAREHOUSES** (9 records) - Warehouse information
- **LOCATIONS** (23 records) - Warehouse locations
- **COUNTRIES** (25 records) - Country information
- **REGIONS** (4 records) - Regional information

---

## BEGINNER LEVEL

### 1. Basic PL/SQL Block Structure

**Question:** Write a simple PL/SQL anonymous block that displays "Welcome to Oracle Tutorial" using the sample database.

**Answer:**
```sql
DECLARE
    v_message VARCHAR2(100) := 'Welcome to Oracle Tutorial';
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_message);
END;
/
```

### 2. Variables and Data Types

**Question:** Write a PL/SQL block to declare variables for storing customer information (ID, Name, Credit Limit) and assign sample values.

**Answer:**
```sql
DECLARE
    v_customer_id    NUMBER(6) := 100;
    v_customer_name  VARCHAR2(255) := 'Tech Solutions Inc';
    v_credit_limit   NUMBER(8,2) := 50000.00;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id);
    DBMS_OUTPUT.PUT_LINE('Customer Name: ' || v_customer_name);
    DBMS_OUTPUT.PUT_LINE('Credit Limit: $' || v_credit_limit);
END;
/
```

### 3. SELECT INTO Statement

**Question:** Write a PL/SQL block to fetch and display details of a specific customer using SELECT INTO.

**Answer:**
```sql
DECLARE
    v_customer_name VARCHAR2(255);
    v_credit_limit  NUMBER(8,2);
    v_address      VARCHAR2(255);
BEGIN
    SELECT name, credit_limit, address
    INTO v_customer_name, v_credit_limit, v_address
    FROM customers
    WHERE customer_id = 1;
    
    DBMS_OUTPUT.PUT_LINE('Customer: ' || v_customer_name);
    DBMS_OUTPUT.PUT_LINE('Credit Limit: $' || NVL(TO_CHAR(v_credit_limit), 'Not Set'));
    DBMS_OUTPUT.PUT_LINE('Address: ' || NVL(v_address, 'Not Available'));
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Customer not found');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
```

### 4. IF-ELSE Conditions

**Question:** Write a PL/SQL block that categorizes products based on their list price (Expensive: >1000, Moderate: 100-1000, Cheap: <100).

**Answer:**
```sql
DECLARE
    v_product_name VARCHAR2(255);
    v_list_price   NUMBER(9,2);
    v_category     VARCHAR2(20);
BEGIN
    SELECT product_name, list_price
    INTO v_product_name, v_list_price
    FROM products
    WHERE product_id = 1;
    
    IF v_list_price > 1000 THEN
        v_category := 'Expensive';
    ELSIF v_list_price >= 100 THEN
        v_category := 'Moderate';
    ELSE
        v_category := 'Cheap';
    END IF;
    
    DBMS_OUTPUT.PUT_LINE('Product: ' || v_product_name);
    DBMS_OUTPUT.PUT_LINE('Price: $' || v_list_price);
    DBMS_OUTPUT.PUT_LINE('Category: ' || v_category);
END;
/
```

### 5. Basic Loop

**Question:** Write a PL/SQL block using a basic loop to display the first 5 product categories.

**Answer:**
```sql
DECLARE
    v_counter      NUMBER := 1;
    v_category_name VARCHAR2(255);
BEGIN
    LOOP
        SELECT category_name
        INTO v_category_name
        FROM product_categories
        WHERE category_id = v_counter;
        
        DBMS_OUTPUT.PUT_LINE('Category ' || v_counter || ': ' || v_category_name);
        v_counter := v_counter + 1;
        
        EXIT WHEN v_counter > 5;
    END LOOP;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No more categories found');
END;
/
```

---

## INTERMEDIATE LEVEL

### 6. Cursor with FOR LOOP

**Question:** Write a PL/SQL block using a cursor FOR loop to display all employees with their job titles and managers.

**Answer:**
```sql
DECLARE
    v_manager_name VARCHAR2(511);
BEGIN
    FOR emp_rec IN (
        SELECT employee_id, first_name, last_name, job_title, manager_id
        FROM employees
        ORDER BY employee_id
    ) LOOP
        -- Get manager name if exists
        IF emp_rec.manager_id IS NOT NULL THEN
            BEGIN
                SELECT first_name || ' ' || last_name
                INTO v_manager_name
                FROM employees
                WHERE employee_id = emp_rec.manager_id;
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    v_manager_name := 'Manager Not Found';
            END;
        ELSE
            v_manager_name := 'No Manager (Top Level)';
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('ID: ' || emp_rec.employee_id || 
                           ' | Name: ' || emp_rec.first_name || ' ' || emp_rec.last_name ||
                           ' | Title: ' || emp_rec.job_title ||
                           ' | Manager: ' || v_manager_name);
    END LOOP;
END;
/
```

### 7. Exception Handling

**Question:** Create a PL/SQL block that handles exceptions when trying to fetch product details. Handle NO_DATA_FOUND and TOO_MANY_ROWS exceptions.

**Answer:**
```sql
DECLARE
    v_product_name VARCHAR2(255);
    v_list_price   NUMBER(9,2);
    v_category_name VARCHAR2(255);
    v_search_term  VARCHAR2(50) := 'Intel'; -- Change this to test different scenarios
BEGIN
    SELECT p.product_name, p.list_price, pc.category_name
    INTO v_product_name, v_list_price, v_category_name
    FROM products p
    JOIN product_categories pc ON p.category_id = pc.category_id
    WHERE UPPER(p.product_name) LIKE '%' || UPPER(v_search_term) || '%';
    
    DBMS_OUTPUT.PUT_LINE('Product Found:');
    DBMS_OUTPUT.PUT_LINE('Name: ' || v_product_name);
    DBMS_OUTPUT.PUT_LINE('Price: $' || v_list_price);
    DBMS_OUTPUT.PUT_LINE('Category: ' || v_category_name);
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No product found containing: ' || v_search_term);
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Multiple products found containing: ' || v_search_term);
        DBMS_OUTPUT.PUT_LINE('Please be more specific in your search.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('An unexpected error occurred: ' || SQLERRM);
END;
/
```

### 8. Parameterized Cursor

**Question:** Create a PL/SQL block with a parameterized cursor to show all orders for a specific customer along with order items.

**Answer:**
```sql
DECLARE
    CURSOR c_customer_orders(p_customer_id NUMBER) IS
        SELECT o.order_id, o.order_date, o.status, c.name as customer_name
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.customer_id = p_customer_id
        ORDER BY o.order_date DESC;
    
    CURSOR c_order_items(p_order_id NUMBER) IS
        SELECT oi.item_id, p.product_name, oi.quantity, oi.unit_price,
               (oi.quantity * oi.unit_price) as line_total
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        WHERE oi.order_id = p_order_id
        ORDER BY oi.item_id;
    
    v_customer_id   NUMBER := 1; -- Change this to test different customers
    v_order_total   NUMBER := 0;
    v_grand_total   NUMBER := 0;
    v_order_count   NUMBER := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== CUSTOMER ORDER REPORT ===');
    DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id);
    DBMS_OUTPUT.PUT_LINE('');
    
    FOR order_rec IN c_customer_orders(v_customer_id) LOOP
        v_order_count := v_order_count + 1;
        v_order_total := 0;
        
        DBMS_OUTPUT.PUT_LINE('Order #' || order_rec.order_id || 
                           ' | Date: ' || TO_CHAR(order_rec.order_date, 'DD-MON-YYYY') ||
                           ' | Status: ' || order_rec.status);
        DBMS_OUTPUT.PUT_LINE('Customer: ' || order_rec.customer_name);
        DBMS_OUTPUT.PUT_LINE('Order Items:');
        
        FOR item_rec IN c_order_items(order_rec.order_id) LOOP
            DBMS_OUTPUT.PUT_LINE('  Item ' || item_rec.item_id || ': ' || 
                               item_rec.product_name ||
                               ' | Qty: ' || item_rec.quantity ||
                               ' | Unit Price: $' || item_rec.unit_price ||
                               ' | Total: $' || item_rec.line_total);
            v_order_total := v_order_total + item_rec.line_total;
        END LOOP;
        
        DBMS_OUTPUT.PUT_LINE('  Order Total: $' || v_order_total);
        DBMS_OUTPUT.PUT_LINE('');
        v_grand_total := v_grand_total + v_order_total;
    END LOOP;
    
    IF v_order_count = 0 THEN
        DBMS_OUTPUT.PUT_LINE('No orders found for customer ID: ' || v_customer_id);
    ELSE
        DBMS_OUTPUT.PUT_LINE('=== SUMMARY ===');
        DBMS_OUTPUT.PUT_LINE('Total Orders: ' || v_order_count);
        DBMS_OUTPUT.PUT_LINE('Grand Total: $' || v_grand_total);
    END IF;
END;
/
```

### 9. Stored Procedure

**Question:** Create a stored procedure that calculates and displays inventory valuation for a specific warehouse.

**Answer:**
```sql
CREATE OR REPLACE PROCEDURE calculate_warehouse_inventory(
    p_warehouse_id IN NUMBER
) IS
    v_warehouse_name VARCHAR2(255);
    v_location      VARCHAR2(255);
    v_total_value   NUMBER := 0;
    v_total_items   NUMBER := 0;
    
    CURSOR c_inventory IS
        SELECT p.product_name, i.quantity, p.standard_cost,
               (i.quantity * p.standard_cost) as item_value
        FROM inventories i
        JOIN products p ON i.product_id = p.product_id
        WHERE i.warehouse_id = p_warehouse_id
        ORDER BY item_value DESC;
BEGIN
    -- Get warehouse information
    BEGIN
        SELECT w.warehouse_name, l.city || ', ' || l.state as location
        INTO v_warehouse_name, v_location
        FROM warehouses w
        JOIN locations l ON w.location_id = l.location_id
        WHERE w.warehouse_id = p_warehouse_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Warehouse ID ' || p_warehouse_id || ' not found.');
            RETURN;
    END;
    
    DBMS_OUTPUT.PUT_LINE('=== WAREHOUSE INVENTORY VALUATION ===');
    DBMS_OUTPUT.PUT_LINE('Warehouse: ' || v_warehouse_name);
    DBMS_OUTPUT.PUT_LINE('Location: ' || v_location);
    DBMS_OUTPUT.PUT_LINE('');
    
    FOR inv_rec IN c_inventory LOOP
        DBMS_OUTPUT.PUT_LINE('Product: ' || inv_rec.product_name);
        DBMS_OUTPUT.PUT_LINE('  Quantity: ' || inv_rec.quantity ||
                           ' | Unit Cost: $' || inv_rec.standard_cost ||
                           ' | Value: $' || inv_rec.item_value);
        
        v_total_value := v_total_value + inv_rec.item_value;
        v_total_items := v_total_items + inv_rec.quantity;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('=== SUMMARY ===');
    DBMS_OUTPUT.PUT_LINE('Total Items: ' || v_total_items);
    DBMS_OUTPUT.PUT_LINE('Total Value: $' || TO_CHAR(v_total_value, '999,999,990.00'));
END;
/

-- Execute the procedure
BEGIN
    calculate_warehouse_inventory(1);
END;
/
```

### 10. Function with Return Value

**Question:** Create a function that calculates the total sales for a given employee and returns the amount.

**Answer:**
```sql
CREATE OR REPLACE FUNCTION get_employee_sales(
    p_employee_id IN NUMBER,
    p_start_date IN DATE DEFAULT NULL,
    p_end_date IN DATE DEFAULT NULL
) RETURN NUMBER IS
    v_total_sales NUMBER := 0;
    v_employee_name VARCHAR2(511);
    v_start_date DATE;
    v_end_date DATE;
BEGIN
    -- Set default date range if not provided
    v_start_date := NVL(p_start_date, DATE '2000-01-01');
    v_end_date := NVL(p_end_date, SYSDATE);
    
    -- Check if employee exists
    BEGIN
        SELECT first_name || ' ' || last_name
        INTO v_employee_name
        FROM employees
        WHERE employee_id = p_employee_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Employee ID ' || p_employee_id || ' not found');
    END;
    
    -- Calculate total sales
    SELECT NVL(SUM(oi.quantity * oi.unit_price), 0)
    INTO v_total_sales
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.salesman_id = p_employee_id
    AND o.order_date BETWEEN v_start_date AND v_end_date;
    
    RETURN v_total_sales;
END;
/

-- Test the function
DECLARE
    v_sales_amount NUMBER;
    v_employee_id NUMBER := 56; -- Change this to test different employees
BEGIN
    v_sales_amount := get_employee_sales(v_employee_id);
    
    DBMS_OUTPUT.PUT_LINE('Employee ID: ' || v_employee_id);
    DBMS_OUTPUT.PUT_LINE('Total Sales: $' || TO_CHAR(v_sales_amount, '999,999,990.00'));
END;
/
```

---

## ADVANCED LEVEL

### 11. Package Creation

**Question:** Create a package for order management with procedures to create orders, add items, and get order summary.

**Answer:**
```sql
-- Package Specification
CREATE OR REPLACE PACKAGE pkg_order_management IS
    -- Create a new order
    PROCEDURE create_order(
        p_customer_id IN NUMBER,
        p_salesman_id IN NUMBER,
        p_order_id OUT NUMBER
    );
    
    -- Add item to order
    PROCEDURE add_order_item(
        p_order_id IN NUMBER,
        p_product_id IN NUMBER,
        p_quantity IN NUMBER,
        p_unit_price IN NUMBER DEFAULT NULL
    );
    
    -- Get order summary
    PROCEDURE get_order_summary(
        p_order_id IN NUMBER
    );
    
    -- Calculate order total
    FUNCTION calculate_order_total(
        p_order_id IN NUMBER
    ) RETURN NUMBER;
    
    -- Constants
    c_status_pending CONSTANT VARCHAR2(20) := 'Pending';
    c_status_shipped CONSTANT VARCHAR2(20) := 'Shipped';
    c_status_canceled CONSTANT VARCHAR2(20) := 'Canceled';
END pkg_order_management;
/

-- Package Body
CREATE OR REPLACE PACKAGE BODY pkg_order_management IS
    
    PROCEDURE create_order(
        p_customer_id IN NUMBER,
        p_salesman_id IN NUMBER,
        p_order_id OUT NUMBER
    ) IS
        v_customer_exists NUMBER;
        v_salesman_exists NUMBER;
    BEGIN
        -- Validate customer
        SELECT COUNT(*)
        INTO v_customer_exists
        FROM customers
        WHERE customer_id = p_customer_id;
        
        IF v_customer_exists = 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'Invalid customer ID: ' || p_customer_id);
        END IF;
        
        -- Validate salesman
        SELECT COUNT(*)
        INTO v_salesman_exists
        FROM employees
        WHERE employee_id = p_salesman_id;
        
        IF v_salesman_exists = 0 THEN
            RAISE_APPLICATION_ERROR(-20002, 'Invalid salesman ID: ' || p_salesman_id);
        END IF;
        
        -- Create order
        INSERT INTO orders (customer_id, status, salesman_id, order_date)
        VALUES (p_customer_id, c_status_pending, p_salesman_id, SYSDATE)
        RETURNING order_id INTO p_order_id;
        
        DBMS_OUTPUT.PUT_LINE('Order created successfully. Order ID: ' || p_order_id);
    END create_order;
    
    PROCEDURE add_order_item(
        p_order_id IN NUMBER,
        p_product_id IN NUMBER,
        p_quantity IN NUMBER,
        p_unit_price IN NUMBER DEFAULT NULL
    ) IS
        v_order_exists NUMBER;
        v_product_price NUMBER;
        v_next_item_id NUMBER;
    BEGIN
        -- Validate order exists
        SELECT COUNT(*)
        INTO v_order_exists
        FROM orders
        WHERE order_id = p_order_id;
        
        IF v_order_exists = 0 THEN
            RAISE_APPLICATION_ERROR(-20003, 'Invalid order ID: ' || p_order_id);
        END IF;
        
        -- Get product price if not provided
        IF p_unit_price IS NULL THEN
            SELECT list_price
            INTO v_product_price
            FROM products
            WHERE product_id = p_product_id;
        ELSE
            v_product_price := p_unit_price;
        END IF;
        
        -- Get next item ID
        SELECT NVL(MAX(item_id), 0) + 1
        INTO v_next_item_id
        FROM order_items
        WHERE order_id = p_order_id;
        
        -- Insert order item
        INSERT INTO order_items (order_id, item_id, product_id, quantity, unit_price)
        VALUES (p_order_id, v_next_item_id, p_product_id, p_quantity, v_product_price);
        
        DBMS_OUTPUT.PUT_LINE('Item added to order successfully.');
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20004, 'Invalid product ID: ' || p_product_id);
    END add_order_item;
    
    PROCEDURE get_order_summary(
        p_order_id IN NUMBER
    ) IS
        v_customer_name VARCHAR2(255);
        v_order_date DATE;
        v_status VARCHAR2(20);
        v_salesman_name VARCHAR2(511);
        v_order_total NUMBER;
        
        CURSOR c_order_items IS
            SELECT oi.item_id, p.product_name, oi.quantity, oi.unit_price,
                   (oi.quantity * oi.unit_price) as line_total
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = p_order_id
            ORDER BY oi.item_id;
    BEGIN
        -- Get order header information
        SELECT c.name, o.order_date, o.status, e.first_name || ' ' || e.last_name
        INTO v_customer_name, v_order_date, v_status, v_salesman_name
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        LEFT JOIN employees e ON o.salesman_id = e.employee_id
        WHERE o.order_id = p_order_id;
        
        -- Display order header
        DBMS_OUTPUT.PUT_LINE('=== ORDER SUMMARY ===');
        DBMS_OUTPUT.PUT_LINE('Order ID: ' || p_order_id);
        DBMS_OUTPUT.PUT_LINE('Customer: ' || v_customer_name);
        DBMS_OUTPUT.PUT_LINE('Order Date: ' || TO_CHAR(v_order_date, 'DD-MON-YYYY'));
        DBMS_OUTPUT.PUT_LINE('Status: ' || v_status);
        DBMS_OUTPUT.PUT_LINE('Salesman: ' || NVL(v_salesman_name, 'Not Assigned'));
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('Order Items:');
        
        -- Display order items
        FOR item_rec IN c_order_items LOOP
            DBMS_OUTPUT.PUT_LINE('  ' || item_rec.item_id || '. ' || item_rec.product_name ||
                               ' | Qty: ' || item_rec.quantity ||
                               ' | Price: $' || item_rec.unit_price ||
                               ' | Total: $' || item_rec.line_total);
        END LOOP;
        
        -- Calculate and display total
        v_order_total := calculate_order_total(p_order_id);
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('Order Total: $' || TO_CHAR(v_order_total, '999,999,990.00'));
        
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20005, 'Order ID ' || p_order_id || ' not found');
    END get_order_summary;
    
    FUNCTION calculate_order_total(
        p_order_id IN NUMBER
    ) RETURN NUMBER IS
        v_total NUMBER := 0;
    BEGIN
        SELECT NVL(SUM(quantity * unit_price), 0)
        INTO v_total
        FROM order_items
        WHERE order_id = p_order_id;
        
        RETURN v_total;
    END calculate_order_total;

END pkg_order_management;
/

-- Test the package
DECLARE
    v_new_order_id NUMBER;
BEGIN
    -- Create a new order
    pkg_order_management.create_order(
        p_customer_id => 1,
        p_salesman_id => 56,
        p_order_id => v_new_order_id
    );
    
    -- Add some items (you'll need to check for valid product IDs)
    pkg_order_management.add_order_item(v_new_order_id, 1, 2);
    pkg_order_management.add_order_item(v_new_order_id, 2, 1, 150.00);
    
    -- Get order summary
    pkg_order_management.get_order_summary(v_new_order_id);
END;
/
```

### 12. Collections (Associative Arrays)

**Question:** Create a PL/SQL block that uses associative arrays to store and process sales data by region.

**Answer:**
```sql
DECLARE
    -- Define associative array types
    TYPE t_region_sales IS TABLE OF NUMBER INDEX BY VARCHAR2(100);
    TYPE t_region_orders IS TABLE OF NUMBER INDEX BY VARCHAR2(100);
    
    v_region_sales t_region_sales;
    v_region_orders t_region_orders;
    v_region_name VARCHAR2(100);
    
    -- Cursor to get sales data by region
    CURSOR c_regional_sales IS
        SELECT r.region_name,
               SUM(oi.quantity * oi.unit_price) as total_sales,
               COUNT(DISTINCT o.order_id) as order_count
        FROM regions r
        JOIN countries c ON r.region_id = c.region_id
        JOIN locations l ON c.country_id = l.country_id
        JOIN warehouses w ON l.location_id = w.location_id
        JOIN inventories i ON w.warehouse_id = i.warehouse_id
        JOIN products p ON i.product_id = p.product_id
        JOIN order_items oi ON p.product_id = oi.product_id
        JOIN orders o ON oi.order_id = o.order_id
        GROUP BY r.region_name
        ORDER BY total_sales DESC;
        
    v_total_company_sales NUMBER := 0;
    v_total_company_orders NUMBER := 0;
    v_avg_order_value NUMBER := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== REGIONAL SALES ANALYSIS ===');
    DBMS_OUTPUT.PUT_LINE('');
    
    -- Populate associative arrays
    FOR sales_rec IN c_regional_sales LOOP
        v_region_sales(sales_rec.region_name) := sales_rec.total_sales;
        v_region_orders(sales_rec.region_name) := sales_rec.order_count;
        
        v_total_company_sales := v_total_company_sales + sales_rec.total_sales;
        v_total_company_orders := v_total_company_orders + sales_rec.order_count;
    END LOOP;
    
    -- Display results
    v_region_name := v_region_sales.FIRST;
    WHILE v_region_name IS NOT NULL LOOP
        v_avg_order_value := CASE 
                               WHEN v_region_orders(v_region_name) > 0 
                               THEN v_region_sales(v_region_name) / v_region_orders(v_region_name)
                               ELSE 0 
                           END;
        
        DBMS_OUTPUT.PUT_LINE('Region: ' || v_region_name);
        DBMS_OUTPUT.PUT_LINE('  Sales: $' || TO_CHAR(v_region_sales(v_region_name), '999,999,990.00'));
        DBMS_OUTPUT.PUT_LINE('  Orders: ' || v_region_orders(v_region_name));
        DBMS_OUTPUT.PUT_LINE('  Avg Order Value: $' || TO_CHAR(v_avg_order_value, '999,999,990.00'));
        DBMS_OUTPUT.PUT_LINE('  % of Total Sales: ' || 
                           TO_CHAR((v_region_sales(v_region_name) / v_total_company_sales) * 100, '990.00') || '%');
        DBMS_OUTPUT.PUT_LINE('');
        
        v_region_name := v_region_sales.NEXT(v_region_name);
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('=== COMPANY TOTALS ===');
    DBMS_OUTPUT.PUT_LINE('Total Sales: $' || TO_CHAR(v_total_company_sales, '999,999,990.00'));
    DBMS_OUTPUT.PUT_LINE('Total Orders: ' || v_total_company_orders);
    DBMS_OUTPUT.PUT_LINE('Overall Avg Order Value: $' || 
                        TO_CHAR(v_total_company_sales / v_total_company_orders, '999,999,990.00'));
END;
/
```

### 13. Complex Exception Handling with Custom Exceptions

**Question:** Create a comprehensive order processing system with custom exception handling for business rules.

**Answer:**
```sql
DECLARE
    -- Custom exceptions
    insufficient_inventory EXCEPTION;
    credit_limit_exceeded EXCEPTION;
    invalid_discount EXCEPTION;
    inactive_customer EXCEPTION;
    
    -- Variables
    v_customer_id NUMBER := 1;
    v_product_id NUMBER := 1;
    v_order_quantity NUMBER := 5;
    v_discount_percent NUMBER := 10;
    v_warehouse_id NUMBER := 1;
    
    v_credit_limit NUMBER;
    v_current_balance NUMBER;
    v_unit_price NUMBER;
    v_order_total NUMBER;
    v_available_qty NUMBER;
    v_customer_status VARCHAR2(20) := 'ACTIVE'; -- Simulate customer status
    
    -- Order details
    v_order_id NUMBER;
    v_discounted_price NUMBER;
    
    PROCEDURE validate_business_rules IS
    BEGIN
        -- Check customer credit limit
        SELECT NVL(credit_limit, 0) INTO v_credit_limit
        FROM customers WHERE customer_id = v_customer_id;
        
        -- Calculate current balance (simulate)
        SELECT NVL(SUM(oi.quantity * oi.unit_price), 0) INTO v_current_balance
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.customer_id = v_customer_id
        AND o.status != 'Paid';
        
        -- Get product price and check inventory
        SELECT list_price INTO v_unit_price
        FROM products WHERE product_id = v_product_id;
        
        SELECT quantity INTO v_available_qty
        FROM inventories 
        WHERE product_id = v_product_id AND warehouse_id = v_warehouse_id;
        
        -- Calculate order total with discount
        v_discounted_price := v_unit_price * (1 - v_discount_percent/100);
        v_order_total := v_discounted_price * v_order_quantity;
        
        -- Business rule validations
        IF v_customer_status != 'ACTIVE' THEN
            RAISE inactive_customer;
        END IF;
        
        IF v_available_qty < v_order_quantity THEN
            RAISE insufficient_inventory;
        END IF;
        
        IF (v_current_balance + v_order_total) > v_credit_limit THEN
            RAISE credit_limit_exceeded;
        END IF;
        
        IF v_discount_percent < 0 OR v_discount_percent > 50 THEN
            RAISE invalid_discount;
        END IF;
    END validate_business_rules;
    
    PROCEDURE process_order IS
    BEGIN
        -- Create order
        INSERT INTO orders (customer_id, status, salesman_id, order_date)
        VALUES (v_customer_id, 'Pending', 56, SYSDATE)
        RETURNING order_id INTO v_order_id;
        
        -- Add order item
        INSERT INTO order_items (order_id, item_id, product_id, quantity, unit_price)
        VALUES (v_order_id, 1, v_product_id, v_order_quantity, v_discounted_price);
        
        -- Update inventory
        UPDATE inventories 
        SET quantity = quantity - v_order_quantity
        WHERE product_id = v_product_id AND warehouse_id = v_warehouse_id;
        
        DBMS_OUTPUT.PUT_LINE('Order processed successfully!');
        DBMS_OUTPUT.PUT_LINE('Order ID: ' || v_order_id);
        DBMS_OUTPUT.PUT_LINE('Total Amount: 
             || TO_CHAR(v_order_total, '999,999,990.00'));
        DBMS_OUTPUT.PUT_LINE('Discount Applied: ' || v_discount_percent || '%');
    END process_order;
    
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== ORDER PROCESSING SYSTEM ===');
    DBMS_OUTPUT.PUT_LINE('Customer ID: ' || v_customer_id);
    DBMS_OUTPUT.PUT_LINE('Product ID: ' || v_product_id);
    DBMS_OUTPUT.PUT_LINE('Quantity: ' || v_order_quantity);
    DBMS_OUTPUT.PUT_LINE('');
    
    -- Validate business rules
    validate_business_rules;
    
    -- Process the order
    process_order;
    
EXCEPTION
    WHEN insufficient_inventory THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Insufficient inventory!');
        DBMS_OUTPUT.PUT_LINE('Available quantity: ' || v_available_qty);
        DBMS_OUTPUT.PUT_LINE('Requested quantity: ' || v_order_quantity);
        ROLLBACK;
        
    WHEN credit_limit_exceeded THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Credit limit exceeded!');
        DBMS_OUTPUT.PUT_LINE('Credit Limit: 
             || TO_CHAR(v_credit_limit, '999,999,990.00'));
        DBMS_OUTPUT.PUT_LINE('Current Balance: 
             || TO_CHAR(v_current_balance, '999,999,990.00'));
        DBMS_OUTPUT.PUT_LINE('Order Total: 
             || TO_CHAR(v_order_total, '999,999,990.00'));
        ROLLBACK;
        
    WHEN invalid_discount THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Invalid discount percentage!');
        DBMS_OUTPUT.PUT_LINE('Discount must be between 0% and 50%');
        DBMS_OUTPUT.PUT_LINE('Provided discount: ' || v_discount_percent || '%');
        ROLLBACK;
        
    WHEN inactive_customer THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Customer account is inactive!');
        DBMS_OUTPUT.PUT_LINE('Please contact customer service.');
        ROLLBACK;
        
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Invalid customer or product ID');
        ROLLBACK;
        
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('ERROR: Unexpected error occurred');
        DBMS_OUTPUT.PUT_LINE('Error Code: ' || SQLCODE);
        DBMS_OUTPUT.PUT_LINE('Error Message: ' || SQLERRM);
        ROLLBACK;
END;
/
```

### 14. Dynamic SQL and Bulk Operations

**Question:** Create a PL/SQL block that uses dynamic SQL to generate reports and bulk operations for performance optimization.

**Answer:**
```sql
DECLARE
    -- Types for bulk operations
    TYPE t_product_ids IS TABLE OF NUMBER;
    TYPE t_product_names IS TABLE OF VARCHAR2(255);
    TYPE t_sales_amounts IS TABLE OF NUMBER;
    
    v_product_ids t_product_ids;
    v_product_names t_product_names;
    v_sales_amounts t_sales_amounts;
    
    -- Dynamic SQL variables
    v_sql VARCHAR2(4000);
    v_report_type VARCHAR2(20) := 'SALES'; -- Can be 'SALES', 'INVENTORY', 'CUSTOMERS'
    v_sort_column VARCHAR2(50) := 'total_sales';
    v_sort_direction VARCHAR2(10) := 'DESC';
    
    -- Report parameters
    v_date_from DATE := DATE '2023-01-01';
    v_date_to DATE := SYSDATE;
    v_min_amount NUMBER := 1000;
    
    TYPE ref_cursor IS REF CURSOR;
    v_cursor ref_cursor;
    
    v_total_records NUMBER := 0;
    v_grand_total NUMBER := 0;
    
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== DYNAMIC REPORTING SYSTEM ===');
    DBMS_OUTPUT.PUT_LINE('Report Type: ' || v_report_type);
    DBMS_OUTPUT.PUT_LINE('Date Range: ' || TO_CHAR(v_date_from, 'DD-MON-YYYY') || 
                        ' to ' || TO_CHAR(v_date_to, 'DD-MON-YYYY'));
    DBMS_OUTPUT.PUT_LINE('');
    
    -- Build dynamic SQL based on report type
    CASE v_report_type
        WHEN 'SALES' THEN
            v_sql := '
                SELECT p.product_id, p.product_name, 
                       NVL(SUM(oi.quantity * oi.unit_price), 0) as total_sales
                FROM products p
                LEFT JOIN order_items oi ON p.product_id = oi.product_id
                LEFT JOIN orders o ON oi.order_id = o.order_id
                WHERE (o.order_date BETWEEN :date_from AND :date_to OR o.order_date IS NULL)
                GROUP BY p.product_id, p.product_name
                HAVING NVL(SUM(oi.quantity * oi.unit_price), 0) >= :min_amount
                ORDER BY ' || v_sort_column || ' ' || v_sort_direction;
            
            DBMS_OUTPUT.PUT_LINE('=== PRODUCT SALES REPORT ===');
            DBMS_OUTPUT.PUT_LINE('Products with sales >= 
             || v_min_amount);
            DBMS_OUTPUT.PUT_LINE('');
    END CASE;
    
    -- Execute dynamic SQL with bulk collect
    OPEN v_cursor FOR v_sql USING v_date_from, v_date_to, v_min_amount;
    FETCH v_cursor BULK COLLECT INTO v_product_ids, v_product_names, v_sales_amounts;
    CLOSE v_cursor;
    
    -- Process results using bulk operations
    IF v_product_ids.COUNT > 0 THEN
        FOR i IN 1..v_product_ids.COUNT LOOP
            v_total_records := v_total_records + 1;
            v_grand_total := v_grand_total + v_sales_amounts(i);
            
            DBMS_OUTPUT.PUT_LINE(
                RPAD(v_total_records || '.', 4) ||
                RPAD(v_product_names(i), 35) || 
                LPAD('
             || TO_CHAR(v_sales_amounts(i), '999,999,990.00'), 15)
            );
        END LOOP;
        
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE(RPAD('=', 54, '='));
        DBMS_OUTPUT.PUT_LINE(
            RPAD('TOTAL (' || v_total_records || ' records)', 39) ||
            LPAD('
             || TO_CHAR(v_grand_total, '999,999,990.00'), 15)
        );
        
    ELSE
        DBMS_OUTPUT.PUT_LINE('No records found matching the criteria.');
    END IF;
    
EXCEPTION
    WHEN OTHERS THEN
        IF v_cursor%ISOPEN THEN
            CLOSE v_cursor;
        END IF;
        DBMS_OUTPUT.PUT_LINE('Error in dynamic report generation: ' || SQLERRM);
END;
/
```

### 15. Trigger Implementation

**Question:** Create a trigger that maintains an audit trail for inventory changes when order items are modified.

**Answer:**
```sql
-- Create audit table first
CREATE TABLE inventory_audit_log (
    log_id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    product_id NUMBER,
    warehouse_id NUMBER,
    old_quantity NUMBER,
    new_quantity NUMBER,
    change_amount NUMBER,
    change_type VARCHAR2(10),
    change_date DATE DEFAULT SYSDATE,
    order_id NUMBER,
    item_id NUMBER,
    user_name VARCHAR2(100) DEFAULT USER
);

-- Create the audit trigger
CREATE OR REPLACE TRIGGER trg_inventory_audit
    AFTER INSERT OR UPDATE OR DELETE ON order_items
    FOR EACH ROW
DECLARE
    v_warehouse_id NUMBER := 1; -- Default warehouse
    v_old_qty NUMBER;
    v_new_qty NUMBER;
    v_change_amount NUMBER;
BEGIN
    -- Get current inventory quantity
    BEGIN
        SELECT quantity INTO v_old_qty
        FROM inventories
        WHERE product_id = NVL(:NEW.product_id, :OLD.product_id)
        AND warehouse_id = v_warehouse_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            v_old_qty := 0;
    END;
    
    IF INSERTING THEN
        -- New order item - decrease inventory
        v_change_amount := -:NEW.quantity;
        v_new_qty := v_old_qty + v_change_amount;
        
        -- Update inventory
        UPDATE inventories
        SET quantity = v_new_qty
        WHERE product_id = :NEW.product_id AND warehouse_id = v_warehouse_id;
        
        -- Log the change
        INSERT INTO inventory_audit_log (
            product_id, warehouse_id, old_quantity, new_quantity,
            change_amount, change_type, order_id, item_id
        ) VALUES (
            :NEW.product_id, v_warehouse_id, v_old_qty, v_new_qty,
            v_change_amount, 'INSERT', :NEW.order_id, :NEW.item_id
        );
        
    ELSIF UPDATING THEN
        -- Quantity changed - adjust inventory
        v_change_amount := :OLD.quantity - :NEW.quantity;
        v_new_qty := v_old_qty + v_change_amount;
        
        UPDATE inventories
        SET quantity = v_new_qty
        WHERE product_id = :NEW.product_id AND warehouse_id = v_warehouse_id;
        
        INSERT INTO inventory_audit_log (
            product_id, warehouse_id, old_quantity, new_quantity,
            change_amount, change_type, order_id, item_id
        ) VALUES (
            :NEW.product_id, v_warehouse_id, v_old_qty, v_new_qty,
            v_change_amount, 'UPDATE', :NEW.order_id, :NEW.item_id
        );
        
    ELSIF DELETING THEN
        -- Order item deleted - increase inventory
        v_change_amount := :OLD.quantity;
        v_new_qty := v_old_qty + v_change_amount;
        
        UPDATE inventories
        SET quantity = v_new_qty
        WHERE product_id = :OLD.product_id AND warehouse_id = v_warehouse_id;
        
        INSERT INTO inventory_audit_log (
            product_id, warehouse_id, old_quantity, new_quantity,
            change_amount, change_type, order_id, item_id
        ) VALUES (
            :OLD.product_id, v_warehouse_id, v_old_qty, v_new_qty,
            v_change_amount, 'DELETE', :OLD.order_id, :OLD.item_id
        );
    END IF;
    
EXCEPTION
    WHEN OTHERS THEN
        -- Log error but don't prevent the operation
        INSERT INTO inventory_audit_log (
            product_id, warehouse_id, old_quantity, new_quantity,
            change_amount, change_type, order_id, item_id
        ) VALUES (
            NVL(:NEW.product_id, :OLD.product_id), v_warehouse_id, -1, -1,
            0, 'ERROR', NVL(:NEW.order_id, :OLD.order_id), 
            NVL(:NEW.item_id, :OLD.item_id)
        );
END;
/
```

---

## EXPERT LEVEL CHALLENGES

### 16. Performance Analysis System

**Question:** Create an advanced performance monitoring system that analyzes database operations and provides optimization recommendations.

**Answer:**
```sql
CREATE OR REPLACE PACKAGE pkg_performance_monitor IS
    -- Analyze query performance
    PROCEDURE analyze_query_performance(
        p_sql_id IN VARCHAR2 DEFAULT NULL
    );
    
    -- Generate performance report
    PROCEDURE generate_performance_report(
        p_report_type IN VARCHAR2 DEFAULT 'SUMMARY'
    );
    
    -- Monitor table access patterns
    PROCEDURE monitor_table_access;
    
    -- Cleanup old statistics
    PROCEDURE cleanup_old_stats(
        p_days_old IN NUMBER DEFAULT 30
    );
END pkg_performance_monitor;
/

CREATE OR REPLACE PACKAGE BODY pkg_performance_monitor IS
    
    PROCEDURE analyze_query_performance(
        p_sql_id IN VARCHAR2 DEFAULT NULL
    ) IS
        CURSOR c_sql_stats IS
            SELECT sql_id, executions, elapsed_time, cpu_time,
                   buffer_gets, disk_reads, rows_processed,
                   ROUND(elapsed_time/1000000, 2) as elapsed_seconds,
                   ROUND(cpu_time/1000000, 2) as cpu_seconds,
                   CASE WHEN executions > 0 
                        THEN ROUND(elapsed_time/executions/1000, 2) 
                        ELSE 0 END as avg_elapsed_ms
            FROM v$sql
            WHERE (p_sql_id IS NULL OR sql_id = p_sql_id)
            AND executions > 0
            ORDER BY elapsed_time DESC;
    BEGIN
        DBMS_OUTPUT.PUT_LINE('=== SQL PERFORMANCE ANALYSIS ===');
        DBMS_OUTPUT.PUT_LINE('Generated: ' || TO_CHAR(SYSDATE, 'DD-MON-YYYY HH24:MI:SS'));
        DBMS_OUTPUT.PUT_LINE('');
        
        FOR sql_rec IN c_sql_stats LOOP
            DBMS_OUTPUT.PUT_LINE('SQL ID: ' || sql_rec.sql_id);
            DBMS_OUTPUT.PUT_LINE('  Executions: ' || sql_rec.executions);
            DBMS_OUTPUT.PUT_LINE('  Total Elapsed: ' || sql_rec.elapsed_seconds || 's');
            DBMS_OUTPUT.PUT_LINE('  CPU Time: ' || sql_rec.cpu_seconds || 's');
            DBMS_OUTPUT.PUT_LINE('  Avg Elapsed: ' || sql_rec.avg_elapsed_ms || 'ms');
            DBMS_OUTPUT.PUT_LINE('  Buffer Gets: ' || sql_rec.buffer_gets);
            DBMS_OUTPUT.PUT_LINE('  Disk Reads: ' || sql_rec.disk_reads);
            DBMS_OUTPUT.PUT_LINE('  Rows Processed: ' || sql_rec.rows_processed);
            
            -- Performance recommendations
            IF sql_rec.disk_reads > sql_rec.buffer_gets * 0.1 THEN
                DBMS_OUTPUT.PUT_LINE('  ** RECOMMENDATION: High disk reads - consider indexing');
            END IF;
            
            IF sql_rec.avg_elapsed_ms > 1000 THEN
                DBMS_OUTPUT.PUT_LINE('  ** RECOMMENDATION: Slow query - review execution plan');
            END IF;
            
            DBMS_OUTPUT.PUT_LINE('');
            EXIT WHEN c_sql_stats%ROWCOUNT >= 10; -- Limit output
        END LOOP;
    END analyze_query_performance;
    
    PROCEDURE generate_performance_report(
        p_report_type IN VARCHAR2 DEFAULT 'SUMMARY'
    ) IS
        v_total_sessions NUMBER;
        v_active_sessions NUMBER;
        v_blocked_sessions NUMBER;
    BEGIN
        DBMS_OUTPUT.PUT_LINE('=== DATABASE PERFORMANCE REPORT ===');
        DBMS_OUTPUT.PUT_LINE('Report Type: ' || p_report_type);
        DBMS_OUTPUT.PUT_LINE('Timestamp: ' || TO_CHAR(SYSTIMESTAMP, 'DD-MON-YYYY HH24:MI:SS.FF3'));
        DBMS_OUTPUT.PUT_LINE('');
        
        -- Session statistics
        SELECT COUNT(*), 
               SUM(CASE WHEN status = 'ACTIVE' THEN 1 ELSE 0 END),
               SUM(CASE WHEN blocking_session IS NOT NULL THEN 1 ELSE 0 END)
        INTO v_total_sessions, v_active_sessions, v_blocked_sessions
        FROM v$session
        WHERE type = 'USER';
        
        DBMS_OUTPUT.PUT_LINE('=== SESSION STATISTICS ===');
        DBMS_OUTPUT.PUT_LINE('Total Sessions: ' || v_total_sessions);
        DBMS_OUTPUT.PUT_LINE('Active Sessions: ' || v_active_sessions);
        DBMS_OUTPUT.PUT_LINE('Blocked Sessions: ' || v_blocked_sessions);
        DBMS_OUTPUT.PUT_LINE('');
        
        -- Wait events analysis
        DBMS_OUTPUT.PUT_LINE('=== TOP WAIT EVENTS ===');
        FOR wait_rec IN (
            SELECT event, total_waits, time_waited,
                   ROUND(time_waited/total_waits, 2) as avg_wait_time
            FROM v$system_event
            WHERE wait_class != 'Idle'
            AND total_waits > 0
            ORDER BY time_waited DESC
            FETCH FIRST 5 ROWS ONLY
        ) LOOP
            DBMS_OUTPUT.PUT_LINE(wait_rec.event);
            DBMS_OUTPUT.PUT_LINE('  Total Waits: ' || wait_rec.total_waits);
            DBMS_OUTPUT.PUT_LINE('  Time Waited: ' || wait_rec.time_waited || 'cs');
            DBMS_OUTPUT.PUT_LINE('  Avg Wait: ' || wait_rec.avg_wait_time || 'cs');
            DBMS_OUTPUT.PUT_LINE('');
        END LOOP;
        
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Note: Some performance views may not be accessible');
            DBMS_OUTPUT.PUT_LINE('This is normal in non-DBA environments');
    END generate_performance_report;
    
    PROCEDURE monitor_table_access IS
    BEGIN
        DBMS_OUTPUT.PUT_LINE('=== TABLE ACCESS MONITORING ===');
        DBMS_OUTPUT.PUT_LINE('Monitoring system tables for the OT schema...');
        DBMS_OUTPUT.PUT_LINE('');
        
        -- Simulate table access analysis for OT database
        FOR table_rec IN (
            SELECT table_name, num_rows, last_analyzed
            FROM user_tables
            WHERE table_name IN ('CUSTOMERS', 'ORDERS', 'ORDER_ITEMS', 'PRODUCTS', 'INVENTORIES')
            ORDER BY num_rows DESC NULLS LAST
        ) LOOP
            DBMS_OUTPUT.PUT_LINE('Table: ' || table_rec.table_name);
            DBMS_OUTPUT.PUT_LINE('  Rows: ' || NVL(TO_CHAR(table_rec.num_rows), 'Not analyzed'));
            DBMS_OUTPUT.PUT_LINE('  Last Analyzed: ' || 
                               NVL(TO_CHAR(table_rec.last_analyzed, 'DD-MON-YYYY'), 'Never'));
            
            -- Recommendations
            IF table_rec.last_analyzed IS NULL OR 
               table_rec.last_analyzed < SYSDATE - 7 THEN
                DBMS_OUTPUT.PUT_LINE('  ** RECOMMENDATION: Update table statistics');
            END IF;
            
            DBMS_OUTPUT.PUT_LINE('');
        END LOOP;
    END monitor_table_access;
    
    PROCEDURE cleanup_old_stats(
        p_days_old IN NUMBER DEFAULT 30
    ) IS
        v_cutoff_date DATE := SYSDATE - p_days_old;
        v_records_deleted NUMBER := 0;
    BEGIN
        DBMS_OUTPUT.PUT_LINE('=== CLEANUP OLD STATISTICS ===');
        DBMS_OUTPUT.PUT_LINE('Cutoff Date: ' || TO_CHAR(v_cutoff_date, 'DD-MON-YYYY'));
        
        -- This would normally clean up custom statistics tables
        -- For demo purposes, we'll just show the concept
        
        DBMS_OUTPUT.PUT_LINE('Statistics cleanup completed.');
        DBMS_OUTPUT.PUT_LINE('Records deleted: ' || v_records_deleted);
    END cleanup_old_stats;
    
END pkg_performance_monitor;
/

-- Execute performance monitoring
BEGIN
    pkg_performance_monitor.generate_performance_report('SUMMARY');
    pkg_performance_monitor.monitor_table_access;
END;
/
```

---

## PRACTICE EXERCISES

### Exercise Set 1: Basic Operations
1. **Customer Analysis**: Find customers with no orders and their contact information
2. **Inventory Valuation**: Calculate total inventory value by product category
3. **Sales Performance**: Rank employees by total sales in the last quarter
4. **Product Popularity**: Find the top 10 products by quantity sold
5. **Regional Analysis**: Compare sales performance across different regions

### Exercise Set 2: Intermediate Challenges
1. **Bulk Price Update**: Create a procedure to update product prices with audit trail
2. **Credit Management**: Implement a credit limit approval workflow system
3. **Inventory Alerts**: Build an automated low stock notification system
4. **Commission Calculator**: Create a monthly sales commission calculation system
5. **Order Tracking**: Develop a comprehensive order status tracking system

### Exercise Set 3: Advanced Projects
1. **Complete Audit System**: Implement triggers for all major table changes
2. **Data Archiving**: Create a system to archive orders older than 2 years
3. **Real-time Inventory**: Build a real-time inventory management dashboard
4. **Customer Segmentation**: Develop an RFM (Recency, Frequency, Monetary) analysis
5. **Sales Forecasting**: Create a predictive model for future sales trends

---

## BEST PRACTICES & TIPS

### 1. **Code Organization**
- Use consistent naming conventions (v_ for variables, c_ for cursors, p_ for parameters)
- Group related procedures and functions into packages
- Always include proper exception handling
- Document your code with meaningful comments

### 2. **Performance Optimization**
- Use BULK COLLECT for processing large datasets
- Implement proper indexing strategies
- Use cursor FOR loops when possible
- Avoid unnecessary data type conversions
- Use bind variables in dynamic SQL

### 3. **Error Handling**
- Always handle NO_DATA_FOUND and TOO_MANY_ROWS
- Create custom exceptions for business logic
- Use RAISE_APPLICATION_ERROR for user-defined errors
- Log errors appropriately for debugging

### 4. **Security Considerations**
- Validate all input parameters
- Use parameterized queries to prevent SQL injection
- Implement proper access controls
- Audit sensitive operations

### 5. **Testing Strategy**
- Test with various data scenarios including edge cases
- Test exception handling paths
- Verify transaction management (COMMIT/ROLLBACK)
- Performance test with realistic data volumes
- Create unit tests for critical functions

### 6. **Documentation Standards**
```sql
/*
Purpose: Brief description of what the code does
Author: Your name
Created: Date
Modified: Date and reason for modification
Parameters: 
  - p_param1: Description
  - p_param2: Description
Returns: Description of return value
Dependencies: List any dependencies
Example Usage:
  BEGIN
    procedure_name(param1, param2);
  END;
*/
```

### 7. **Sample Testing Framework**
```sql
-- Create a simple testing procedure
CREATE OR REPLACE PROCEDURE test_order_management IS
    v_order_id NUMBER;
    v_test_passed BOOLEAN := TRUE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== TESTING ORDER MANAGEMENT ===');
    
    -- Test 1: Create valid order
    BEGIN
        pkg_order_management.create_order(1, 56, v_order_id);
        DBMS_OUTPUT.PUT_LINE('✓ Test 1 PASSED: Order creation successful');
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('✗ Test 1 FAILED: ' || SQLERRM);
            v_test_passed := FALSE;
    END;
    
    -- Test 2: Add invalid product
    BEGIN
        pkg_order_management.add_order_item(v_order_id, 99999, 1);
        DBMS_OUTPUT.PUT_LINE('✗ Test 2 FAILED: Should have thrown exception');
        v_test_passed := FALSE;
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('✓ Test 2 PASSED: Invalid product rejected');
    END;
    
    -- Final result
    IF v_test_passed THEN
        DBMS_OUTPUT.PUT_LINE('=== ALL TESTS PASSED ===');
    ELSE
        DBMS_OUTPUT.PUT_LINE('=== SOME TESTS FAILED ===');
    END IF;
    
    -- Cleanup
    ROLLBACK;
END;
/
```

This comprehensive guide provides a solid foundation for mastering PL/SQL with the Oracle sample database. Practice these examples progressively, and don't forget to experiment with your own variations!