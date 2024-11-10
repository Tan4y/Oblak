# db_init.py
import psycopg2

def initialize_db():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    # Insert some sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM items")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO items (name) VALUES (%s)", ('Item 1',))
        cursor.execute("INSERT INTO items (name) VALUES (%s)", ('Item 2',))
        cursor.execute("INSERT INTO items (name) VALUES (%s)", ('Item 3',))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    initialize_db()
