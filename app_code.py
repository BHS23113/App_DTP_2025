import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()


while True:
    choice = input("Press A to add a movie, U to update a movie D to delete a movie and L to shiow a list with all the mioves\n")
    choice_upper = choice.title()

    if choice_upper == "A":
        name = input("Please provide a name for the moive\n")
    
        data = [name]
        cursor.execute("INSERT INTO `movies` (`name`) VALUES (?)",data)
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
