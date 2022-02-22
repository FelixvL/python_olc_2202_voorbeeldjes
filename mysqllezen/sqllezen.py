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

#rows = dict(zip(decursor.column_names, decursor.fetchone()))

#print("{last_name}, {first_name}: {hire_date}".format(row))

print(decursor.column_names)
for student in destudenten:
    print(student[4])


print("u wilt iets invullen: naamstudent")
invoer = input()


print(invoer)

sqlstatement = "INSERT INTO student (voornaam, lengte, geboortedatum, stad) VALUES (%s, %s,%s,%s)"
waarden = (invoer, 34, '2002-02-02','Eindhoven')

decursor.execute(sqlstatement, waarden)

dedb.commit()