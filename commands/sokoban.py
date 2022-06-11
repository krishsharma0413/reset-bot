import disnake
from disnake.ext import commands

class Sokoban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="sokoban",description="sokoban commands.")
    async def sokoban_game(self,inter:disnake.ApplicationCommandInteraction):
        return 
    
    @sokoban_game.sub_command(name="play",description="play sokoban level.")
    async def sokoban_game_play(self,inter:disnake.ApplicationCommandInteraction, level:str):
        return await inter.send("todo")

    @sokoban_game.sub_command(name="selector",description="sokoban level selector.")
    async def sokoban_game_selector(self,inter:disnake.ApplicationCommandInteraction):
        return await inter.send("todo")

    @sokoban_game.sub_command(name="creator",description="create sokoban levels.")
    async def sokoban_game_creator(self,inter:disnake.ApplicationCommandInteraction):
        return await inter.send("todo")

def setup(client):
    client.add_cog(Sokoban(client))