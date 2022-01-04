from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def getInput():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
     }
    
    if len(password_input) == 0 or len(website_input) == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave any fields empty!")
    else:

        try: 
            with open("Day-30\data.json","r") as data:
                # reading the old data
                data_seg = json.load(data)

        except FileNotFoundError:
            # Creating new file
            with open("Day-30\data.json","w") as data:
                json.dump(new_data,data, indent=4)

        else:
            # updating the old data with new Data 
            data_seg.update(new_data )
            with open("Day-30\data.json","w") as data:
                # writing the data
                json.dump(data_seg, data,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCHING ------------------------------ #
def find_password():
    website_input = website_entry.get()
    try:
        with open("Day-30/data.json","r") as data:
            search_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No such Data File Found.")
    else:
        if website_input in search_data:
            email = search_data[website_input]["email"]
            password = search_data[website_input]["password"]
            messagebox.showinfo(title=website_input, message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website_input} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="Day-30/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# 5 Row and 3 columns division 

# Labels
website = Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1,sticky='ew')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky='ew')
email_entry.insert(0,"rohityou000@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,sticky='ew')

# Buttons
gen_password = Button(text="Generate Password", command=gen_password) 
gen_password.config(padx=10,pady=0)
gen_password.grid(row=3,column=2)

add_button = Button(text="Add",width=36, command=getInput)
add_button.grid(row=4,column=1,columnspan=2,sticky='ew')

search_button = Button(text="Search", command=find_password)
search_button.config(padx=10,pady=0)
search_button.grid(row=1,column=2,sticky='ew')

window.mainloop()