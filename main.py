import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv("tokens.env")


intents = disnake.Intents.default()

client = commands.Bot(
    command_prefix=commands.when_mentioned_or("resbot "),
    intents=intents,
    test_guilds=[885836332855881728, 651209882531266570, 915655393546481686],
    reload = True
)

database = motor.motor_asyncio.AsyncIOMotorClient(os.environ["database_link"])
database = database["economy"]
client.database = database

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


client.load_extensions("./commands")

client.run(os.environ["bot_token"])