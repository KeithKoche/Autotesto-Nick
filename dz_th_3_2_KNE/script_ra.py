import csv
from csv import DictReader
import json


with open("../dz_th_3_2_KNE/books.csv", newline='') as file_b:
    reader = DictReader(file_b)
    books = []

    for row in reader:
        row_d = {}
        row_d["Title"] = row["Title"]
        row_d["Author"] = row["Author"]
        row_d["Height"] = row["Height"]
        books.append(dict(row_d))


with open("../dz_th_3_2_KNE/users.json", "r") as file_u:
    users = json.loads(file_u.read())
    users_list = users
    final = []

if len(books) < len(users_list) == True:
    for user in users_list:
        sold_book = {}
        sold_book["name"] = user["name"]
        sold_book["gender"] = user["gender"]
        sold_book["address"] = user["address"]
        sold_book["books"] = [books.pop(0)] if len(books) > 0 else []
        final.append(sold_book)

else:
    for user in users_list:
        sold_book = {}
        sold_book["name"] = user["name"]
        sold_book["gender"] = user["gender"]
        sold_book["address"] = user["address"]
        sold_book["books"] = [books.pop(0)]
        final.append(sold_book)



with open("../dz_th_3_2_KNE/final.json", "w") as file_e:
        s = json.dumps(final, indent=4)
        file_e.write(s)