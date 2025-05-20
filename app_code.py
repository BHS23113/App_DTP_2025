import sqlite3

def isint(num):
  try:
    int(num)
    return True
  except:
    return False


connection = sqlite3.connect("movies.db")
cursor = connection.cursor()


while True:
    choice = input("Press A to add a workout, U to update a workout D to delete a workout and L to shiow a list with all the workouts\n")
    choice_upper = choice.title()

    if choice_upper == "A":
        date = input("Please provide the date D/M/Y\n")
        workout_type = input("please enter the name of the work out")
        sets = input("Please enter the number of sets")
        reps = input("Please enter the number of reps")
        weight = input("Please enter the weight")
        while True:
            duration = input("Please endter the duration of your workout in minutes\n")
            if isint(duration) == False:
                print('Please enter a number')
                continue
            else:
                break
    
        data = [date, duration]
        cursor.execute("INSERT INTO `workout` (date, duration) VALUES (?, ?)",data)
        connection.commit()
    
    elif choice_upper == "U":
        id = input("Please provide the ID for the movie you want to update\n")
        name = input("Please provide a name for the moive\n")

        data = [date, id]
        cursor.execute("UPDATE workout SET name=? WHERE id=?",data)
        connection.commit()

    elif choice_upper == "D":
        id = input("Please provide the ID for the movie you want to delete\n")
        
        data = [id]
        cursor.execute("DELETE FROM workout WHERE id=?",data)
        connection.commit()

    elif choice_upper == "L":
        result = cursor.execute("SELECT * FROM workout")

        workout = result.fetchall()

        for movie in workout:
            print(str(movie[0])+'. - '+movie[1])
    
    else:
        print("Please press A, U, D or L")
        while True:
            end = input("Please press E to end the program or R to continue\n")
            end_cap = end.title()
            if end_cap == "E":
                break
            elif end_cap == "R":
                continue
            else:
                print("Please press E or R")
        if end_cap == "E":
            break
