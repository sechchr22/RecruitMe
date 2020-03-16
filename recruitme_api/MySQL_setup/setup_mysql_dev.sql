-- MYSQL server setup
DROP USER RecruitMe_dev@localhost;
FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS RecruitMe_dev_db;
CREATE USER IF NOT EXISTS 'RecruitMe_dev'@'localhost' IDENTIFIED BY 'RecruitMe_dev_pwd';
GRANT ALL PRIVILEGES ON RecruitMe_dev_db.* TO 'RecruitMe_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'RecruitMe_dev'@'localhost';
FLUSH PRIVILEGES;
