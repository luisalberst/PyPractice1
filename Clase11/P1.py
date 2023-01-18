import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE IF NOT EXISTS students(Id INT, name TEXT, lastname TEXT)")

db_cursor.execute("INSERT INTO students VALUES(1,'Monica', 'García')")
db_cursor.execute("INSERT INTO students VALUES(2,'Jorge', 'Herrero')")
db_cursor.execute("INSERT INTO students VALUES(3,'Pepe', 'Martinez')")
db_cursor.execute("INSERT INTO students VALUES(4,'Pablo', 'Villanueva')")
db_cursor.execute("INSERT INTO students VALUES(5,'Francisco', 'Perez')")
db_cursor.execute("INSERT INTO students VALUES(6,'Clara', 'Santamaria')")
db_cursor.execute("INSERT INTO students VALUES(7,'Maria', 'Lopez')")
db_cursor.execute("INSERT INTO students VALUES(8,'Pepe', 'Rodriguez')")

db_connection.commit()

db_cursor.execute("SELECT * FROM students WHERE name LIKE '%P%'")

row = db_cursor.fetchall()

db_connection.close()

def unique(list):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print(x)

unique(row)