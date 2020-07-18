from tamil import utf8
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import string
import os, glob

#Opening a file 
# with open('newfile.txt', 'r') as f:
#     data = f.read()
#     print(data)

# soup = BeautifulSoup(response.text, "html.parser")
folderPath = 'venmurasu/'

for root, dirs, files in os.walk('venmurasu/'):
    for file in files:
        # print(file)
        soup = BeautifulSoup(open(folderPath+file,encoding="utf-8"), "html.parser")
        one_a_tag = soup.findAll('p', style="text-align:justify;")
        plainText = ""
        for i in one_a_tag:
            plainText=plainText+i.text
            plainText=plainText+'\n'+'\t'
        # print(plainText)
        with open('venmurasu-text/'+file, "w", encoding="utf-8") as f:
            f.write(plainText)


# The following used to get list of files using global 
# list_of_files = glob.glob('venmurasu/*') #1933 files
# for file_name in list_of_files:
#     print(file_name)

# This prints the list of files 
# entries = os.listdir('venmurasu/')
# for entry in entries:
#     print(entry)