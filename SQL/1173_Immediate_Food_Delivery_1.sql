/*
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key of this table.
The table holds information about food delivery 
to customers that make orders at some date and 
specify a preferred delivery date (on the same order date or after it).


If the preferred delivery date of the customer is the 
same as the order date then the order is called 
immediate otherwise it's called scheduled.

Write an SQL query to find the percentage of 
immediate orders in the table, rounded to 2 decimal places.
*/

SELECT
ROUND(100* SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END AS)/COUNT(*), 2) AS immediate_percentage
FROM Delivery 
