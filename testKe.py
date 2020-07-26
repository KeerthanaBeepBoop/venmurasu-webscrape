from tamil import utf8
import string
import os,glob
import pandas as pd
import csv

folder_path = 'csv'
a=['']*100
flag=0
c=0;
                    
for root, dirs, files in os.walk(folder_path):
    for file in files:       
        with open(r"csv/"+file, "r", encoding="utf-8") as f:
            data=f.read()
            #data=data.split(",")
            for i in data:
                for j in range(100):
                    if len(utf8.get_letters(i)) > len(utf8.get_letters(a[j])):
                        print(utf8.get_letters(i))
                        a[j]=i                   
                        break