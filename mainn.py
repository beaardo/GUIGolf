import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time
from database import *
from Logindeets import logout
from math import pi, cos, sin
deleted = False



def mainpage(): #Main page seen when logged in
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
    tk.Button(menu, text="Settings", font=("Calibri", 16, "bold"),width=15,height=2, command = lambda:settingz()).pack(pady=12.5)

    def clearcontents(): #clears right side with contents when called
        for widget in content.winfo_children():
            widget.destroy()


    def page_ovv(): #Overview button
        clearcontents()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS game (
            HoleNumber INTEGER PRIMARY KEY,
            PAR Integer NOT NULL,
            DISTANCE FLOAT NOT NULL,
            Shots Integer NOT NULL,
            Clubs_used TEXT NOT NULL,
            Putter_count INTEGER NOT NULL
        )

        """)
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM game")
        count = cursor.fetchone()[0]
        if count == 0:
            tk.Label(content, text="No stats found", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=40)
            tk.Label(content, text="Please Create New Game", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=80)

        else:
            statistics_page(content)

    def crea_button(): # Creates New Game
        clearcontents()
        tk.Button(content,text="Click to Create New Game",  font=("Calibri", 12, "bold"),width=40,height=1, command = lambda:game_cre()).pack(pady=5)
        global currenthole
        currenthole=1
    def game_cre():
        clearcontents()
        gamecreation()
        form = tk.Frame(content, bg="white")
        form.pack(pady=20)

        # Hole Number
        tk.Label(form, text="Hole:", font=("Calibri", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        hole_entry = tk.Entry(form, font=("Calibri", 14))
        hole_entry.grid(row=0, column=1)

        # Par
        tk.Label(form, text="Par:", font=("Calibri", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        par_entry = tk.Entry(form, font=("Calibri", 14))
        par_entry.grid(row=1, column=1)

        # Distance
        tk.Label(form, text="Distance (yards):", font=("Calibri", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        distance_entry = tk.Entry(form, font=("Calibri", 14))
        distance_entry.grid(row=2, column=1)

        # Shots
        tk.Label(form, text="Shots:", font=("Calibri", 14), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        shots_entry = tk.Entry(form, font=("Calibri", 14))
        shots_entry.grid(row=3, column=1)

        # Clubs Used
        tk.Label(form, text="Clubs Used:", font=("Calibri", 14), bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        clubs_entry = tk.Entry(form, font=("Calibri", 14))
        clubs_entry.grid(row=4, column=1)

        # Putts
        tk.Label(form, text="Number of Putts:", font=("Calibri", 14), bg="white").grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        putts_entry = tk.Entry(form, font=("Calibri", 14))
        putts_entry.grid(row=5, column=1)




        def savegame(): #game is saved in create game when called
            print("Par entry:", par_entry.get())
            print("Distance entry:", distance_entry.get())
            print("Shots entry:", shots_entry.get())
            print("Clubs entry:", clubs_entry.get())
            print("Putts entry:", putts_entry.get())

            HoleNumber = int(hole_entry.get())

            PAR = int(par_entry.get())

            DIST = float(distance_entry.get())

            Shot = int(shots_entry.get())

            Clubs_usd = clubs_entry.get().lower()


            Putter_coun = int(putts_entry.get())
            game_append(HoleNumber, PAR, DIST, Shot, Clubs_usd, Putter_coun)
            global currenthole
            currenthole+=1
            if currenthole <= 10:
                game_cre()
            else:
                clearcontents()
                stats()
                tk.Label(content, text="Game Complete!",font=("Calibri", 24, "bold"),bg="white").pack(pady=50)






        tk.Button(content, text="Save", font=("Calibri", 14, "bold"), bg="#8BC34A", fg="white", command = lambda:savegame()
        ).pack(pady=20)

    def prevview(): #previous games button
        clearcontents()
        cursor.execute("SELECT COUNT(*) FROM game")
        count = cursor.fetchone()[0]
        if count == 0: #if no games are found nothing can be displayed
            tk.Label(content, text="No stats found", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25, y=40)
            tk.Label(content, text="Please Create New Game", font=("Calibri", 20, "bold"), bg="#dfe6e9").place(x=25,y=80)

        else: #table displayed
            clearcontents()
            tk.Label(content,text="Previous Games",font=("Calibri", 24, "bold"),bg="#dfe6e9").pack(pady=20)

            table = ttk.Treeview(content,columns=("Hole","Par", "Distance", "Shots", "Clubs", "Putts"),show="headings",height=10)

            table.heading("Hole", text="Hole")
            table.heading("Par", text="Par")
            table.heading("Distance", text="Distance")
            table.heading("Shots", text="Shots")
            table.heading("Clubs", text="Clubs Used")
            table.heading("Putts", text="Putts")

            table.column("Hole", width=70, anchor = "center")
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

    def settingz(): #settings page with logout and clear last game's data
        clearcontents()

        tk.Label(
            content,
            text="Settings",
            font=("Calibri", 24, "bold"),
            bg="#dfe6e9"
        ).pack(pady=20)

        tk.Button(content,text="Log Out",font=("Calibri", 16, "bold"), bg="#f39c12", fg="white",width=20,command=logmeout).pack(pady=20)

        tk.Button(content, text="Delete Last Game Data",font=("Calibri", 16, "bold"), bg="#e74c3c", fg="white", width=20, command=delete_games).pack(pady=20)

    def logmeout(): #logout button
        answer = messagebox.askyesno("Logout","Are you sure you want to log out?")

        if answer:
            main_window.destroy()

        from Logindeets import loginpage
        loginpage()
    def delete_games(): #delete last game button
        answer = messagebox.askyesno("Delete Data", "Are you sure you want to delete the previous game? This cannot be undone." )
        deleted = True

        if answer:
            cursor.execute("DELETE FROM game")
            conn.commit()

            messagebox.showinfo("Success", "All previous game data has been deleted.")


def statistics_page(content): #pie chart function using clubs used
    cursor.execute("SELECT COUNT(*) FROM game")
    count = cursor.fetchone()[0]

    if count != 0:

        canvas = tk.Canvas(content,width=700,height=500,bg="#dfe6e9",highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # -------------------------
        # GET CLUBS FROM DATABASE
        # -------------------------

        cursor.execute("SELECT Clubs_used FROM game")
        club_rows = cursor.fetchall()

        # Dictionary to store how many times each club was used
        club_counts = {}

        for row in club_rows:

            clubs_string = row[0]

            if clubs_string:

                # Split the string wherever there is a comma
                clubs = clubs_string.split(",")

                for club in clubs:

                    # Remove spaces before/after the club name
                    club = club.strip()

                    if club:

                        if club in club_counts:
                            club_counts[club] += 1
                        else:
                            club_counts[club] = 1

        print("CLUB COUNTS:", club_counts)

        # -------------------------
        # CALCULATE TOTAL
        # -------------------------

        total = sum(club_counts.values())

        print("TOTAL:", total)

        # -------------------------
        # COLOURS
        # -------------------------

        colours = [
            "#3498DB",
            "#2980B9",
            "#1ABC9C",
            "#16A085",
            "#2ECC71",
            "#F39C12",
            "#E74C3C",
            "#9B59B6",
            "#E67E22",
            "#34495E",
            "#95A5A6"
        ]

        # -------------------------
        # TITLE
        # -------------------------

        canvas.create_text(350,35,text="Golf Club Usage",font=("Calibri", 24, "bold"),fill="black")

        # -------------------------
        # PIE CHART
        # -------------------------

        centre_x = 260
        centre_y = 270
        radius = 180

        start_angle = 0

        for i, (club, value) in enumerate(club_counts.items()):

            # Work out what percentage this club represents
            percentage = (value / total) * 100

            # Work out how much of the 360 degree circle it gets
            extent = (value / total) * 360

            canvas.create_arc(centre_x - radius,centre_y - radius,centre_x + radius,centre_y + radius,start=start_angle,extent=extent,fill=colours[i % len(colours)],outline="white",width=2)

            # -------------------------
            # PERCENTAGE TEXT
            # -------------------------

            middle_angle = start_angle + extent / 2

            text_radius = radius * 0.65

            x = centre_x + text_radius * cos(middle_angle * pi / 180)

            y = centre_y - text_radius * sin(middle_angle * pi / 180)

            canvas.create_text(x,y,text=f"{percentage:.1f}%",font=("Calibri", 11, "bold"),fill="white")

            start_angle += extent

        # -------------------------
        # LEGEND
        # -------------------------

        legend_x = 480
        legend_y = 130

        canvas.create_text(legend_x,90,text="Clubs Used",font=("Calibri", 16, "bold"),anchor="w",fill="black")

        for i, (club, value) in enumerate(club_counts.items()):

            percentage = (value / total) * 100

            canvas.create_rectangle(legend_x,legend_y,legend_x + 20,legend_y + 20,fill=colours[i % len(colours)],outline="")

            canvas.create_text(legend_x + 30,legend_y + 10,text=f"{club}: {percentage:.1f}%",anchor="w",font=("Calibri", 11),fill="black")

            legend_y += 40