import mysql.connector
import argparse

def execute_transaction(user3_id, show):
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

        # Create a cursor object to execute SQL queries
        cursor1= connection1.cursor()

        # Start the transaction
        cursor1.execute("START TRANSACTION")

        # T1,1: Check the existence of user id x1
        cursor1.execute(f"SELECT COUNT(*) FROM User WHERE id = %s", (user3_id,))
        user1_exists = cursor1.fetchone()[0]


        # T1,3: Update user x1’s friend list
        # T1,4: Update user x2’s friend list
        if user1_exists > 0:
            cursor1.execute(f"SELECT * FROM User WHERE id = %s", (user3_id,))
            user1_info = cursor1.fetchone()
            if show:
                print(user1_info)
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
        connection1.close()

# Example usage
parser = argparse.ArgumentParser(description="My parser")
if __name__=="__main__":
    parser.add_argument('--user1id', type=int,default=1, help='an integer for the ac\
cumulator')
    parser.add_argument('--show', action='store_true', default=False)
    args = parser.parse_args()
    execute_transaction(args.user1id, args.show)
