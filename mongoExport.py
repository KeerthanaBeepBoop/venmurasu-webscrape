import csv
from tamil import utf8 
import re
import pymongo

from pymongo import MongoClient
client = MongoClient("mongodb+srv://keerthana:keerthana@cluster0.2jruk.mongodb.net/venmurasuDB?retryWrites=true&w=majority")

mydb = client["venmurasuDB"]
mycol = mydb["venmurasu-text"]

def fun(e):
    return len(utf8.get_letters(e))

with open("./combined_csv.csv", newline='\n', encoding="utf-8") as f:
    reader = csv.reader(f)
    print(reader)
    data = list(reader)
    data = [i[0] for i in data if(re.search("^[a-zA-Z0-9]*$",i[0])==None)]
    data = data[1:]
    data.sort(reverse=True,key=fun)

    for i in data:
        entry = {"text": i}
        x = mycol.insert_one(entry)

    print(data[0:1000])