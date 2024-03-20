-- setup_mysql_test.sql
-- Check if the test database exists, and create it if it does not
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the test user exists, create the user if it does not
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the test database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Ensure the test user has SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes made by GRANT statements
FLUSH PRIVILEGES;
