-- ============================================================================
-- 12_Call_Center_Database/call_center_queries.sql
-- Description: Analytical queries to extract operational KPIs, agent 
--              performance, and quality control metrics from call center data.
-- ============================================================================

USE call_center_db;

-- ----------------------------------------------------------------------------
-- 1. MACRO KPIs: Overall Call Center Performance
-- Useful for high-level dashboard metrics
-- ----------------------------------------------------------------------------
SELECT 
    COUNT(call_id) AS total_calls,
    ROUND(AVG(duration_minutes), 2) AS avg_handling_time_mins,
    ROUND(AVG(csat_score), 2) AS overall_avg_csat,
    SUM(CASE WHEN resolution_status = 'Resolved' THEN 1 ELSE 0 END) / COUNT(call_id) * 100 AS resolution_rate_pct
FROM 
    call_records;
-- Insight: 
-- The call center processed exactly 100 calls during this period, achieving a moderate overall customer satisfaction (CSAT) score of 3.73 out of 5.
-- The resolution rate is 66%, meaning exactly one-third of all customer interactions remain pending or required escalation, with an average handling time of ~17.3 minutes per call.

-- ----------------------------------------------------------------------------
-- 2. OPERATIONAL METRICS: Call Volume and AHT by Call Type
-- Identifies which types of inquiries drain the most resources
-- ----------------------------------------------------------------------------
SELECT 
    call_type,
    COUNT(call_id) AS total_calls,
    ROUND(AVG(duration_minutes), 2) AS avg_duration,
    MAX(duration_minutes) AS max_duration,
    ROUND(AVG(csat_score), 2) AS avg_csat
FROM 
    call_records
GROUP BY 
    call_type
ORDER BY 
    total_calls DESC;
-- Insight: 
-- "Inquiry" and "Billing" represent the bulk of the call volume (58%) and enjoy high satisfaction scores (>4.10) with quick handling times. 
-- Conversely, "Complaints" and "Technical Support" severely drain resources, averaging 23 to 30+ minutes per call, and suffer from critically low CSAT scores (2.15 and 3.32, respectively).

-- ----------------------------------------------------------------------------
-- 3. QUALITY CONTROL: Agent Performance Matrix
-- Evaluates individual agents based on satisfaction and handling time
-- ----------------------------------------------------------------------------
SELECT 
    agent_id,
    COUNT(call_id) AS calls_handled,
    ROUND(AVG(duration_minutes), 2) AS avg_handling_time,
    ROUND(AVG(csat_score), 2) AS avg_csat_score,
    SUM(CASE WHEN resolution_status = 'Escalated' THEN 1 ELSE 0 END) AS total_escalations
FROM 
    call_records
GROUP BY 
    agent_id
ORDER BY 
    avg_csat_score DESC, calls_handled DESC;
-- Insight: 
-- Call distribution is perfectly balanced, with all 5 agents handling exactly 20 calls each. 
-- Agents A03 and A04 are top performers (CSAT > 4.2, lowest escalation rates), whereas Agent A01 is struggling significantly, logging the highest average handling time (21.15 mins) and the highest number of escalations (7).

-- ----------------------------------------------------------------------------
-- 4. ROOT CAUSE ANALYSIS: Long Calls with Poor Satisfaction
-- Isolating specific records for targeted quality audits
-- ----------------------------------------------------------------------------
SELECT 
    call_id,
    agent_id,
    customer_name,
    call_type,
    duration_minutes,
    csat_score,
    resolution_status
FROM 
    call_records
WHERE 
    duration_minutes > 20 
    AND csat_score <= 2
ORDER BY 
    duration_minutes DESC;
-- Insight: 
-- There are 19 critical calls flagged for lasting over 20 minutes while yielding a CSAT of 2 or lower. 
-- The vast majority of these troublesome calls are categorized as "Complaints," and Agents A01 and A05 are disproportionately responsible for these specific, highly-dissatisfied interactions.

-- ----------------------------------------------------------------------------
-- 5. ADVANCED ANALYSIS: Daily Escalation Rate (Using CTE)
-- Tracks if escalation issues are spiking on specific dates
-- ----------------------------------------------------------------------------
WITH DailyStats AS (
    SELECT 
        call_date,
        COUNT(call_id) AS daily_total_calls,
        SUM(CASE WHEN resolution_status = 'Escalated' THEN 1 ELSE 0 END) AS daily_escalations
    FROM 
        call_records
    GROUP BY 
        call_date
)
SELECT 
    call_date,
    daily_total_calls,
    daily_escalations,
    ROUND((daily_escalations / daily_total_calls) * 100, 2) AS escalation_rate_pct
FROM 
    DailyStats
ORDER BY 
    call_date ASC;
-- Insight: 
-- The center's daily escalation rate generally stabilizes around 16% to 20%, maintaining a relatively steady daily call volume of 5-7 calls. 
-- However, there were significant performance dips on June 25th (28.6% escalation rate) and June 28th (33.3%), contrasting heavily with zero-escalation days on June 26th and July 9th.

-- ----------------------------------------------------------------------------
-- 6. TIME MANAGEMENT: Peak Hour Analysis
-- Identifies busiest hours and when escalations are most likely to occur
-- ----------------------------------------------------------------------------
SELECT 
    SUBSTR(call_time, 1, 2) AS hour_of_day, 
    COUNT(call_id) AS total_calls, 
    ROUND(AVG(duration_minutes), 2) AS avg_duration, 
    SUM(CASE WHEN resolution_status = 'Escalated' THEN 1 ELSE 0 END) AS escalations 
FROM 
    call_records 
GROUP BY 
    hour_of_day 
ORDER BY 
    hour_of_day ASC;
-- Insight: 
-- Call volume spikes at two distinct times: 
--     1. mid-morning (9:00 AM - 10:59 AM) and early afternoon (1:00 PM - 2:59 PM). 
--     2. The 9:00 AM hour is particularly problematic, representing not only high volume but also the highest average call duration (21.13 minutes) and the highest number of escalations (5).

-- ----------------------------------------------------------------------------
-- 7. WORKFLOW: Pending Issue Tracker
-- Isolates calls that require immediate follow-up, sorted by age and severity
-- ----------------------------------------------------------------------------
SELECT 
    call_id, 
    agent_id, 
    call_type, 
    call_date, 
    duration_minutes 
FROM 
    call_records 
WHERE 
    resolution_status = 'Pending' 
ORDER BY 
    call_date ASC, 
    duration_minutes DESC;
-- Insight: 
-- There are currently 16 calls sitting in a "Pending" state, effectively tying up resources. 
-- The oldest unresolved issue (C1025) has been pending since June 25th, and several of these open tickets (like C1043 and C1083) represent interactions that already consumed over 30 minutes of agent time.

-- ----------------------------------------------------------------------------
-- 8. RISK ANALYSIS: Escalation Rate by Call Type
-- Directly measures the likelihood of a call category requiring upper management
-- ----------------------------------------------------------------------------
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
-- Insight: 
-- There is a massive operational divide: "Inquiry" and "Billing" calls have a 0% escalation rate, meaning agents handle them perfectly. 
-- Meanwhile, an alarming 60% of all "Complaints" and 27% of "Technical Support" calls result in escalations, indicating a severe lack of agent empowerment or training in handling high-friction issues.