import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key
d_api_key = os.getenv("DISCORD_API_KEY")

# Establish the base URL 
base_url = "https://discord.com/api"

# Print it
print(d_api_key)
