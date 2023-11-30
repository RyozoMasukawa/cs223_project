import mysql.connector

def execute_transaction(user4_id):
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
        cursor1.execute(f"SELECT COUNT(*) FROM User WHERE id = %s", (user4_id,))
        user4_exists = cursor1.fetchone()[0]


        # T1,3: Update user x1’s friend list
        # T1,4: Update user x2’s friend list
        if user4_exists > 0:
            cursor3.execute("START TRANSACTION")
            cursor3.execute("UPDATE Comment SET Upvotes=Upvotes+1 WHERE ID = 2")
            cursor3.execute("UPDATE Comment SET Upvotes=Upvotes+1 WHERE ID = 1")
            cursor3.execute("SELECT Upvotes FROM Comment WHERE ID = 2")
            num_upvotes = cursor3.fetchone()[0]
            if num_upvotes >= 0:
                cursor1.execute("UPDATE User SET Accolade=1 WHERE ID = %s", (1,))
            cursor3.execute("COMMIT")
            cursor1.execute("COMMIT")            
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
user4_id = 4
execute_transaction(user4_id)
