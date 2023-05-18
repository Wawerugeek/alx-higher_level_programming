-- creates a database and a table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id int not null, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id) );
