import subprocess

# Function to initialize the database and insert the raw data
def init_database():
    try:
        result = subprocess.run(["python", "scripts/init_database.py"], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running init_database: {e}")

if __name__ == "__main__":
    init_database()