import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Bry4na70r.",
    "host": "localhost",
	"port": 3306,
    "database": "Movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    if db.is_connected():
        print("Connection to MySQL database successful!")

        # Create a cursor object
        cursor = db.cursor()

        # First query: Select all fields for the studio table
        cursor.execute("SELECT * FROM studio")
        studio_result = cursor.fetchall()
        print("Studio Table:")
        for row in studio_result:
            print(row)
        print()

        # Second query: Select all fields for the genre table
        cursor.execute("SELECT * FROM genre")
        genre_result = cursor.fetchall()
        print("Genre Table:")
        for row in genre_result:
            print(row)
        print()

        # Third query: Select movie names for movies with a runtime of less than two hours
        cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
        runtime_less_than_two_hours = cursor.fetchall()
        print("Movies with Runtime Less Than Two Hours:")
        for row in runtime_less_than_two_hours:
            print(row[0])
        print()

        # Fourth query: Get a list of film names and directors grouped by director
        cursor.execute("SELECT film_name, film_director FROM film GROUP BY film_director, film_name")
        films_grouped_by_director = cursor.fetchall()
        print("Films Grouped by Director:")
        for row in films_grouped_by_director:
            print(f"Director: {row[1]} - Film: {row[0]}")
        print()

    else:
        print("Connection to MySQL database failed!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("Connection closed.")
