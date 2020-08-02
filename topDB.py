import csv
from tamil import utf8 
import re

def fun(e):
    return len(utf8.get_letters(e))

with open("./combined_csv.csv", newline='\n', encoding="utf-8") as f:
    reader = csv.reader(f)
    print(reader)
    data = list(reader)
    data = [i[0] for i in data if(re.search("^[a-zA-Z0-9]*$",i[0])==None)]
    data = data[1:]
    data.sort(reverse=True,key=fun)
    print(data[0:1000])