CREATE DATABASE employee_management;

USE employee_management;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);