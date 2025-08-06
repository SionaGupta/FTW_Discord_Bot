import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Not using intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

print(TOKEN)

def send_message():
    @client.event
    async def on_ready():
        try:
            print(f'Logged in as {client.user}')

            channel_id = 1402467664189984798
            channel = client.get_channel(channel_id)

            if channel:
                await channel.send("Hello from my bot!")
            else:
                print("Channel not found.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

        await client.close()

    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"🔥 Failed to connect: {e}")
