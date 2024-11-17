import pandas as pd
import psycopg2

def insert_process_times(conn):

    # Queries
    check_query = 'SELECT COUNT(*) FROM ProcessTimes'
    insert_query = '''
        INSERT INTO ProcessTimes (StationGroup, StationName, UnitIdType, SerialNumber, Value, TimeStamp)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    
    try:
        with conn.cursor() as cursor:

            # Check if table contains data
            cursor.execute(check_query)
            count = cursor.fetchone()[0]
            if count > 0:
                print("Table ProcessTimes already contains data.")
            else:

                # Read the JSON file
                df = pd.read_json('data/processtimes.json')

                # Convert DataFrame to list of tuples
                data = list(df.itertuples(index=False, name=None))

                # Insert data into table
                cursor.executemany(insert_query, data)
                conn.commit()
                print("Data inserted successfully into ProcessTimes table.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

if __name__ == "__main__":

    # Database connection parameters
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'example',
        'host': 'postgres',
        'port': '5432'
    }

    # Establish connection
    try:
        conn = psycopg2.connect(**db_params)
        print("Database connection established.")

        # Insert data
        insert_process_times(conn)

    except Exception as e:
        print(f"Error connecting to the database: {e}")

    finally:
        if conn:
            conn.close()
            print("Database connection closed.")