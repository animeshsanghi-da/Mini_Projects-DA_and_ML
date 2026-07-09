-- ==============================================================================
-- Project: 11 - Inventory Management System
-- File: inventory_queries.sql
-- Description: DML and DQL script for inventory analysis and reporting.
-- ==============================================================================

USE InventoryManagementDB;

-- ==========================================
-- SECTION 1: OPERATIONAL ALERTS
-- ==========================================

-- 1. LOW STOCK ALERT
-- Identify products that have hit or dropped below their reorder level.
-- Useful for generating automated purchasing reports.
SELECT 
    product_id, 
    product_name, 
    quantity_in_stock, 
    reorder_level, 
    supplier_id
FROM 
    Products
WHERE 
    quantity_in_stock <= reorder_level
ORDER BY 
    quantity_in_stock ASC;
-- Insight: 
-- Highlights immediate operational vulnerabilities by pinpointing items at risk of stockouts.
-- This allows procurement teams to act proactively rather than reactively, ensuring continuous supply chain flow and preventing lost sales.

-- ==========================================
-- SECTION 2: FINANCIAL METRICS
-- ==========================================

-- 2. INVENTORY VALUATION BY CATEGORY
-- Calculate the total capital tied up in stock for each category.
SELECT 
    IFNULL(category, 'Total') AS category,
    COUNT(product_id) AS total_unique_products,
    SUM(quantity_in_stock) AS total_items,
    ROUND(SUM(unit_price * quantity_in_stock), 2) AS total_inventory_value
FROM 
    Products
GROUP BY 
    category WITH ROLLUP
ORDER BY 
    (category IS NULL) ASC,
    total_inventory_value ASC;
-- Insight: 
-- Reveals exactly where the company's capital is locked up across different product lines. 
-- This macro-level view helps finance teams optimize budget allocation and identify if too much cash is tied down in slow-moving categories.

-- 3. HIGH-VALUE ASSET IDENTIFICATION
-- Find the top 10 most expensive items currently in stock.
SELECT 
    product_id, 
    product_name, 
    category,
    unit_price, 
    quantity_in_stock
FROM 
    Products
ORDER BY 
    unit_price DESC
LIMIT 10;
-- Insight: 
-- Pinpoints the premium items that carry the highest individual financial risk. 
-- These products dictate where warehouse managers should focus their auditing, security, and loss-prevention efforts.

-- ==========================================
-- SECTION 3: SUPPLY CHAIN & LOGISTICS
-- ==========================================

-- 4. SUPPLIER DEPENDENCY REPORT
-- Determine which suppliers provide the most inventory by volume.
-- Uses a LEFT JOIN to ensure products without a registered supplier are still counted.
SELECT 
    s.supplier_id,
    COALESCE(s.supplier_name, 'Unknown/Pending Supplier') AS supplier_name,
    COUNT(p.product_id) AS products_supplied,
    SUM(p.quantity_in_stock) AS total_stock_volume
FROM 
    Products p
LEFT JOIN 
    Suppliers s ON p.supplier_id = s.supplier_id
GROUP BY 
    s.supplier_id, s.supplier_name
ORDER BY 
    total_stock_volume DESC;
-- Insight: 
-- Measures supply chain risk by mapping inventory volume to specific vendors. 
-- If a massive portion of total stock comes from a single supplier, it exposes a critical dependency that could halt operations if that vendor faces delays.

-- 5. STALE INVENTORY IDENTIFICATION
-- Find products that haven't been restocked recently (e.g., before March 2026).
-- Helps in identifying slow-moving goods that might need discounting.
SELECT 
    product_id, 
    product_name, 
    category, 
    quantity_in_stock,
    last_restock_date
FROM 
    Products
WHERE 
    last_restock_date < '2026-03-01'
ORDER BY 
    last_restock_date ASC;
-- Insight: 
-- Exposes "dead stock" and slow-moving capital that is taking up valuable warehouse space. 
-- This provides actionable data for marketing to push clearance sales or for buyers to adjust future purchasing strategies.

-- ==========================================
-- SECTION 4: DATA MANIPULATION (DML EXAMPLES)
-- ==========================================

-- 6. RECORD A RESTOCK (Update stock and restock date)
-- Example: 50 new units of 'Wireless Mouse' (ID 101) arrived today.
/*
UPDATE Products
SET 
    quantity_in_stock = quantity_in_stock + 50,
    last_restock_date = CURRENT_DATE
WHERE 
    product_id = 101;
*/