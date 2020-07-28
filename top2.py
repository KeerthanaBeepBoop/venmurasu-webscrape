import pandas as pd

from itertools import count 
import os
import glob
import pandas as pd
import csv
from tamil import utf8 
import re

url = "./combined_csv.csv"

def sum(data):
  for i in data:
    for j in range(10):
        if (re.search("^[a-zA-Z0-9]*$",i[0])!=None):
            continue
        if len(utf8.get_letters(a[j][0])) < len(utf8.get_letters(i[0])):
            a[j]=i
            break
  return(a)    

with open(url, newline='\n', encoding="utf-8") as f:
    reader = csv.reader(f)
    print(reader)
    data = list(reader)    

a=[" "]*10
print(sum(data));