from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
  password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
  password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
  passwordlist = password_letters + password_symbols + password_numbers 
  
  random.shuffle(passwordlist)
  password = "".join(passwordlist)
  e_password.insert(END, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website_input = e_website.get()
  email_user_input = e_email_user.get()
  password_input = e_password.get()
  new_data = {
    website_input: {
      "email": email_user_input,
      "password": password_input,
    }
  }
  if len(website_input) == 0 or len(email_user_input) == 0 or len(password_input) == 0:
    messagebox.showinfo(title="Missing Entires", message="You are missing some information, try again.")
  else:
    confirmed = messagebox.askokcancel(title=website_input, message=f"Are these correct?:\nEmail: {email_user_input}\nPassword: {password_input}\nConfirm?")
    if confirmed:
      try:
        with open("./Intermediate/password_manager/data.json", mode="r") as data_file:
          data = json.load(data_file)
      except FileNotFoundError:
        with open("./Intermediate/password_manager/data.json", mode="w") as data_file:
          json.dump(new_data, data_file, indent=2)
      else:
        data.update(new_data)
        with open("./Intermediate/password_manager/data.json", mode="w") as data_file:
          json.dump(data, data_file, indent=2)
      finally:
        e_website.delete(0, END)
        e_email_user.delete(0, END)
        e_password.delete(0, END)
        e_email_user.insert(END, "test@test.test")
        e_website.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
  website_search = e_website.get()
  if len(website_search) == 0:
    messagebox.showinfo(title="Missing Entires", message="You are missing a website, try again.")
  else:
    try:
      with open("./Intermediate/password_manager/data.json", mode="r") as data_file:
        data = json.load(data_file)
      try:
        messagebox.showinfo(title=f"{website_search}", message=f"Email: {data[website_search]['email']}\nPassword: {data[website_search]['password']}")
      except KeyError:
        messagebox.showinfo(title="No Website", message=f"You have nothing saved for '{website_search}' try again.")
    except FileNotFoundError:
      messagebox.showinfo(title="No File", message="No Data File.")
    except json.JSONDecodeError:
      messagebox.showerror(title="JSON Error", message="The data file is corrupted.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Main Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./Intermediate/password_manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
l_website = Label(text="Website:")
l_website.grid(column=0, row=1, sticky=E)

l_email_user = Label(text="Email/Username:")
l_email_user.grid(column=0, row=2, sticky=E)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3, sticky=E)

#Inputs
e_website = Entry(width=25)
e_website.grid(column=1, row=1, sticky=W)
e_website.focus()

e_email_user = Entry(width=35)
e_email_user.grid(column=1, row=2, columnspan=2, sticky=W)
e_email_user.insert(END, "test@test.test")

e_password = Entry(width=25)
e_password.grid(column=1, row=3, sticky=W)

#Buttons
b_generate = Button(text="Generate", command=generate_password, padx=6, pady=1)
b_generate.grid(column=2, row=3, sticky=E)

b_add = Button(text="Add to Storage", command=save, width=32, pady=1)
b_add.grid(column=1, row=4, columnspan=2, sticky=E)

b_search = Button(text="Search", command=search, padx=15, pady=1)
b_search.grid(column=2, row=1, sticky=E)

window.mainloop()