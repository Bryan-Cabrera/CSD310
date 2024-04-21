import mysql.connecter
from mysql.connecter import errorcode

config = {
	"user": "root",
	"password": "popcorn",
	"localhost": "3306",
	"database": "Movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	if db.is_connected():
       print("Connection to MySQL database successful!")
    else:
       print("Connection to MySQL database failed!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Connection closed.")