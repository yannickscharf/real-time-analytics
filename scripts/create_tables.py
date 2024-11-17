import psycopg2

def create_tables(conn):

    # Definition of tables schemas
    # Raw data table
    process_times_table = '''
        CREATE TABLE IF NOT EXISTS ProcessTimes (
        id SERIAL PRIMARY KEY,
        StationGroup VARCHAR(255) NOT NULL,
        StationName VARCHAR(255) NOT NULL,
        UnitIdType VARCHAR(255) NOT NULL,
        SerialNumber VARCHAR(255) NOT NULL,
        Value NUMERIC(10, 3) NOT NULL,
        TimeStamp TIMESTAMP WITH TIME ZONE NOT NULL
            );
    '''

    # Processed data table
    processed_data_table = '''
        CREATE TABLE IF NOT EXISTS ProcessedData (
        id SERIAL PRIMARY KEY,
        StationGroup VARCHAR(255) NOT NULL,
        StationName VARCHAR(255) NOT NULL,
        UnitIdType VARCHAR(255) NOT NULL,
        SerialNumber VARCHAR(255) NOT NULL,
        Value NUMERIC(10, 3) NOT NULL,
        TimeStamp TIMESTAMP WITH TIME ZONE NOT NULL,
        ProcessedValue NUMERIC(10, 3) NOT NULL
            );
    '''
    
    # Create tables
    try:
        with conn.cursor() as cursor:
            cursor.execute(process_times_table)
            cursor.execute(processed_data_table)
            conn.commit()
            print("Table ProcessTimes created successfully.")
            print("Table ProcessedData created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
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
        conn = psycopg2.connect(
            dbname=db_params['dbname'],
            user=db_params['user'],
            password=db_params['password'],
            host=db_params['host'],
            port=db_params['port']
        )
        print("Database connection established.")
        
        # Create tables
        create_tables(conn)
        
    except Exception as e:
        print(f"Error connecting to the database: {e}")

    finally:
        if conn:
            conn.close()
            print("Database connection closed.")
