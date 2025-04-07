from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

#Labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

km = Label(text="KMs")
km.grid(column=2, row=1)

calculated_kms = Label(text="0")
calculated_kms.grid(column=1, row=1)

#Buttons
def convert():
  num = float(input.get())
  calculated_kms.config(text=f"{round(num * 1.609)}")

#calls action() when pressed
converter = Button(text="Convert", command=convert)
converter.grid(column=1, row=2)
converter.config(padx=5, pady=5)

#Entries
input = Entry(width=10)
#Add some text to begin with
input.insert(END, string="0")
#Gets text in entry
input.grid(column=1, row=0)

window.mainloop()