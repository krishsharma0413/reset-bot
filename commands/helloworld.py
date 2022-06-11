import disnake
from disnake.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="hello",
        description="Say hello to the world",
    )
    async def hello(self, inter:disnake.ApplicationCommandInteraction):
        return await inter.send("Hello, world!")
        

def setup(client):
    client.add_cog(HelloWorld(client))