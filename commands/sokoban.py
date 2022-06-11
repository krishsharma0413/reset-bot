import disnake
from disnake.ext import commands

class Sokoban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="sokoban")
    async def sokoban_game(self,inter:disnake.ApplicationCommandInteraction):
        return
    
    @sokoban_game.sub_command(name="play")
    async def sokoban_game_play(self,inter:disnake.ApplicationCommandInteraction, level:str):
        """
        Play sokoban level.

        Parameters
        ----------
        level : Level to play.
        """
        return await inter.send("todo")

    @sokoban_game.sub_command(name="selector")
    async def sokoban_game_selector(self,inter:disnake.ApplicationCommandInteraction):
        """
        Level selector for sokoban.
        """
        return await inter.send("todo")

    @sokoban_game.sub_command(name="creator")
    async def sokoban_game_creator(self,inter:disnake.ApplicationCommandInteraction):
        """
        Level creator for sokoban.

        """
        return await inter.send("todo")

def setup(client):
    client.add_cog(Sokoban(client))