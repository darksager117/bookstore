from tkinter import *
import backend

def view_command():
    list1.delete(0,END)  #se pone antes de que el for entre a la lista para que no se repita la operacion, si se pone despues, la lista se elimina.
    for row in backend.view():
        list1.insert(END, row)    #"""pyinstaller --onefile --windowed frontend.py / INSTALAR PYINSTALLER"""

def search_command():
    list1.delete(0,END)
    for row in backend.search(entry_title.get(),entry_author.get(), entry_year.get(),  entry_id.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(entry_title.get(),entry_author.get(), entry_year.get(),  entry_id.get())
    list1.delete(0,END)   #limpia la lista
    list1.insert(END,entry_title.get(),entry_author.get(), entry_year.get(),  entry_id.get())

def get_selected_row(event):             #funcion para enlazar la accion de seleccionar lista con el boton delete
    global selected_tuple                #Se declara global para poder usarse en la funcion delete
    index=list1.curselection()[0]        #se ubica el cursor en la lista seleccionada , ID index de 0
    selected_tuple=list1.get(index)      #Se extrae toda la informacion por el id
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])        #title index 1
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], entry_title.get(),entry_author.get(), entry_year.get(),  entry_id.get())


window= Tk()

window.wm_title("BookStore")

la1= Label(window, text="Title")
la1.grid(row=0, column=0)

la2= Label(window, text="Year")
la2.grid(row=1, column=0)

la3= Label(window, text="Author")
la3.grid(row=0, column=2)

la4= Label(window, text="ISBN")
la4.grid(row=1, column=2)

entry_title=StringVar()
e1= Entry(window, textvariable=entry_title)
e1.grid(row=0, column=1)

entry_author=StringVar()
e2= Entry(window, textvariable=entry_author)
e2.grid(row=0, column=3)

entry_year=StringVar()
e3= Entry(window, textvariable=entry_year)
e3.grid(row=1, column=1)

entry_id=StringVar()
e4= Entry(window, textvariable=entry_id)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scbar=Scrollbar(window)
scbar.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scbar.set)
scbar.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)    #Enlazar el scroll con la lista

b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
