class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Alumno(Persona):
    def __init__(self, nombre, email, nota):
        super().__init__(nombre, email)
        self.nota = nota
        
    def mostrar_alumno(self):
        super().mostrar()
        print(f"Nota: {self.nota}")

class Profesor(Persona):
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad

    def mostrar(self):
        print("===== DATOS DEL PROFESOR =====")
        super().mostrar()
        print(f"Especialidad: {self.especialidad}")
        
alumno1 = Alumno("Juan Perez", "jpe@gmail.com", 20)
#alumno.mostrar()

profesor1 = Profesor("Ana Gomez", "agomez@universidad.con", "Data Analytics")
#profesor.mostrar()

# Funcion que usa polimorfismo
def presentar_datos(persona):
    persona.mostrar()
    
presentar_datos(alumno1)
presentar_datos(profesor1)