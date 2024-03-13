-- creates hbtn_0d_usa db
CREATE DATABASE IF NOT EXISTS "hbtn_0d_usa";
-- creates states table with a auto, unique, primary id
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id)
);
