from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://Jeevanshi:3hgjkr$9@cluster0.comyh.mongodb.net/Lesson2?retryWrites=true&w=majority"

client = pymongo.MongoClient("mongodb+srv://Jeevanshi:3hgjkr$9@cluster0.comyh.mongodb.net/Lesson2?retryWrites=true&w=majority")
db = client.test