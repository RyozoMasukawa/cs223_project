-- Add User 1 with random values
USE db1;
INSERT INTO User (Name, DateOfBirth, Email, Accolade, Story)
VALUES (
    CONCAT('User1_', FLOOR(RAND() * 10000)),
    DATE_ADD('1970-01-01', INTERVAL FLOOR(RAND() * 365*50) DAY),
    CONCAT('user1_', FLOOR(RAND() * 10000), '@example.com'),
    0,
    'Random story for User 1'
);

-- Add User 2 with random values
INSERT INTO User (Name, DateOfBirth, Email, Accolade, Story)
VALUES (
    CONCAT('User2_', FLOOR(RAND() * 10000)),
    DATE_ADD('1970-01-01', INTERVAL FLOOR(RAND() * 365*50) DAY),
    CONCAT('user2_', FLOOR(RAND() * 10000), '@example.com'),
    RAND() > 0.5,
    'Random story for User 2'
);

-- Add User 3 with random values
INSERT INTO User (Name, DateOfBirth, Email, Accolade, Story)
VALUES (
    CONCAT('User3_', FLOOR(RAND() * 10000)),
    DATE_ADD('1970-01-01', INTERVAL FLOOR(RAND() * 365*50) DAY),
    CONCAT('user3_', FLOOR(RAND() * 10000), '@example.com'),
    RAND() > 0.5,
    'Random story for User 3'
);

-- Add User 4 with random values
INSERT INTO User (Name, DateOfBirth, Email, Accolade, Story)
VALUES (
    CONCAT('User1_', FLOOR(RAND() * 10000)),
    DATE_ADD('1970-01-01', INTERVAL FLOOR(RAND() * 365*50) DAY),
    CONCAT('user1_', FLOOR(RAND() * 10000), '@example.com'),
    0,
    'Random story for User 1'
);
