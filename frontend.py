"""
Program to log and display crop plantings.
crop, quantity
date, outcome
notes

User can:
view all records
search for an entry
add an entry
update an entry
delete an entry
exit
"""

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    if list1.curselection():
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        print(index)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(crop_text.get(),quantity_text.get(),date_text.get(),outcome_text.get()):
        list1.insert(END,row)

def insert_command():
    backend.insert(crop_text.get(),quantity_text.get(),date_text.get(),outcome_text.get(),notes_text.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],crop_text.get(),quantity_text.get(),date_text.get(),outcome_text.get(),notes_text.get())
    view_command()

window=Tk()
window.wm_title("Planting Log")

l1=Label(window,text="Crop")
l1.grid(row=0, column=0)

crop_text=StringVar()
e1=Entry(window,textvariable=crop_text)
e1.grid(row=0, column=1)

l2=Label(window,text="Quantity")
l2.grid(row=0, column=2)

quantity_text=StringVar()
e2=Entry(window,textvariable=quantity_text)
e2.grid(row=0, column=3)

l3=Label(window,text="Date")
l3.grid(row=1, column=0)

date_text=StringVar()
e3=Entry(window,textvariable=date_text)
e3.grid(row=1, column=1)

l4=Label(window,text="Outcome")
l4.grid(row=1, column=2)

outcome_text=StringVar()
e4=Entry(window,textvariable=outcome_text)
e4.grid(row=1, column=3)

l5=Label(window,text="Notes")
l5.grid(row=2, column=0)

notes_text=StringVar()
e5=Entry(window,textvariable=notes_text)
e5.grid(row=2, column=1)

list1=Listbox(window, height=10,width=55)
list1.grid(row=3, column=0, rowspan=10,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All", width=12, command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Search", width=12, command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry", width=12, command=insert_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update Selected", width=12, command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete Selected", width=12, command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=8,column=3)

window.mainloop()
