from flask import Flask, request
import requests

app = Flask(__name__)

D_WH_URL = "https://discord.com/api/webhooks/1402781367380475935/JbIOx-7jQXzv-EB4K3htPmPI1knO4nIbkoILSAgza6MQL7Y7rKP_W9iGL_wSKEn4nZJF"

@app.route("/"):
    