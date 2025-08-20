# PL/SQL Complete Notes

## Table of Contents Structure

This document outlines the recommended MkDocs structure for your PL/SQL notes based on the comprehensive content provided.

## Suggested `mkdocs.yml` Configuration

```yaml
site_name: PL/SQL Complete Guide
site_description: Comprehensive PL/SQL learning resource
site_author: Your Name
site_url: https://yoursite.com

theme:
  name: material
  palette:
    - scheme: default
      primary: blue
      accent: light blue
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: blue
      accent: light blue
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - search.share
    - toc.follow

plugins:
  - search
  - minify:
      minify_html: true

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - admonition
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Introduction:
    - PL/SQL Overview: introduction/overview.md
    - Block Structure: introduction/block-structure.md
    - Variables & Data Types: introduction/variables.md
  - Basic Concepts:
    - SELECT INTO: basics/select-into.md
    - Variable Attributes: basics/variable-attributes.md
    - Conditional Statements: basics/conditionals.md
    - Control Statements: basics/loops.md
    - Bind Variables: basics/bind-variables.md
  - Cursors:
    - Cursor Basics: cursors/introduction.md
    - Implicit Cursors: cursors/implicit.md
    - Explicit Cursors: cursors/explicit.md
    - Cursor Attributes: cursors/attributes.md
    - Cursor FOR Loops: cursors/for-loops.md
    - Parameterized Cursors: cursors/parameterized.md
  - Exception Handling:
    - Exception Types: exceptions/types.md
    - Predefined Exceptions: exceptions/predefined.md
    - User-Defined Exceptions: exceptions/user-defined.md
    - Exception Propagation: exceptions/propagation.md
    - Error Functions: exceptions/error-functions.md
  - Subprograms:
    - Procedures: subprograms/procedures.md
    - Functions: subprograms/functions.md
    - Parameter Modes: subprograms/parameters.md
    - Local Subprograms: subprograms/local.md
  - Packages:
    - Package Basics: packages/introduction.md
    - Global Variables: packages/globals.md
    - Overloading: packages/overloading.md
    - Forward Declaration: packages/forward.md
  - Collections:
    - Index by Tables: collections/index-by.md
    - Nested Tables: collections/nested.md
    - VArrays: collections/varrays.md
    - PL/SQL Records: collections/records.md
  - Bulk Operations:
    - Bulk Collect: bulk/bulk-collect.md
    - FORALL Statement: bulk/forall.md
    - Bulk Exceptions: bulk/exceptions.md
  - REF Cursors:
    - REF Cursor Types: ref-cursors/types.md
    - Strong vs Weak: ref-cursors/strong-weak.md
    - SYS_REFCURSOR: ref-cursors/sys-refcursor.md
  - Triggers:
    - Trigger Basics: triggers/introduction.md
    - Row vs Statement: triggers/row-statement.md
    - Trigger Events: triggers/events.md
    - System Triggers: triggers/system.md
    - Compound Triggers: triggers/compound.md
  - Advanced Topics:
    - Dynamic SQL: advanced/dynamic-sql.md
    - UTL_FILE Package: advanced/utl-file.md
    - SQL*Loader: advanced/sql-loader.md
    - Large Objects (LOBs): advanced/lobs.md
    - Object Types: advanced/objects.md
  - Oracle Features:
    - 11g Features: features/11g.md
    - 12c Features: features/12c.md
    - Predefined Packages: features/packages.md
```

## Sample Page Structure

### 1. Introduction/Overview (introduction/overview.md)

```markdown
# PL/SQL Overview

## What is PL/SQL?

PL/SQL (Procedural Language Extension for SQL) is Oracle's procedural extension to SQL. It was introduced with Oracle 6.0.

### Version History

| Oracle Version | PL/SQL Version |
|----------------|----------------|
| Oracle 6.0     | PL/SQL 1.0     |
| Oracle 7.0     | PL/SQL 2.0     |
| Oracle 8.0     | PL/SQL 8.0     |
| Oracle 11.2    | PL/SQL 11.2    |

### Key Features

- **Block Structured**: Organized into logical blocks
- **Procedural**: Supports loops, conditions, procedures
- **Integrated**: Seamlessly works with SQL
- **Portable**: Runs on any platform that supports Oracle

!!! info "Processing Architecture"
    When you submit a PL/SQL block:
    - **SQL Engine**: Executes SQL statements
    - **PL/SQL Engine**: Executes procedural statements
```

### 2. Block Structure (introduction/block-structure.md)

```markdown
# PL/SQL Block Structure

## Block Types

PL/SQL has two types of blocks:

### 1. Anonymous Blocks
```sql
DECLARE
    -- Variable declarations
BEGIN
    -- Executable statements
EXCEPTION
    -- Exception handling
END;
/
```

### 2. Named Blocks
- Stored Procedures
- Functions
- Packages
- Triggers

## Basic Block Structure

```sql
DECLARE (Optional)
    -- Variable declarations
    -- Constant declarations
    -- Type declarations
    -- Cursor declarations
BEGIN (Mandatory)
    -- Executable statements
    -- SQL statements
    -- PL/SQL statements
EXCEPTION (Optional)
    -- Exception handlers
END; (Mandatory)
/
```

!!! example "Simple Example"
    ```sql
    DECLARE
        v_message VARCHAR2(50);
    BEGIN
        v_message := 'Hello, PL/SQL!';
        DBMS_OUTPUT.PUT_LINE(v_message);
    END;
    /
    ```
```

### 3. Variables & Data Types (introduction/variables.md)

```markdown
# Variables and Data Types

## Variable Declaration

### Syntax
```sql
variable_name datatype(size);
```

### Example
```sql
DECLARE
    v_empno NUMBER(10);
    v_ename VARCHAR2(20);
    v_salary NUMBER(10,2) := 5000;
    v_bonus NUMBER(10,2) DEFAULT 1000;
BEGIN
    -- Variable usage
END;
/
```

## Storing Values

### Assignment Operator (:=)
```sql
DECLARE
    v_number NUMBER(10);
BEGIN
    v_number := 50;
    DBMS_OUTPUT.PUT_LINE(v_number);
END;
/
```

## Displaying Output

### DBMS_OUTPUT Package
```sql
-- Enable output
SET SERVEROUTPUT ON;

-- Display message
DBMS_OUTPUT.PUT_LINE('Your message here');

-- Display variable
DBMS_OUTPUT.PUT_LINE(variable_name);
```

## Data Types

### Scalar Data Types
- `NUMBER` - Numeric values
- `VARCHAR2` - Variable length strings
- `DATE` - Date values
- `BOOLEAN` - True/False values

### Composite Data Types
- `RECORD` - User-defined records
- `TABLE` - Collections
- `VARRAY` - Variable arrays

!!! tip "Best Practices"
    - Always initialize variables
    - Use meaningful variable names
    - Follow naming conventions (v_ for variables, c_ for constants)
```

### 4. Cursors Introduction (cursors/introduction.md)

```markdown
# Cursors in PL/SQL

## What is a Cursor?

A cursor is a private SQL memory area used to process multiple records on a record-by-record basis.

## Types of Cursors

### 1. Implicit Cursors
- Automatically created by Oracle
- Used for single-row SELECT statements
- Also called "Context Area"

### 2. Explicit Cursors
- Manually declared by programmer
- Used for multi-row SELECT statements
- Also called "Active Set Area"

## When to Use Cursors?

| Scenario | Cursor Type |
|----------|-------------|
| Single row SELECT | Implicit |
| Multiple row processing | Explicit |
| Row-by-row operations | Explicit |

## Cursor Memory Structure

```
┌─────────────────┐
│   Cursor Area   │
├─────────────────┤
│  %FOUND        │
│  %NOTFOUND     │
│  %ISOPEN       │
│  %ROWCOUNT     │
└─────────────────┘
```

!!! note "Important"
    Cursors provide a way to process query results one row at a time, giving you complete control over data processing.
```

### 5. Exception Handling (exceptions/types.md)

```markdown
# Exception Handling in PL/SQL

## What are Exceptions?

Exceptions are runtime errors that occur during program execution. PL/SQL provides a robust mechanism to handle these errors gracefully.

## Types of Exceptions

### 1. Predefined Exceptions
Oracle provides 20+ predefined exceptions for common errors:

| Exception Name | Oracle Error | Description |
|---------------|--------------|-------------|
| `NO_DATA_FOUND` | ORA-01403 | SELECT INTO returns no rows |
| `TOO_MANY_ROWS` | ORA-01422 | SELECT INTO returns multiple rows |
| `ZERO_DIVIDE` | ORA-01476 | Division by zero |
| `DUP_VAL_ON_INDEX` | ORA-00001 | Unique constraint violation |

### 2. User-Defined Exceptions
Custom exceptions created by programmers:

```sql
DECLARE
    insufficient_salary EXCEPTION;
    v_salary NUMBER := 3000;
BEGIN
    IF v_salary < 5000 THEN
        RAISE insufficient_salary;
    END IF;
EXCEPTION
    WHEN insufficient_salary THEN
        DBMS_OUTPUT.PUT_LINE('Salary is too low!');
END;
/
```

### 3. Unnamed Exceptions
Oracle errors without predefined names:

```sql
DECLARE
    foreign_key_error EXCEPTION;
    PRAGMA EXCEPTION_INIT(foreign_key_error, -2291);
BEGIN
    -- Code that might raise ORA-02291
EXCEPTION
    WHEN foreign_key_error THEN
        DBMS_OUTPUT.PUT_LINE('Foreign key constraint violated!');
END;
/
```

## Exception Handling Syntax

```sql
EXCEPTION
    WHEN exception_name1 THEN
        -- Handle specific exception
    WHEN exception_name2 THEN
        -- Handle another exception
    WHEN OTHERS THEN
        -- Handle any other exception
END;
```

!!! warning "Best Practice"
    Always handle exceptions appropriately. Use WHEN OTHERS as a catch-all, but be specific when possible.
```

## Directory Structure

Create the following directory structure for your MkDocs project:

```
docs/
├── index.md
├── introduction/
│   ├── overview.md
│   ├── block-structure.md
│   └── variables.md
├── basics/
│   ├── select-into.md
│   ├── variable-attributes.md
│   ├── conditionals.md
│   ├── loops.md
│   └── bind-variables.md
├── cursors/
│   ├── introduction.md
│   ├── implicit.md
│   ├── explicit.md
│   ├── attributes.md
│   ├── for-loops.md
│   └── parameterized.md
├── exceptions/
│   ├── types.md
│   ├── predefined.md
│   ├── user-defined.md
│   ├── propagation.md
│   └── error-functions.md
├── subprograms/
│   ├── procedures.md
│   ├── functions.md
│   ├── parameters.md
│   └── local.md
├── packages/
│   ├── introduction.md
│   ├── globals.md
│   ├── overloading.md
│   └── forward.md
├── collections/
│   ├── index-by.md
│   ├── nested.md
│   ├── varrays.md
│   └── records.md
├── bulk/
│   ├── bulk-collect.md
│   ├── forall.md
│   └── exceptions.md
├── ref-cursors/
│   ├── types.md
│   ├── strong-weak.md
│   └── sys-refcursor.md
├── triggers/
│   ├── introduction.md
│   ├── row-statement.md
│   ├── events.md
│   ├── system.md
│   └── compound.md
├── advanced/
│   ├── dynamic-sql.md
│   ├── utl-file.md
│   ├── sql-loader.md
│   ├── lobs.md
│   └── objects.md
└── features/
    ├── 11g.md
    ├── 12c.md
    └── packages.md
```

## Additional Features

### Code Highlighting
Use proper SQL syntax highlighting:

```sql
-- This will be highlighted as SQL
DECLARE
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM emp;
    DBMS_OUTPUT.PUT_LINE('Employee count: ' || v_count);
END;
/
```

### Admonitions
Use Material theme admonitions for better presentation:

!!! info "Information"
    This is informational content.

!!! tip "Pro Tip"
    This is a helpful tip.

!!! warning "Warning"
    This is important warning information.

!!! example "Example"
    This shows an example.

### Tables
Create comparison tables:

| Feature | Implicit Cursor | Explicit Cursor |
|---------|----------------|-----------------|
| Declaration | Automatic | Manual |
| Control | Oracle | Developer |
| Usage | Single row | Multiple rows |

This structure will give you a comprehensive, well-organized PL/SQL documentation site using MkDocs with Material theme.