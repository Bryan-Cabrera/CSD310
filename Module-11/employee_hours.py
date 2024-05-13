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
    # Create database connection
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format("root", "127.0.0.1", "movies"))

    cursor = db.cursor()

    # Execute query to retrieve employee work hours data
    query = """
            SELECT e.name AS 'Employee Name', eh.overtime_hours AS 'Overtime Hours', eh.hours_worked AS 'Total Hours Worked'
            FROM Employees e
            INNER JOIN EmployeeHours eh ON e.employee_id = eh.employee_id
            """
    cursor.execute(query)

    # Get all rows from the result set
    employee_work_hours = cursor.fetchall()

    # Print Employee Work Hours Report
    print("\nEmployee Work Hours Report:")
    for row in employee_work_hours:
        print("Employee Name: {}, Overtime Hours: {}, Total Hours Worked: {}".format(row[0], row[1], row[2]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Please check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
