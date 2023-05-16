-- script that converts db to UTF8

USE hbtn_0c_0
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table COLLATE utf8mb4_unicode_ci;
