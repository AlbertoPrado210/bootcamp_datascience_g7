class Alumno:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Hola, soy {self.nombre} y mi email es {self.email}.")
        
        
class Profesor:
    def __init__(self, nombre, email, especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad

    def mostrar(self):
        print(f"Hola, soy {self.nombre}, mi email es {self.email} y enseño {self.especialidad}.")
        
alumno = Alumno("Juan Perez", "jpe@gmail.com")
alumno.mostrar()

profesor = Profesor("Ana Gomez", "agomez@universidad.con", "Data Analytics")
profesor.mostrar()