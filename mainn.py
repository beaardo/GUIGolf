import tkinter as tk
from tkinter import*
from tkinter import ttk
import time




def mainpage():
    main_window = tk.Tk()

    main_window.title("Main Page")
    main_window.geometry("1000x800")
    main_window.configure(bg="#dfe6e9")

    menu = tk.Frame(main_window, bg="#2c3e50", width=300, )
    menu.pack(side="left", fill="y", pady=200)



    content = tk.Frame(main_window, bg="white")
    content.pack(side="right", fill="both", expand=True)

    tk.Button(menu, text="Overview",  font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)
    tk.Button(menu, text="Add New Game",  font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)
    tk.Button(menu, text="Previous Games", font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)
    tk.Button(menu, text="Settings", font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)



