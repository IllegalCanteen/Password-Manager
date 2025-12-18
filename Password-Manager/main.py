from tkinter import *
from tkinter import messagebox
import random
import pyperclip
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")

#------------------------------------------------------------------------------------------------------------
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_characters = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    new_password = password_characters + password_numbers + password_letters
    random.shuffle(new_password)
    password = "".join(new_password)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

#------------------------------------------------------------------------------------------------------------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email)==0:
        messagebox.showerror(title="Oops",message="Please do not leave any field empty!")

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details you entered \nEmail: {email}\nWebsite: {website}\nPassword: {password}\nIs this ok to save?")
        if is_ok:

            with open("password_data.txt","a") as password_file:
                password_file.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



canvas.create_image(100,100 ,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky="EW")
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
email_entry.insert(0,"kaustubh.sunderraman@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,sticky="EW")

generate_password_button=Button(text="Generate Password",command=generate)
generate_password_button.grid(row=3,column=2)
add_button=Radiobutton(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")
window.mainloop()