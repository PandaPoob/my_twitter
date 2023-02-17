SELECT * FROM customers;
--sort ascending
SELECT * FROM customers ORDER BY companyname ASC;
--sort descending
SELECT * FROM customers ORDER BY companyname DESC;

SELECT * FROM products;

--------- Aggregate functions ---------

-- Get most expensive product
SELECT MAX(unitprice) AS max_product_price FROM products;
-- Get cheapest product
SELECT MIN(unitprice) AS min_product_price FROM products;
-- Get average price
SELECT AVG(unitprice) FROM products;
-- Get total number of products
SELECT COUNT(*) FROM products;
-- ALIAS, choose what the key should be named
SELECT COUNT(*) AS total_products FROM products;

-- Pagination first number: from where, second number: how many
--SELECT * FROM products LIMIT 15, 5;
SELECT * FROM products LIMIT 0, 5;
-- Get 5 products and order by cheapest to highest
SELECT * FROM products ORDER BY unitprice ASC LIMIT 0, 5;

--LIKE/include for search, WILDCARD: % means + everything after
SELECT * FROM customers WHERE contactname LIKE "m%";
--Get everything that ends with r
SELECT * FROM customers WHERE contactname LIKE "%r";
--Something in the begining and contains "wa" and something after
SELECT * FROM customers WHERE contactname LIKE "%wa%";

--Tweet elon + message with the word elon + users with elon
--Full text search

--join two tables
SELECT Orders.OrderID, Customers.ContactName, Orders.OrderDate, Customers.Country
FROM Orders
-- on: get customers that who order.id = customer id
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID ORDER BY Orders.OrderDate DESC;

--santiagos
SELECT * FROM orders
JOIN customers
ON orders.customerid = customers.customerid
WHERE customers.customerid = "VINET" LIMIT 0,2;

--double join
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerID, Customers.ContactName, Products.ProductID, Products.ProductName 
FROM orders 
JOIN Customers ON Orders.CustomerID=Customers.CustomerID
JOIN "Order Details" ON "Order Details".OrderID=Orders.OrderID
JOIN Products ON "Order Details".ProductID=Products.ProductID
WHERE customers.customerid = "VINET";

--WHERE customers.customerid = "elon"


