-- MYSQL tests base setup

CREATE DATABASE IF NOT EXISTS RecruitMe_test_db;
CREATE USER IF NOT EXISTS 'RecruitMe_test'@'localhost' IDENTIFIED BY 'RecruitMe_test_pwd';
GRANT ALL PRIVILEGES ON RecruitMe_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'RecruitMe_test'@'localhost';
FLUSH PRIVILEGES;
