"""This program is a sql and python database, it stores data for different exercises and allows the user to print them out in different catagories"""


import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

while True:
    choice = input("Press \033[36mI\033[0m to show a list with all the workouts, \033[36mO\033[0m to list a specific muscle group, \033[36mP\033[0m to list workout by category or \033[31mE\033[0m to end the program\n")
    choice_upper = choice.upper()

    if choice_upper == "P":
        
        while True:
            category = input("\n\nEnter \033[36mF\033[0m for Push, \033[36mG\033[0m for Pull or \033[36mH\033[0m for Legs:\n")
            category_upper = category.upper()
            if category_upper == "F":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 1")
                break

            elif category_upper == "G":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 2")
                break

            elif category_upper == "H":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 3")
                break

            else:
                print("\n\n\033[31mInvalid category.\033[0m Please enter \033[36mF\033[0m, \033[36mG\033[0m, or \033[36mH\033[0m.\n")

        workout = result.fetchall()

        for exercises in workout:
            print(str(exercises[0]) + '. - ' + exercises[1])
        print()

        start = input("\n\nPress \033[36mR\033[0m to return or \033[31mE\033[0m to end:\n").upper()
        if start == "E":
            break
        elif start == "R":
            continue
        else:
            print("\n\n\033[31mInvalid input returning to main menu.\033[0m\n")
            continue

    elif choice_upper == "I":
        result = cursor.execute("SELECT * FROM workout")
        workout = result.fetchall()

        for movie in workout:
            print(str(movie[0]) + '. - ' + movie[1])
        print()

    elif choice_upper == "O":
        muscle_group = input("\n\nEnter the muscle group to search:\n")
        result = cursor.execute
        workout = result.fetchall()

        for movie in workout:
            print(str(movie[0]) + '. - ' + movie[1])
        print()

    elif choice_upper == "E":
        break

    else:
        print("\n\n\033[31mInvalid choice.\033[0m Please enter \033[36mF\033[0m, \033[36mG\033[0m, \033[36mH\033[0m. or \033[31mE\033[0m.\n")
        continue

connection.close()
