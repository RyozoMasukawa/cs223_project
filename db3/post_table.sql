-- db3/post_table.sql
CREATE TABLE Post (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    User INT,
    Content TEXT,
    Likes INT DEFAULT 0,
    Comments INT DEFAULT 0,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (User) REFERENCES User(ID)
);
