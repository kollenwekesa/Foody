from random import *
import random
from tkinter import *
from tkinter import ttk 

win = Tk()
win.title("Food Choice")

win.geometry("400x300")


entrylabel1 = Label(win, text = "Starch options")
entrylabel2 = Label(win, text = "Protein options")
entrylabel3 = Label(win, text = "Vitamin options")

entrylabel1.grid(row = 0, column= 1)
entrylabel2.grid(row=1, column = 1)
entrylabel3.grid(row = 2, column = 1)

e1 = Entry(win, width = 50, bg = "white", fg = "blue")
e1.grid(row = 0, column = 2)
e2 = Entry(win, width = 50, bg = "white", fg = "blue")
e2.grid(row = 1, column = 2)
e3 = Entry(win, width = 50, bg = "white", fg = "blue")
e3.grid(row = 2, column = 2)
e = Entry(win, width = 50, bg = "white", fg = "yellow")
e.grid(row = 6, column = 1, columnspan = 2, pady = 10)

'''e1.insert()
e2.insert()
e3.insert()



starch_option = StringVar()
protein_option =StringVar()
vitamin_option =StringVar()

'''
result =StringVar()
outputlabel = StringVar()
def myClick():
	starch_option = e1.get()
	protein_option = e2.get()
	vitamin_option = e3.get() 

	starch_list = starch_option.split(",")
	protein_list = protein_option.split(",")
	vitamin_list = vitamin_option.split(",")

	starch_choice = random.choice(starch_list)
	protein_choice = random.choice(protein_list)
	vitamin_choice = random.choice(vitamin_list)

	e.insert(0, str(starch_choice) + "," + str(protein_choice)  + "," + str(vitamin_choice))

	result = starch_option + protein_option + vitamin_option
	# outputlabel =  Label(win, text = result)
	# outputlabel.grid(row= 6, column= 5)




Enterbutton = ttk.Button(win, text = "Press Enter", command=myClick)
Enterbutton.grid(row = 5, column = 1, columnspan = 2, pady = 20)




'''

def myClick():
	result= e1.get()
	outputlabel = Label(win, text = e1.get())
	outputlabel.grid(row=6, column = 6)


Enterbutton = Button(win, text = "Press Enter", bg = "white", fg = "blue", command=myClick)
Enterbutton.grid(row = 5, column = 5)

'''
win.mainloop()