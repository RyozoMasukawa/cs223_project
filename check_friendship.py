import mysql.connector

def check_friendship():
    try:
        # Establish a connection to your MySQL database
        root_user = "root"
        root_pass = "root_password"
        
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port="3308",
            user=root_user,
            password=root_pass,
            database="db2"
        )

        # Create a cursor object to execute SQL queries
        cursor= connection.cursor()

        # Start the transaction
        cursor.execute("START TRANSACTION")

        # T1,1: Check the existence of user id x1
        cursor.execute(f"SELECT * FROM Follow")
        friendship = cursor.fetchone()
        print(friendship)
        
        # Commit the transaction
        cursor.execute("COMMIT")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Example usage
check_friendship()
