import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("API_KEY")

# Print it
print("Your API Key is:", api_key)
