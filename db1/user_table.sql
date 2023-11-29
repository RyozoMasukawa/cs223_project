-- db1/user_table.sql
CREATE TABLE User (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Accolade BOOLEAN,
    Story TEXT
);
