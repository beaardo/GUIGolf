import tkinter as tk
from tkinter import*
from tkinter import ttk
import time
from database import *



def mainpage():
    main_window = tk.Tk()

    main_window.title("Main Page")
    main_window.geometry("1000x800")
    main_window.configure(bg="white")

    menu = tk.Frame(main_window, bg="#8bc34a", width=300, )
    menu.pack(side="left", fill="y", pady=200)



    content = tk.Frame(main_window, bg="#dfe6e9")
    content.pack(side="right", fill="both", expand=True)

    tk.Label(content, text="Welcome to Outgolfed!", font=("Calibri", 30, "bold"), bg="#dfe6e9").place(relx=0.5, rely=0.3, anchor="center")
    tk.Label(content, text=first_n+" "+last_n, font=("Calibri", 30, "bold"), bg="#dfe6e9").place(relx=0.5, rely=0.4, anchor="center")


    tk.Label(main_window,text="Menu",font=("Calibri", 20, "bold"),bg="white").place(x=25, y=40)

    tk.Button(menu, text="Overview",  font=("Calibri", 16, "bold"),width=15,height=2, command = lambda:page_ovv()).pack(pady=12.5)
    tk.Button(menu, text="Add New Game",  font=("Calibri", 16, "bold"),width=15,height=2, command = lambda:game_cre()).pack(pady=12.5)
    tk.Button(menu, text="Previous Games", font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)
    tk.Button(menu, text="Settings", font=("Calibri", 16, "bold"),width=15,height=2).pack(pady=12.5)

    def clearcontents():
        for widget in content.winfo_children():
            widget.destroy()


    def page_ovv():
        clearcontents()
        cursor.execute("SELECT COUNT(*) FROM game")
        count = cursor.fetchone()[0]
        if count == 0:
            tk.Label(content, text="No stats found", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=40)
            tk.Label(content, text="Please Create New Game", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=80)

    def game_cre():
        clearcontents()
        for i in range(1, 11):
            PAR = int(input("Enter Par number: "))
            DIST = int(input("Enter distance from tee: "))
            Shot = int(input("Enter number of shots taken: "))
            Clubs_usd = input("Enter which Clubs used: ")
            Putter_coun = int(input("Enter how many times was putter used? "))
            cursor.execute("""
            INSERT INTO game (PAR, DISTANCE, Shots, Clubs_used, Putter_count)
            VALUES (?, ?, ?, ?, ?)
            """, (PAR, DIST, Shot, Clubs_usd, Putter_coun))
            print("Row inserted successfully.")
            totalscore = totalscore + Shot
            differential = ((Shot - course_rating) * 113) / slope_rating
            gamelist.append(differential)
            conn.commit()

        # Get all clubs used from the table
        cursor.execute("SELECT Clubs_used FROM game")
        clubs = cursor.fetchall()

        # Simplify list for changes
        club_list = [club[0].lower() for club in clubs]

        # Remove putter since its always used
        club_list = [club for club in club_list if club != "putter"]

        # Find most common club
        if club_list:
            mostusedclub = Counter(club_list).most_common(1)[0][0]
        else:
            mostusedclub = None

        print("Most used club (excluding putter):", mostusedclub)
        # Take lowest 10 values
        lowest_10 = sorted(gamelist)[:10]

        # Calculate handicap
        handicap = sum(lowest_10) * 0.96

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print(cursor.fetchall())

        print("Tables in DB:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for table in cursor.fetchall():
            print(table)






