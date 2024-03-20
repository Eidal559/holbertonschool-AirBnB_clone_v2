-- setup_mysql_dev.sql
-- Check if the database exists, and create it if it does not
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if the user exists, create the user if it does not
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Ensure the user has SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes made by GRANT statements
FLUSH PRIVILEGES;
