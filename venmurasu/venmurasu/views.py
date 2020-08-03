from django.shortcuts import redirect, render
from django.http import HttpResponse
import pymongo

client = pymongo.MongoClient("mongodb+srv://keerthana:keerthana@cluster0.2jruk.mongodb.net/venmurasuDB?retryWrites=true&w=majority")
db = client["venmurasuDB"]
col = db["venmurasu-text"]

# Create your views here.
def largeWords(request, n):
    doc = col.fin().limit(n)