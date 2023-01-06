-- Setup the test database and user

-- Create the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the user the privilege to use all databases
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- Grant the user the privilege to query the performance_schema database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Grant the user all privileges on the hbnb_test_db database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
