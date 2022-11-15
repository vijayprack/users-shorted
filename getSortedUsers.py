# assigenment 1.A
# sorted by first name


# # first method - using pandas
# import pandas as pd

# data_frame = pd.read_csv('users.csv')
# shorted_data_frame = data_frame.sort_values(by=['FirstName'])
# shorted_data_frame.to_csv('users_sorted.csv', index=False)


# second method - using sorting method
import csv ,operator
  
data = csv.reader(open('users.csv'),delimiter=',')
data = sorted(data, key=operator.itemgetter(2))    # 2 = number of column
data.remove(['', 'id', 'FirstName', 'LastName', 'Username', 'Email', 'Avatar', 'Gender', 'DoB', 'Address'])
data.insert(0, ['', 'id', 'FirstName', 'LastName', 'Username', 'Email', 'Avatar', 'Gender', 'DoB', 'Address'])

with open("users_sorted.csv", "w") as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)
