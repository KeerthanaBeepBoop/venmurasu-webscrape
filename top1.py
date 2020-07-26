from itertools import count 
import os
import glob
import pandas as pd
import csv
from tamil import utf8 

# path = "/combined_csv.csv"
with open('./combined_csv.csv', newline='\n', encoding="utf-8") as f:
    reader = csv.reader(f)
    print(reader)
    data = list(reader)
    
    
a=[" "]*100
for i in data:
    for j in range(100):
        if i[0].isalpha():
            continue
        if len(utf8.get_letters(a[j][0])) < len(utf8.get_letters(i[0])):
            a[j]=i
            break
for j in a:
    print(j)