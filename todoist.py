from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('API_KEY')

api = TodoistAPI(API_KEY)

try:
    tasks = api.get_tasks()
    for task in tasks:
        print(task.content)
except Exception as error:
    print("Error:", error)