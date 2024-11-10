from flask import Flask, render_template
# Flask: Flask is a micro web framework used to create web applications in Python.
# render_template: This function allows us to render HTML templates. 
# It will look for templates in a templates directory (by default) and pass any necessary data to the HTML template.
import psycopg2
# psycopg2: This is a library used to connect to a PostgreSQL database in Python.
import psycopg2.extras 
# psycopg2.extras: This module provides additional tools for working with PostgreSQL,
# like custom cursor types.

app = Flask(__name__)
# app: Creates an instance of the Flask class. This app object is essential as it represents
# the application and is used to configure and define routes.

def get_db_connection():
# get_db_connection(): This function establishes a connection to a PostgreSQL database.
    conn = psycopg2.connect(
    # psycopg2.connect: Establishes a connection to the database using the provided credentials:
        dbname="mydatabase",
        # dbname: The name of the database to connect to ("mydatabase" here).
        user="user",
        # user: The username for the database.
        password="password",
        # password: The password for the database user.
        host="db",
        # host: The hostname of the database server ("db"),
        # which could be a hostname like "localhost" or an IP address.
        port="5432"
        # port: The database port, default for PostgreSQL is 5432.
    )
    return conn
    # conn: This connection object, conn,
    # is returned by the function, allowing other functions to interact with the database.

@app.route('/')
# @app.route('/'): This decorator registers a URL route to this view function. In this case,
# it’s the root URL (/), so visiting http://localhost:5000/ will trigger this function.
def index():
# index(): This function defines what happens when a user navigates to the root URL.
    conn = get_db_connection()
    # conn = get_db_connection(): Calls the get_db_connection function to connect to the database.
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor):
    # Creates a cursor object to execute SQL commands. By using DictCursor,
    # each row fetched from the database is returned as a dictionary,
    # allowing column access by name instead of by index.
    cursor.execute('SELECT * FROM items')
    # cursor.execute('SELECT * FROM items'):
    # Executes an SQL query to retrieve all rows from the items table.
    items = cursor.fetchall()
    # items = cursor.fetchall():
    # Fetches all rows from the result of the query and stores them in the items variable.
    cursor.close()
    # cursor.close(): Closes the cursor to free up resources.
    conn.close()
    # conn.close(): Closes the connection to the database, ending the session.
    return render_template('index.html', items=items)
    # render_template('index.html', items=items):
    # Renders an HTML template called index.html (located in the templates folder).
    # The items data is passed to the template, making it accessible for rendering in the HTML file.

if __name__ == '__main__':
#if name == 'main': This conditional checks if the script is being run directly (not imported as a module).
# If it is, the application is launched.
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000): Starts the Flask web server:
    # debug=True: Enables debug mode, which provides helpful error messages
    # and enables automatic reloading on code changes.
    # host='0.0.0.0': Makes the app accessible to any IP address on the network.
    # port=5000: Specifies the port on which the app will listen for requests.
