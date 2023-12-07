import mysql.connector

def create_tables(database_config, tables):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**database_config)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        for table_name, table_definition in tables.items():
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {table_definition}")

        # Commit the changes
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Define table definitions for each MySQL server
db1_tables = {
    "User": """
        (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            DateOfBirth DATE,
            Email VARCHAR(255),
            Accolade BOOLEAN,
            Numpost INT,
            Numfollow INT
        )
    """
}

db2_tables = {
    "Follow": """
        (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            User1 INT,
            User2 INT,
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
}

db3_tables = {
    "Post": """
        (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            User INT,
            Content TEXT,
            Likes INT,
            Comments INT,
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "Comment": """
        (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            User INT,
            Post INT,
            Text TEXT,
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Upvotes INT
        )
    """
}


# Example usage for mysql_container_1
root_user = "root"
root_password = "root_password"
database_config_1 = {
    "host": "127.0.0.1",
    "port": "3307",
    "user": root_user,
    "password": root_password,
    "database": "db1"
}

# Example usage for mysql_container_2
database_config_2 = {
    "host": "127.0.0.1",
    "port": "3308",
    "user": root_user,
    "password": root_password,
    "database": "db2"
}

# Example usage for mysql_container_3
database_config_3 = {
    "host": "127.0.0.1",
    "port": "3309",
    "user": root_user,
    "password": root_password,
    "database": "db3"
}

# Create tables in each MySQL server
create_tables(database_config_1, db1_tables)
create_tables(database_config_2, db2_tables)
create_tables(database_config_3, db3_tables)
