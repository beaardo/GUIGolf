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
    tk.Button(menu, text="Add New Game",  font=("Calibri", 16, "bold"),width=15,height=2, command = lambda:crea_button()).pack(pady=12.5)
    tk.Button(menu, text="Previous Games", font=("Calibri", 16, "bold"),width=15,height=2, command = lambda:prevview()).pack(pady=12.5)
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

    def crea_button():
        clearcontents()
        tk.Button(content,text="Click to Create New Game",  font=("Calibri", 12, "bold"),width=40,height=1, command = lambda:game_cre()).pack(pady=5)
    def game_cre():
        clearcontents()
        gamecreation()
        form = tk.Frame(content, bg="white")
        form.pack(pady=20)
        global currenthole
        currenthole=1

        # Hole Number
        tk.Label(form, text="Hole:", font=("Calibri", 14), bg="white").grid(row=0, column=0, padx=10, pady=10,
                                                                            sticky="nsew")
        hole_entry = tk.Entry(form, font=("Calibri", 14))
        hole_entry.grid(row=0, column=1)

        # Par
        tk.Label(form, text="Par:", font=("Calibri", 14), bg="white").grid(row=1, column=0, padx=10, pady=10,
                                                                           sticky="nsew")
        par_entry = tk.Entry(form, font=("Calibri", 14))
        par_entry.grid(row=1, column=1)

        # Distance
        tk.Label(form, text="Distance (yards):", font=("Calibri", 14), bg="white").grid(row=2, column=0, padx=10,
                                                                                        pady=10, sticky="nsew")
        distance_entry = tk.Entry(form, font=("Calibri", 14))
        distance_entry.grid(row=2, column=1)

        # Shots
        tk.Label(form, text="Shots:", font=("Calibri", 14), bg="white").grid(row=3, column=0, padx=10, pady=10,
                                                                             sticky="nsew")
        shots_entry = tk.Entry(form, font=("Calibri", 14))
        shots_entry.grid(row=3, column=1)

        # Clubs Used
        tk.Label(form, text="Clubs Used:", font=("Calibri", 14), bg="white").grid(row=4, column=0, padx=10, pady=10,
                                                                                  sticky="nsew")
        clubs_entry = tk.Entry(form, font=("Calibri", 14))
        clubs_entry.grid(row=4, column=1)

        # Putts
        tk.Label(form, text="Number of Putts:", font=("Calibri", 14), bg="white").grid(row=5, column=0, padx=10,
                                                                                       pady=10, sticky="nsew")
        putts_entry = tk.Entry(form, font=("Calibri", 14))
        putts_entry.grid(row=5, column=1)




        def savegame():
            global PAR
            PAR = par_entry.get()
            global DIST
            DIST = distance_entry.get()
            global Shot
            Shot = shots_entry.get()
            global Clubs_usd
            Clubs_usd = clubs_entry.get()
            global Putter_coun
            Putter_coun = putts_entry.get()
            game_append()
            global currenthole
            currenthole+=1
            if currenthole <= 10:
                game_cre()
            else:
                clearcontents()
                tk.Label(
                    content,
                    text="Game Complete!",
                    font=("Calibri", 24, "bold"),
                    bg="white"
                ).pack(pady=50)
            content.after(2000, clearcontents)





        tk.Button(content, text="Save", font=("Calibri", 14, "bold"), bg="#8BC34A", fg="white", command = lambda:savegame()
        ).pack(pady=20)

    def prevview():
        clearcontents()
        cursor.execute("SELECT COUNT(*) FROM game")
        count = cursor.fetchone()[0]
        if count == 0:
            tk.Label(content, text="No stats found", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=40)
            tk.Label(content, text="Please Create New Game", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25,y=80)

        else:
            clearcontents()
            tk.Label(content,text="Previous Games",font=("Calibri", 24, "bold"),bg="white").pack(pady=20)

            table = ttk.Treeview(content,columns=("Hole","Par", "Distance", "Shots", "Clubs", "Putts"),show="headings",height=10)

            table.heading("Hole", text="Hole")
            table.heading("Par", text="Par")
            table.heading("Distance", text="Distance")
            table.heading("Shots", text="Shots")
            table.heading("Clubs", text="Clubs Used")
            table.heading("Putts", text="Putts")

            table.column("Row", width=70, anchor = "center")
            table.column("Par", width=70, anchor="center")
            table.column("Distance", width=100, anchor="center")
            table.column("Shots", width=70, anchor="center")
            table.column("Clubs", width=180, anchor="center")
            table.column("Putts", width=70, anchor="center")

            table.pack(pady=20)

            cursor.execute("""
            SELECT HoleNumber, PAR, DISTANCE, Shots, Clubs_used, Putter_count
            FROM game
            ORDER BY HoleNumber
            """)

            prevrows = cursor.fetchall()

            for row in prevrows:
                table.insert("","end",values=row)


        # Get all clubs used from the table
        # cursor.execute("SELECT Clubs_used FROM game")
        # clubs = cursor.fetchall()
        #
        # # Simplify list for changes
        # club_list = [club[0].lower() for club in clubs]
        #
        # # Remove putter since its always used
        # club_list = [club for club in club_list if club != "putter"]
        #
        # # Find most common club
        # if club_list:
        #     mostusedclub = Counter(club_list).most_common(1)[0][0]
        # else:
        #     mostusedclub = None
        #
        # print("Most used club (excluding putter):", mostusedclub)
        # # Take lowest 10 values
        # lowest_10 = sorted(gamelist)[:10]
        #
        # # Calculate handicap
        # handicap = sum(lowest_10) * 0.96
        #
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        # print(cursor.fetchall())
        #
        # print("Tables in DB:")
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        # for table in cursor.fetchall():
        #     print(table)
        #
        #
        #
        #


