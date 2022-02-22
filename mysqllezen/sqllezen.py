import mysql.connector

print("sql")

dedb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",  # mac doet hier "root"
    database="olc2202database"
)

decursor = dedb.cursor()

decursor.execute("SELECT * FROM student")

destudenten = decursor.fetchall()

print(destudenten)