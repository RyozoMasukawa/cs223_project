-- db3/comment_table.sql
CREATE TABLE Comment (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    User INT,
    Post INT,
    Text TEXT,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Upvotes INT DEFAULT 0,
    FOREIGN KEY (User) REFERENCES User(ID),
    FOREIGN KEY (Post) REFERENCES Post(ID)
);
