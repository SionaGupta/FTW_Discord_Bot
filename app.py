from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('WEBHOOK_URL')


app = Flask(__name__)
 
@app.route('/todoist-webhook', methods=['GET', 'POST'])
def handle_todoist_webhook():
    data = request.json
    task_content = data.get('event_name', '') + ": " + data.get('event_data', {}).get('content', 'No content')

    # Send to Discord
    discord_data = {
        "content": f"📝 New Todoist Task: {task_content}"
    }
    requests.post(url, json=discord_data)
    
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)