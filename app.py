from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('WEBHOOK_URL')

app = Flask(__name__)

@app.route('/todoist-webhook', methods=['GET', 'POST'])
def handle_todoist_webhook():
    if request.method == 'GET':
        return "Webhook endpoint is live!", 200
    
    if not request.is_json:
        return "Unsupported Media Type: Please send JSON", 415

    data = request.get_json()

    event_name = data.get('event_name', '')
    event_data = data.get('event_data', {})
    task_content = event_data.get('content', 'No content')

    # Compose Discord message
    discord_data = {
        "content": f"📝 New Todoist Task ({event_name}): {task_content}"
    }

    # Send to Discord webhook URL
    response = requests.post(url, json=discord_data)
    if response.status_code != 204:
        print(f"Discord webhook error: {response.status_code} - {response.text}")

    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
