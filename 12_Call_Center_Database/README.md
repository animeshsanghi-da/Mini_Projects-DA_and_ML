# Call Center Operational Analytics Database

This project provides a comprehensive SQL-based framework for managing and analyzing call center performance. It includes schema definitions, sample data, and analytical queries to track KPIs, agent efficiency, and escalation root causes.

## Project Overview

The database is designed to store and process call records, allowing managers to derive actionable insights regarding:
* **Operational Efficiency:** Average handling time, peak hour demand, and call volumes.
* **Quality Control:** CSAT (Customer Satisfaction) scores per agent and per call type.
* **Performance Bottlenecks:** Identification of high-escalation periods, pending issue tracking, and root cause analysis for poor satisfaction.

---

## Database Structure

The `call_records` table tracks individual customer interactions.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `call_id` | VARCHAR(15) | Unique identifier for each call (Primary Key). |
| `agent_id` | VARCHAR(10) | Unique identifier for the agent. |
| `customer_name`| VARCHAR(100)| Customer name. |
| `call_date` | DATE | Date the call occurred. |
| `call_time` | TIME | Time the call occurred. |
| `duration_minutes`| INT | Length of the call in minutes. |
| `call_type` | VARCHAR(50) | Category (Billing, Technical Support, Inquiry, Complaints). |
| `resolution_status`| VARCHAR(50) | Current status (Resolved, Pending, Escalated). |
| `csat_score` | INT | Customer satisfaction score (1-5). |

---

## Analytical Capabilities

The provided queries allow you to extract the following critical business insights:

1. **Macro KPIs:** Overview of total volume, average handling time, and overall resolution rates.
2. **Operational Metrics:** Performance benchmarking by call type to identify resource-heavy categories.
3. **Agent Matrix:** Identifying top performers versus those requiring additional training based on CSAT and escalation volume.
4. **Root Cause Analysis:** Auditing high-friction calls (long duration + low satisfaction).
5. **Trend Analysis:** Monitoring daily escalation spikes using CTEs.
6. **Time Management:** Pinpointing peak hours and their correlation to call duration and escalations.
7. **Pending Issues:** Tracking aging, unresolved tickets for management follow-up.
8. **Risk Assessment:** Measuring the escalation likelihood across different call types.

---

## Setup Instructions

### 1. Requirements
* MySQL Server
* A SQL IDE (e.g., MySQL Workbench, DBeaver)

### 2. Initialization
1. **Create Schema:** Execute `call_center_schema.sql` in your MySQL environment.
2. **Import Data:** * Update the `LOAD DATA LOCAL INFILE` path in `call_center_schema.sql` to point to the absolute path of your `call_center_data.csv` file.

### 3. Running Analytics
Execute the queries provided in `call_center_queries.sql` to generate reports. The queries include embedded insight comments to help interpret the data immediately after execution.

---

## Key Insight Sample: Risk Analysis by Call Type

This query identifies that "Complaints" are a significant risk, with a 60% escalation rate compared to 0% for "Inquiries":

``` sql
SELECT 
    call_type, 
    COUNT(call_id) AS total_calls, 
    SUM(CASE WHEN resolution_status = 'Escalated' THEN 1 ELSE 0 END) AS escalated_calls, 
    ROUND(SUM(CASE WHEN resolution_status = 'Escalated' THEN 1 ELSE 0 END) * 100.0 / COUNT(call_id), 2) AS escalation_rate_pct 
FROM 
    call_records 
GROUP BY 
    call_type 
ORDER BY 
    escalation_rate_pct DESC;
```

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.