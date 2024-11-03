import pandas as pd
from sqlalchemy import create_engine, text

def create_tables(engine):
    # Definition of tables schemas
    raw_data_table = '''
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
    
    # Create tables
    try:
        with engine.connect() as connection:
            connection.execute(text(raw_data_table))
        print("Table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data(engine):
    try:
        # Read the JSON file
        data = pd.read_json('data/processtimes.json')
        
        # Insert the data into the table
        data.to_sql('ProcessTimes', engine, if_exists='append', index=False)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

if __name__ == "__main__":
    from sqlalchemy import create_engine

    # Database connection parameters
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'example',
        'host': 'postgres',
        'port': '5432'
    }

    # Connection string
    con_str = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"

    # Create engine
    engine = create_engine(con_str)

    create_tables(engine)
    insert_data(engine)