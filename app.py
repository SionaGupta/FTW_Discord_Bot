from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('WEBHOOK_URL')


app = Flask(__name__)

url = 
@app.route("/"):
    