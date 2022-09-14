import sqlite3

db_connection = sqlite3.connect('ejercicio01.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Rodrigo', 'Ramirez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Jose', 'Larrain')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Gustavo', 'Perez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Fabiola', 'Quinteros')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Ignacio', 'Borghi')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Rosario', 'Gallego')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Marcelo', 'Borghi')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Juan', 'Gallego')")

db_connection.commit()
db_cursor.execute("SELECT * FROM Alumnos WHERE Id = 3")
filas = db_cursor.fetchall()

print(filas)

db_connection.close()