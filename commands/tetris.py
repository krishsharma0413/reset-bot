import disnake
from disnake.ext import commands


class Tetris(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="tetris")
    async def tetris_game(self, inter:disnake.ApplicationCommandInteraction):
        """
        Play tetris game.
        """
        return await inter.send("todo")
        

def setup(client):
    client.add_cog(Tetris(client))