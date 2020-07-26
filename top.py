from itertools import count 
import os
import glob
import pandas as pd
import csv
  
def longest_word(lst, K): 
    cnt = count() 
    return sorted(lst, key = lambda w : (len(w), next(cnt)),  reverse = True)[:K]

# path = "/combined_csv.csv"
with open('./combined_csv.csv', newline='\n', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)
K = 10
print(longest_word(data, K)) 