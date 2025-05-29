import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

while True:
    choice = input("Press I to show a list with all the workouts, O to list a specific muscle group, P to list workout by category or E to end the program\n")
    choice_upper = choice.upper()

    if choice_upper == "P":
        category = input("Enter F for Push, G for Pull or H for Legs:\n")
        category_upper = category.upper()

        if category_upper == "F":
            result = cursor.execute("SELECT * FROM workout WHERE set_id = 1")

        elif category_upper == "G":
            result = cursor.execute("SELECT * FROM workout WHERE set_id = 2")

        elif category_upper == "H":
            result = cursor.execute("SELECT * FROM workout WHERE set_id = 3")

        else:
            print("Invalid category. Please enter F, G, or H.")
            continue

        workout = result.fetchall()

        for exercises in workout:
            print(str(exercises[0]) + '. - ' + exercises[1])
        print()

        start = input("Press R to return or E to end:\n").upper()
        if start == "E":
            break
        elif start == "R":
            continue
        else:
            print("Invalid input. Returning to main menu.")
            continue

    elif choice_upper == "I":
        result = cursor.execute("SELECT * FROM workout")
        workout = result.fetchall()

        for movie in workout:
            print(str(movie[0]) + '. - ' + movie[1])
        print()

    elif choice_upper == "O":
        muscle_group = input("Enter the muscle group to search:\n")
        result = cursor.execute
        workout = result.fetchall()

        for movie in workout:
            print(str(movie[0]) + '. - ' + movie[1])
        print()

    elif choice_upper == "E":
        break

    else:
        print("Invalid choice. Please press I, O, P, or E.")
        continue

connection.close()
