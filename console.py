from box import Case, Carton
from tkinter import *
#GIT HUB WELCOMED

root = Tk()

label = Label()
label.pack()

milo = Case()

entry = Entry()
entry.pack()

def setValue():
	label["text"] = milo.calculateBoxCompression(int(Entry.get(entry)),300,400)

button = Button(text = "calculate",command = setValue)
button.pack()


root.mainloop()
