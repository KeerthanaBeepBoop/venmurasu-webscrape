from tamil import utf8
import csv
import os,glob
import string

folder_path = 'venmurasu-text/'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(r"venmurasu-text/"+file, "r", encoding="utf-8") as file_, open(r"csv/"+file+".csv", "w", encoding="utf-8") as csvfile:
            data = file_.read()
            writer = csv.writer(csvfile, delimiter=',')
            words = data.replace("‘","").replace("’","").replace('“',"").replace('”',"").replace("...",",").replace("…",",").split()
            table = data.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in words]
            writer.writerow(["Text"])
            for idx, line in enumerate(stripped, 1):
                writer.writerow([line.strip(' ')])

'''
2
folder_path = 'venmurasu-text/'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(r"venmurasu-text/"+file, "r", encoding="utf-8") as file_, open(r"csv/"+file+".csv", "w", encoding="utf-8") as csvfile:
            data = file_.read()
            writer = csv.writer(csvfile, delimiter=',')
            words = data.replace("‘","").replace("’","").replace('“',"").replace('”',"").split()
            table = data.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in words]
            writer.writerow(["Text"])
            for idx, line in enumerate(stripped, 1):
                writer.writerow([line.strip(' ')])
'''

'''
1
from tamil import utf8
import csv
import os,glob
import string

folder_path = 'venmurasu-text/'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(r"venmurasu-text/"+file, "r", encoding="utf-8") as file_, open(r"csv/"+file+".csv", "w", encoding="utf-8") as csvfile:
            data = file_.read()
            writer = csv.writer(csvfile, delimiter=',')
            words = data.replace("‘","").replace("’","").replace('“',"").replace('”',"").split()
            table = data.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in words]
            writer.writerow(('Number', 'Text'))
            for idx, line in enumerate(stripped, 1):
                writer.writerow([idx, line.strip(' ')])
'''