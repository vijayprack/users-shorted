# assigement 1.main

import urllib.request
import json 
# from pprint import pprint   # pretty-print
import pandas as pd

url = "https://random-data-api.com/api/v2/users?size=20&is_xml=true"
response = urllib.request.urlopen(url)
text = response.read()
json_data = json.loads(text)

col = ["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"]
rows = []
  
for i in json_data:
    id = i["id"]
    firstName = i["first_name"]
    lastName = i["last_name"]
    username = i["username"]
    email = i["email"]
    avatar = i["avatar"]
    gender = i["gender"]
    dob = i["date_of_birth"]
    address = i["address"]

    rows.append({
        "id": id,
        "FirstName": firstName,
        "LastName": lastName,
        "Username": username,
        "Email": email,
        "Avatar": avatar,
        "Gender": gender,
        "DoB": dob,
        "Address": address,
    })
  
data_frame = pd.DataFrame(rows, columns=col)

# Writing dataframe to csv
data_frame.to_csv('users.csv')