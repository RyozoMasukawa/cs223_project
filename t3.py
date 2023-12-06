import mysql.connector

def execute_transaction(user1_id, user2_id):
    try:
        # Establish a connection to your MySQL database
        root_user = "root"
        root_pass = "root_password"
        
        connection1 = mysql.connector.connect(
            host="127.0.0.1",
            port="3307",
            user=root_user,
            password=root_pass,
            database="db1"
        )

        connection3 = mysql.connector.connect(
            host="127.0.0.1",
            user=root_user,
            port="3309",
            password=root_pass,
            database="db3"
        )

        # Create a cursor object to execute SQL queries
        cursor1= connection1.cursor()
        cursor3= connection3.cursor()

        # Start the transaction
        cursor1.execute("START TRANSACTION")

        # T1,1: Check the existence of user id x1
        cursor1.execute(f"SELECT COUNT(*) FROM User WHERE id = %s", (user1_id,))
        user1_exists = cursor1.fetchone()[0]

        # T1,2: Check the existence of user id x2
        cursor1.execute("SELECT COUNT(*) FROM User WHERE id = %s", (user2_id,))
        user2_exists = cursor1.fetchone()[0]

        # T1,2: Check the existence of user id x2
        cursor3.execute("SELECT COUNT(*) FROM Post WHERE id = %s", (1,))
        post_exists = cursor3.fetchone()[0]

        # T1,3: Update user x1’s friend list
        # T1,4: Update user x2’s friend list
        if user1_exists > 0 and user2_exists > 0 and post_exists > 0:
            cursor3.execute("SELECT Content INTO @previous_content FROM Post WHERE id = 1;")
            cursor3.execute("INSERT INTO Post (User, Content, Likes, Comments, Timestamp) VALUES (1, CONCAT(@previous_content, 'Contents of s1'), 0, 0, NOW());")
            cursor3.execute("COMMIT")
            cursor1.execute("UPDATE User SET Numpost=Numpost+1 WHERE ID=%s", (user1_id,))
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
user1_id = 1
user2_id = 2
execute_transaction(user1_id, user2_id)


