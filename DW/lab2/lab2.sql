--- TASK 1 ---
--- Show all data about all customers sorted by customer last_name (a-z)

SELECT *
FROM CUSTOMER
ORDER BY LAST_NAME;

--- TASK 2 ---
--- Show all data about all customers sorted by customer last_name (z-a)

SELECT *
FROM CUSTOMER
ORDER BY LAST_NAME DESC;

-- TASK 3 ---
--- Show number of customers that are stored in the table customer
SELECT COUNT(*)
FROM CUSTOMER;

-- TASK 4 --
--- Customers with annual salary greater than 300000 SEK
SELECT COUNT(*)
FROM CUSTOMER
WHERE NVL(SALARY,0) > 300000

-- TASK 5 --
--- Customers with annual salary less than 300000 SEK
SELECT COUNT(*)
FROM CUSTOMER
WHERE NVL(SALARY,0) < 300000

-- TASK 6 --
--- Average annual income for all customers
SELECT AVG(NVL(SALARY,0)) as average_salary
FROM CUSTOMER;

-- TASK 7 --
--- username, firstname, lastname and salary for customer with 
-- salary below the average
SELECT USERNAME, FIRST_NAME, LAST_NAME, NVL(SALARY,0) SALARY
FROM CUSTOMER
WHERE NVL(SALARY,0) < (SELECT AVG(NVL(SALARY,0)) FROM CUSTOMER);

--TASK 8--
-- SHOW FIRST-NAME, LAST-NAME WITH UPPERCASE

SELECT UPPER(FIRST_NAME), UPPER(LAST_NAME)
FROM CUSTOMER
WHERE UPPER(LAST_NAME) LIKE '%S%'

--TASK 9--
-- SHOW FIRST-NAME, LAST-NAME PROFESSION WITH LOWERCASE
-- REPLACE NULL PROFESSION WITH 'jobless'

SELECT LOWER(FIRST_NAME), LOWER(LAST_NAME),  lower(nvl(profession,'jobless')) as profession
FROM CUSTOMER
WHERE LOWER(FIRST_NAME) LIKE '%s'

--TASK 10--
--The column headings should be profession and quantity.
--Replace null-values in the column profession with the string 'jobless'.
--Show profession capitalized. 

select Initcap(nvl(profession, 'jobless')) as profession ,count(*) as quantity
from customer
group by profession
order by profession desc

--TASK 11--
--Show first_name concatenated with a space and last_name under the heading customer_name. 
select Initcap(first_name)||' '||Initcap(last_name) as Customer_name
from customer
