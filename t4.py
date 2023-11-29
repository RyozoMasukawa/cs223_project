import mysql.connector

def execute_transaction(user3_id):
    try:
        # Establish a connection to your MySQL database
        root_user = "root"
        root_pass = "root_password"
        
        connection1 = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user=root_user,
            password=root_pass,
            database="db1"
        )

        connection3 = mysql.connector.connect(
            host="127.0.0.1",
            user=root_user,
            port="3308",
            password=root_pass,
            database="db3"
        )

        # Create a cursor object to execute SQL queries
        cursor1= connection1.cursor()
        cursor3= connection3.cursor()

        # Start the transaction
        cursor1.execute("START TRANSACTION")

        # T1,1: Check the existence of user id x1
        cursor1.execute(f"SELECT COUNT(*) FROM User WHERE id = %s", (user3_id,))
        user3_exists = cursor1.fetchone()[0]


        # T1,3: Update user x1’s friend list
        # T1,4: Update user x2’s friend list
        if user3_exists > 0:
            cursor3.execute("INSERT INTO Comment (ID, User, Post, Text, Timestamp, Upvotes) VALUES (1, 3, 2, %s, NOW(), 0);", ("That's cool bro!",))
            cursor3.execute("UPDATE Post SET Comments=Comments+1 WHERE ID=2")
            cursor3.execute("COMMIT")
            
        else:
            # Rollback the transaction if users do not exist
            cursor1.execute("ROLLBACK")
            raise ValueError("ABORT TRANSACTION: Users do not exist.")        

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor1.close()
        cursor3.close()
        connection1.close()
        connection3.close()

# Example usage
user3_id = 3
execute_transaction(user3_id)
