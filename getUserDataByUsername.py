# Assigenment 1.B
# Searching by id or username

import csv

with open("users_sorted.csv", "r") as file:
    reader = csv.reader(file)
    
    search = str(input("Give Id or Username: "))
    for row in reader:
        if search in row:
            print(f"""
            Id: {row[1]},
            FirstName: {row[2]},
            LastName: {row[3]},
            Username: {row[4]},
            Email: {row[5]},
            Avatar: {row[6]},
            Gender: {row[7]},
            DoB: {row[8]},
            Address: {row[9]},
            """)