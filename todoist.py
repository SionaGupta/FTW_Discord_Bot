from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('TODOIST_API_KEY')

api = TodoistAPI(api_key)

try:
    tasks = api.get_tasks()
    for task in tasks:
        print(task["content"])
except Exception as error:
    print("Error:", error)