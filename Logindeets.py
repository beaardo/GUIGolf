import tkinter as tk
from tkinter import messagebox
import time
maintest=False


def loginpage():
    intro_pg.withdraw()
    global login_window
    login_window = tk.Toplevel()
    login_window.title("Login Page")
    login_window.geometry("400x300")
    login_window.configure(bg="#dfe6e9")
    title = tk.Label(
        login_window,
        text="Login System",
        font=("Calibri", 22, "bold"),
        bg="#dfe6e9"
    )
    title.pack(pady=20)

    username_label = tk.Label(
        login_window,
        text="Email",
        font=("Calibri", 12),
        bg="#dfe6e9"
    )
    username_label.pack()

    global username_entry
    username_entry = tk.Entry(login_window, font=("Calibri", 12))
    username_entry.pack(pady=5)

    password_label = tk.Label(
        login_window,
        text="Password",
        font=("Calibri", 12),
        bg="#dfe6e9"
    )
    password_label.pack()

    global password_entry
    password_entry = tk.Entry(login_window, show="*", font=("Calibri", 12))
    password_entry.pack(pady=5)

    login_button = tk.Button(
        login_window,
        text="Login",
        font=("Calibri", 12, "bold"),
        bg="#0984e3",
        fg="white",
        width=15,
        command= lambda:loginpls()
    )
    login_button.pack(pady=20)


def loginpls():
    email = username_entry.get()
    password = password_entry.get()

    if email == "cbd@outlook.com" and password == "1234":
        open_front_page()

        from mainn import mainpage
        def switch_to_main():
            front_page.withdraw()
            mainpage()
        login_window.after(3000, switch_to_main)

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def open_front_page():
    login_window.withdraw()
    global front_page
    front_page = tk.Toplevel()
    front_page.title("Front Page")
    front_page.geometry("500x300")
    front_page.configure(bg="#ffffff")


    info_label = tk.Label(
        front_page,
        text="You have successfully logged in.",
        font=("Calibri", 14),
        bg="#f0f0f0"
    )
    info_label.pack(pady=10)


    logout_button = tk.Button(
        front_page,
        text="Cancel",
        font=("Calibri", 12),
        bg="red",
        fg="white",
        command=lambda: logout(front_page)

    )
    logout_button.pack(pady=30)




def logout(front_page):
    front_page.destroy()
    login_window.deiconify()

intro_pg=tk.Tk()
intro_pg.title("Intro Page")
intro_pg.geometry("500x300")
intro_pg.configure(bg="#f0f0f0")
title_label = tk.Label(
        intro_pg,
        text="Welcome to Outgolfed!",
        font=("Calibri", 20, "bold"),
        bg="#f0f0f0"
    )
title_label.pack(pady=15)
login=tk.Button(intro_pg,
    text="Log In",
    font=("Calibri", 14),
    bg="#0984e3",
    fg="white",
    command=lambda: loginpage()
                )
login.pack(pady=20)
login=tk.Button(intro_pg,
    text="Sign Up",
    font=("Calibri", 14),
    bg="#0984e3",
    fg="white",
    command=lambda: loginpage()
                )
login.pack(pady=20)




intro_pg.mainloop()
