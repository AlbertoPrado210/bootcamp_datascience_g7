from tkinter import *
from tkinter import messagebox


def saludar():
    nombre = txt_nombre.get()
    print(f"Hola {nombre}, bienvenido a Tkinter!")
    messagebox.showinfo("Saludo", f"Hola {nombre}, bienvenido a Tkinter!")


# Crear la ventana principal
app = Tk()
app.title("Mi primera app con Tkinter")
app.geometry("300x200")

# agregar un objeto
frame = Frame(app)
frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

#agregar un objeto label
lb_dni = Label(frame, text="DNI: ")
lb_dni.grid(row=1, column=0, pady=10)

lb_nombre = Label(frame, text="Nombre: ")
lb_nombre.grid(row=3, column=0, pady=10)

lb_email = Label(frame, text="Email: ")
lb_email.grid(row=5, column=0, pady=10)

#agregar un objeto Entry
txt_dni = Entry(frame)
txt_dni.grid(row=1, column=1)

txt_nombre = Entry(frame)
txt_nombre.grid(row=3, column=1)

txt_email = Entry(frame)
txt_email.grid(row=5, column=1)

#agregar un objeto Button
btn_saludar = Button(frame, text="Insertar nuevo alumno", command=saludar)
btn_eliminar = Button(frame, text="Eliminar Alumno", command=saludar)
btn_saludar.grid(row=7, column=1, columnspan=3)
btn_eliminar.grid(row=8, column=1, columnspan=3)



app.mainloop()