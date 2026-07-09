# Inventory Management System (Project 11)

## Overview
This project provides a structured SQL-based framework for managing inventory operations. It includes the database schema, sample inventory data, and a suite of analytical queries to track stock levels, calculate valuation, identify stale items, and monitor supplier dependencies.

## Directory Structure
- `inventory_schema.sql`: The DDL & DML script for creating the `InventoryManagementDB` database, tables, indexing, and populating the initial sample data.
- `inventory_queries.sql`: A collection of DQL and DML scripts for operational and financial reporting.

## Prerequisites
- A relational database management system (RDBMS) such as **MySQL**, **MariaDB**, or **PostgreSQL**.
- A SQL client or CLI to execute the scripts (e.g., MySQL Workbench, DBeaver, or command line).

## Setup Instructions

### 1. Initialize and Populate the Database
Execute the `inventory_schema.sql` file. This single script will create the database, build the tables, and insert all necessary `Suppliers` and `Products` data automatically.

```sql
-- Run this in your SQL client
SOURCE path/to/11_Inventory_Management/inventory_schema.sql;
```

## Key Features & Queries

The `inventory_queries.sql` file is divided into four actionable sections:

### 1. Operational Alerts
* **Low Stock Alert:** Identifies items where `quantity_in_stock` is less than or equal to the `reorder_level`. Use this for automated procurement triggers.

### 2. Financial Metrics
* **Inventory Valuation:** Aggregates total capital tied up in stock per category using `SUM(unit_price * quantity_in_stock)`.
* **High-Value Assets:** Generates a leaderboard of the top 10 most expensive items currently in stock.

### 3. Supply Chain & Logistics
* **Supplier Dependency Report:** Analyzes total stock volume provided by each supplier.
* **Stale Inventory:** Flags products that have not been restocked since March 2026, useful for identifying slow-moving items.

### 4. Data Manipulation
* **Record a Restock:** Includes a template `UPDATE` statement to adjust stock levels and timestamps after a delivery.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.

## Contact
Project created as part of the Inventory Management System module.