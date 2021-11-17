-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE cities(
    id INT UNIQUE AUTO NOT NULL,
    state_id INT NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);
