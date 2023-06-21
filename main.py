import tkinter
from tkinter import messagebox
import random

def generate_pw():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', '=', '_', '-', '/', '?', '\\', '.', ',', '<', '>', '"', '\'']
    pw_list = [random.choice(characters) for _ in range(25)]
    random.shuffle(pw_list)
    pw_str = ''.join(pw_list)
    password_output.delete(0, tkinter.END)
    password_output.insert(0, pw_str)

def save_info():
    if not website_input.get() or not username_input.get() or not password_output.get():
        messagebox.showerror(message = 'Please complete all fields.')
    else:
        line = f"\nWebsite: {website_input.get()}\nUsername: {username_input.get()}\nPassword: {password_output.get()}\n"
        if messagebox.askokcancel(message = f"You are about to save: \n{line}") == True:
            handler = open('usernames_and_passwords.txt', 'a')
            handler.write(line)
            handler.close()
            website_input.delete(0, tkinter.END)
            username_input.delete(0, tkinter.END)
            password_output.delete(0, tkinter.END)
            messagebox.showinfo('Info saved to usernames_and_passwords.txt')

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx = 35, pady = 35)

lock_canvas = tkinter.Canvas(height = 200, width = 200)
lock_logo = tkinter.PhotoImage(file = 'logo.png')
lock_canvas.create_image(100, 100, image = lock_logo)
lock_canvas.grid(row = 1, column = 2)

website_label = tkinter.Label(text = 'Website:')
website_label.grid(row = 2, column = 1)
website_input = tkinter.Entry(width = 38)
website_input.grid(row = 2, column = 2, columnspan = 2)
website_input.focus()

username_label = tkinter.Label(text = 'Username:')
username_label.grid(row = 3, column = 1)
username_input = tkinter.Entry(width = 38)
username_input.grid(row = 3, column = 2, columnspan = 2)

password_label = tkinter.Label(text = 'Password:')
password_label.grid(row = 4, column = 1)
password_output = tkinter.Entry(width = 27)
password_output.grid(row = 4, column = 2)
password_generator_button = tkinter.Button(text = 'Generate', command = generate_pw)
password_generator_button.grid(row = 4, column = 3)

save_button = tkinter.Button(text = 'Save', command = save_info, width = 36)
save_button.grid(row = 5, column = 2, columnspan= 2)

window.mainloop()