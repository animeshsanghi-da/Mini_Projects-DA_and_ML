-- ==============================================================================
-- Project: 11 - Inventory Management System
-- File: inventory_schema.sql
-- Description: DDL script to create the database schema and tables. Also Inserts the data into the tables.
-- ==============================================================================

DROP DATABASE IF EXISTS InventoryManagementDB;

-- 1. Create the Database
CREATE DATABASE IF NOT EXISTS InventoryManagementDB;
USE InventoryManagementDB;

-- 2. Create Suppliers Table (Lookup Table)
-- Demonstrates relational integrity, linking to supplier_id in the main dataset
CREATE TABLE Suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20)
);

-- 3. Create Products Table (Main Inventory Table)
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    supplier_id VARCHAR(10),
    unit_price DECIMAL(10, 2) NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 0,
    last_restock_date DATE,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- 4. Create an Index (Optimization for Analytics)
-- Adding an index on the category column to speed up aggregation queries
CREATE INDEX idx_category ON Products(category);

-- 5 Insert data into Suppliers table
-- This must happen BEFORE inserting into Products to satisfy the Foreign Key constraint
INSERT INTO Suppliers (supplier_id, supplier_name, contact_email, contact_phone)
VALUES 
('S001', 'Tech Supplies Inc.', 'contact@techsupplies.com', '555-0101'),
('S002', 'Global Electronics', 'sales@globalelec.com', '555-0102'),
('S003', 'Premium Office Furniture', 'info@premiumoffice.com', '555-0103'),
('S004', 'Paper & Pen Co.', 'support@paperpenco.com', '555-0104');

-- 6. Insert data into Products table
INSERT INTO Products (product_id, product_name, category, supplier_id, unit_price, quantity_in_stock, reorder_level, last_restock_date)
VALUES
(101, 'Wireless Mouse', 'Electronics', 'S001', 15.99, 150, 30, '2026-05-10'),
(102, 'Mechanical Keyboard', 'Electronics', 'S001', 45.50, 85, 20, '2026-06-01'),
(103, '27-inch Monitor', 'Electronics', 'S002', 199.99, 40, 10, '2026-04-15'),
(104, 'Ergonomic Chair', 'Furniture', 'S003', 120.00, 25, 5, '2026-03-20'),
(105, 'Standing Desk', 'Furniture', 'S003', 250.00, 12, 5, '2026-05-22'),
(106, 'A4 Printer Paper', 'Office Supplies', 'S004', 5.99, 500, 100, '2026-06-15'),
(107, 'Gel Pens (Pack of 10)', 'Office Supplies', 'S004', 8.50, 300, 50, '2026-06-10'),
(108, 'Whiteboard Markers', 'Office Supplies', 'S004', 4.20, 120, 30, '2026-06-12'),
(109, 'Noise Cancelling Headphones', 'Electronics', 'S002', 89.99, 60, 15, '2026-05-28'),
(110, 'USB-C Hub', 'Electronics', 'S001', 24.99, 200, 40, '2026-06-05'),
(111, 'Filing Cabinet', 'Furniture', 'S003', 75.00, 18, 5, '2026-02-14'),
(112, 'Sticky Notes (Pack of 5)', 'Office Supplies', 'S004', 3.50, 450, 100, '2026-06-20'),
(113, 'Webcam 1080p', 'Electronics', 'S002', 39.99, 90, 20, '2026-05-05'),
(114, 'Desk Lamp', 'Furniture', 'S003', 22.50, 45, 10, '2026-04-30'),
(115, 'HDMI Cable 6ft', 'Electronics', 'S001', 9.99, 350, 50, '2026-06-22'),
(116, 'Notebook 1', 'Furniture', 'S001', 108.45, 301, 71, '2026-03-01'),
(117, 'External Hard Drive 2', 'Electronics', 'S001', 260.59, 365, 7, '2026-01-08'),
(118, 'Desk Organizer 3', 'Office Supplies', 'S002', 391.02, 380, 45, '2026-02-19'),
(119, 'Notebook 4', 'Electronics', 'S003', 223.66, 230, 21, '2026-02-25'),
(120, 'Stapler 5', 'Office Supplies', 'S003', 192.02, 344, 11, '2026-04-16'),
(121, 'Office Chair 6', 'Electronics', 'S003', 39.85, 489, 62, '2026-02-23'),
(122, 'External Hard Drive 7', 'Office Supplies', 'S003', 213.78, 139, 5, '2026-02-02'),
(123, 'Office Chair 8', 'Furniture', 'S002', 356.65, 110, 99, '2026-05-08'),
(124, 'Desk Organizer 9', 'Electronics', 'S004', 6.45, 207, 42, '2026-03-19'),
(125, 'USB Drive 10', 'Office Supplies', 'S003', 203.19, 451, 8, '2026-01-10'),
(126, 'Monitor Stand 11', 'Electronics', 'S003', 408.13, 28, 25, '2026-05-17'),
(127, 'Stapler 12', 'Office Supplies', 'S002', 42.26, 193, 60, '2026-06-13'),
(128, 'Desk Organizer 13', 'Furniture', 'S001', 465.60, 71, 28, '2026-04-13'),
(129, 'USB Drive 14', 'Furniture', 'S004', 247.23, 415, 66, '2026-03-19'),
(130, 'Office Chair 15', 'Furniture', 'S003', 241.81, 475, 77, '2026-04-24'),
(131, 'Notebook 16', 'Office Supplies', 'S004', 264.53, 447, 49, '2026-04-18'),
(132, 'Stapler 17', 'Office Supplies', 'S001', 48.36, 68, 17, '2026-04-22'),
(133, 'Notebook 18', 'Office Supplies', 'S002', 170.80, 10, 98, '2026-04-26'),
(134, 'Paper Clips 19', 'Office Supplies', 'S001', 257.06, 248, 27, '2026-06-09'),
(135, 'Paper Clips 20', 'Furniture', 'S002', 43.22, 220, 60, '2026-05-28'),
(136, 'Stapler 21', 'Office Supplies', 'S003', 285.29, 378, 37, '2026-05-10'),
(137, 'Stapler 22', 'Office Supplies', 'S004', 2.26, 148, 7, '2026-01-26'),
(138, 'Bluetooth Speaker 23', 'Furniture', 'S001', 346.89, 154, 46, '2026-06-12'),
(139, 'Bluetooth Speaker 24', 'Furniture', 'S002', 25.31, 286, 39, '2026-03-13'),
(140, 'USB Drive 25', 'Electronics', 'S002', 85.98, 91, 67, '2026-01-14'),
(141, 'External Hard Drive 26', 'Electronics', 'S003', 309.09, 445, 5, '2026-01-27'),
(142, 'Bluetooth Speaker 27', 'Furniture', 'S002', 266.84, 448, 39, '2026-01-07'),
(143, 'USB Drive 28', 'Office Supplies', 'S002', 36.89, 468, 97, '2026-05-25'),
(144, 'Keyboard Tray 29', 'Office Supplies', 'S001', 480.27, 458, 46, '2026-05-21'),
(145, 'Desk Organizer 30', 'Office Supplies', 'S001', 491.25, 430, 16, '2026-02-13'),
(146, 'USB Drive 31', 'Office Supplies', 'S003', 139.34, 308, 51, '2026-02-13'),
(147, 'Office Chair 32', 'Office Supplies', 'S003', 463.97, 411, 8, '2026-01-25'),
(148, 'Monitor Stand 33', 'Office Supplies', 'S004', 202.97, 326, 39, '2026-02-22'),
(149, 'Paper Clips 34', 'Electronics', 'S002', 123.95, 126, 38, '2026-02-03'),
(150, 'Paper Clips 35', 'Electronics', 'S001', 365.05, 12, 28, '2026-02-18'),
(151, 'Bluetooth Speaker 36', 'Electronics', 'S004', 455.39, 402, 25, '2026-01-06'),
(152, 'External Hard Drive 37', 'Electronics', 'S004', 263.73, 303, 77, '2026-02-11'),
(153, 'Desk Organizer 38', 'Electronics', 'S004', 111.21, 115, 62, '2026-03-02'),
(154, 'Stapler 39', 'Furniture', 'S002', 182.31, 199, 96, '2026-04-09'),
(155, 'Office Chair 40', 'Electronics', 'S002', 402.05, 417, 42, '2026-05-19'),
(156, 'Stapler 41', 'Office Supplies', 'S001', 69.29, 54, 40, '2026-06-04'),
(157, 'Keyboard Tray 42', 'Office Supplies', 'S002', 54.93, 490, 89, '2026-06-18'),
(158, 'Bluetooth Speaker 43', 'Electronics', 'S001', 441.28, 360, 65, '2026-01-14'),
(159, 'USB Drive 44', 'Furniture', 'S004', 284.71, 443, 76, '2026-01-03'),
(160, 'Bluetooth Speaker 45', 'Office Supplies', 'S002', 166.38, 220, 49, '2026-05-15'),
(161, 'Desk Organizer 46', 'Office Supplies', 'S003', 94.80, 46, 99, '2026-04-30'),
(162, 'Keyboard Tray 47', 'Office Supplies', 'S001', 267.43, 322, 21, '2026-03-25'),
(163, 'Desk Organizer 48', 'Office Supplies', 'S003', 12.82, 42, 13, '2026-03-22'),
(164, 'Office Chair 49', 'Furniture', 'S002', 252.01, 465, 65, '2026-04-05'),
(165, 'Desk Organizer 50', 'Office Supplies', 'S001', 442.82, 62, 79, '2026-05-01'),
(166, 'External Hard Drive 51', 'Furniture', 'S003', 366.84, 492, 49, '2026-05-15'),
(167, 'Stapler 52', 'Electronics', 'S002', 78.26, 459, 13, '2026-03-21'),
(168, 'Notebook 53', 'Electronics', 'S002', 474.67, 66, 74, '2026-05-21'),
(169, 'Office Chair 54', 'Electronics', 'S003', 277.11, 219, 30, '2026-01-22'),
(170, 'USB Drive 55', 'Furniture', 'S003', 213.97, 108, 41, '2026-01-13'),
(171, 'Paper Clips 56', 'Electronics', 'S002', 211.12, 410, 83, '2026-01-28'),
(172, 'Bluetooth Speaker 57', 'Office Supplies', 'S001', 42.06, 396, 35, '2026-05-04'),
(173, 'Office Chair 58', 'Office Supplies', 'S002', 37.63, 322, 100, '2026-02-26'),
(174, 'Monitor Stand 59', 'Furniture', 'S002', 12.30, 385, 10, '2026-06-14'),
(175, 'Keyboard Tray 60', 'Electronics', 'S004', 484.38, 252, 9, '2026-05-24'),
(176, 'USB Drive 61', 'Electronics', 'S004', 62.20, 386, 74, '2026-06-07'),
(177, 'Office Chair 62', 'Office Supplies', 'S001', 497.94, 78, 96, '2026-02-26'),
(178, 'Paper Clips 63', 'Furniture', 'S001', 453.91, 154, 88, '2026-01-13'),
(179, 'Bluetooth Speaker 64', 'Electronics', 'S001', 120.02, 26, 19, '2026-01-29'),
(180, 'Stapler 65', 'Office Supplies', 'S001', 461.60, 291, 9, '2026-03-07'),
(181, 'USB Drive 66', 'Furniture', 'S002', 232.79, 189, 33, '2026-06-11'),
(182, 'Paper Clips 67', 'Furniture', 'S003', 143.77, 428, 15, '2026-01-16'),
(183, 'Paper Clips 68', 'Furniture', 'S002', 402.59, 245, 64, '2026-06-23'),
(184, 'USB Drive 69', 'Office Supplies', 'S004', 174.28, 294, 14, '2026-04-02'),
(185, 'External Hard Drive 70', 'Furniture', 'S004', 329.44, 3, 50, '2026-02-08'),
(186, 'Paper Clips 71', 'Office Supplies', 'S004', 423.68, 52, 43, '2026-06-22'),
(187, 'USB Drive 72', 'Office Supplies', 'S003', 66.25, 204, 26, '2026-06-09'),
(188, 'Bluetooth Speaker 73', 'Furniture', 'S003', 344.38, 356, 46, '2026-05-24'),
(189, 'Keyboard Tray 74', 'Office Supplies', 'S002', 300.32, 461, 16, '2026-02-09'),
(190, 'Keyboard Tray 75', 'Office Supplies', 'S002', 180.38, 8, 33, '2026-05-30'),
(191, 'Keyboard Tray 76', 'Furniture', 'S001', 7.26, 473, 61, '2026-06-12'),
(192, 'Keyboard Tray 77', 'Furniture', 'S001', 411.87, 262, 46, '2026-05-18'),
(193, 'Notebook 78', 'Office Supplies', 'S003', 9.79, 492, 35, '2026-01-03'),
(194, 'Monitor Stand 79', 'Electronics', 'S004', 354.16, 466, 50, '2026-04-19'),
(195, 'External Hard Drive 80', 'Electronics', 'S004', 357.97, 221, 35, '2026-02-11'),
(196, 'Keyboard Tray 81', 'Furniture', 'S003', 236.29, 396, 51, '2026-03-16'),
(197, 'Bluetooth Speaker 82', 'Office Supplies', 'S001', 268.00, 311, 27, '2026-01-14'),
(198, 'USB Drive 83', 'Office Supplies', 'S003', 324.76, 399, 70, '2026-05-15'),
(199, 'Desk Organizer 84', 'Office Supplies', 'S004', 5.64, 238, 29, '2026-02-03'),
(200, 'Stapler 85', 'Furniture', 'S002', 244.12, 20, 100, '2026-05-13'),
(201, 'Monitor Stand 86', 'Electronics', 'S004', 238.84, 202, 20, '2026-01-30'),
(202, 'Office Chair 87', 'Furniture', 'S001', 249.26, 128, 40, '2026-03-23'),
(203, 'External Hard Drive 88', 'Office Supplies', 'S004', 277.59, 405, 94, '2026-04-27'),
(204, 'Keyboard Tray 89', 'Furniture', 'S003', 136.90, 297, 8, '2026-04-08'),
(205, 'Bluetooth Speaker 90', 'Furniture', 'S002', 440.65, 14, 9, '2026-04-14'),
(206, 'External Hard Drive 91', 'Electronics', 'S003', 234.14, 54, 42, '2026-03-24'),
(207, 'Desk Organizer 92', 'Electronics', 'S002', 222.92, 469, 14, '2026-01-13'),
(208, 'Keyboard Tray 93', 'Furniture', 'S003', 282.49, 173, 29, '2026-05-01'),
(209, 'Stapler 94', 'Electronics', 'S004', 34.85, 395, 5, '2026-03-25'),
(210, 'Paper Clips 95', 'Electronics', 'S001', 487.01, 133, 9, '2026-01-14'),
(211, 'Paper Clips 96', 'Office Supplies', 'S004', 365.28, 54, 68, '2026-03-25'),
(212, 'USB Drive 97', 'Office Supplies', 'S003', 211.17, 165, 20, '2026-02-05'),
(213, 'Stapler 98', 'Electronics', 'S001', 264.24, 325, 84, '2026-02-01'),
(214, 'External Hard Drive 99', 'Office Supplies', 'S002', 121.22, 393, 44, '2026-01-14'),
(215, 'Office Chair 100', 'Office Supplies', 'S002', 264.08, 214, 83, '2026-04-26');