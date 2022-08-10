from xml.dom.minidom import Notation


class Alumno:
    nombre = None
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirAlumno(self):
        print("Alumno : " + self.nombre)
        print("Nota : " + str(self.nota))

    def resultadoAlmuno(self):
        if self.nota < 4:
            print (f"Alumno : {self.nombre} REPROBADO")
        else:
            print (f"Alumno : {self.nombre} APROBADO")

alumno1 = Alumno("Rodrigo Ramirez", 3)
alumno2 = Alumno("Rosario Silva", 7)

alumno1.imprimirAlumno()
alumno1.resultadoAlmuno()

alumno2.imprimirAlumno()
alumno2.resultadoAlmuno()