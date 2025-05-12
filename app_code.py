import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()


while True:
    choice = input("Press A to add a workout, U to update a workout D to delete a workout and L to shiow a list with all the workouts\n")
    choice_upper = choice.title()

    if choice_upper == "A":
        name = input("Please provide a name for the workout\n")
        duration = input("Please endter the duration of your workout in minutes\n")
    
        data = [name, duration]
        cursor.execute("INSERT INTO `movies` (name, duration) VALUES (?, ?)",data)
        connection.commit()
    
    elif choice_upper == "U":
        id = input("Please provide the ID for the movie you want to update\n")
        name = input("Please provide a name for the moive ")

        data = [name, id]
        cursor.execute("UPDATE movies SET name=? WHERE id=?",data)
        connection.commit()

    elif choice_upper == "D":
        id = input("Please provide the ID for the movie you want to delete\n")
        
        data = [id]
        cursor.execute("DELETE FROM movies WHERE id=?",data)
        connection.commit()

    elif choice_upper == "L":
        result = cursor.execute("SELECT * FROM movies")

        movies = result.fetchall()

        for movie in movies:
            print(str(movie[0])+'. - '+movie[1])
    
    else:
        print("Please press A, U, D or L")
        while True:
            end = input("Please press E to end the program or R to continue ")
            end_cap = end.title()
            if end_cap == "E":
                break
            elif end_cap == "R":
                continue
            else:
                print("Please press E or R")
        if end_cap == "E":
            break
