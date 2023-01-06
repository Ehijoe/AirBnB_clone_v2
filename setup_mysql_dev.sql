-- Setup the dev database and user

-- Create the dev database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the user the privilege to use all databases
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant the user the privilege to query the performance_schema database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Grant the user all privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
