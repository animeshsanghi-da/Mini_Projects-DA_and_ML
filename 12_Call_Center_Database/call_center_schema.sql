-- call_center_schema.sql

-- Drop database if it already exists to ensure a clean slate for testing
DROP DATABASE IF EXISTS call_center_db;

-- Create the database
CREATE DATABASE IF NOT EXISTS call_center_db;
USE call_center_db;

-- Create the main call records table
CREATE TABLE call_records (
    call_id VARCHAR(15) PRIMARY KEY,
    agent_id VARCHAR(10) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    call_date DATE NOT NULL,
    call_time TIME NOT NULL,
    duration_minutes INT NOT NULL,
    call_type VARCHAR(50) NOT NULL,
    resolution_status VARCHAR(50) NOT NULL,
    csat_score INT,
    
    -- Ensure CSAT score falls within the standard 1-5 range
    CONSTRAINT chk_csat_score CHECK (csat_score >= 1 AND csat_score <= 5)
);

-- Optional: Create indexes to speed up common analytical queries
CREATE INDEX idx_agent_id ON call_records(agent_id);
CREATE INDEX idx_call_date ON call_records(call_date);
CREATE INDEX idx_call_type ON call_records(call_type);

-- Import Data from CSV file
-- Note: Adjust the file path to match your local directory structure.
LOAD DATA LOCAL INFILE 'C:/Users/MY PC/Downloads/minor_projects/12_Call_Center_Database/call_center_data.csv'
INTO TABLE call_records
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;