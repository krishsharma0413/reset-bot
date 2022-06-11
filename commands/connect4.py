import disnake
from disnake.ext import commands


class ConnectFour(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="connect4",description="connect4 commands.")
    async def connect4_game(self, inter:disnake.ApplicationCommandInteraction):
        return await inter.send("todo")

    @connect4_game.sub_command(name="bet", description="bet on a game.")
    async def connect4_game_bet(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member, bet:str):
        return await inter.send("todo")
    
    @connect4_game.sub_command(name="casual", description="casual no bet game.")
    async def connect4_game_casual(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member):
        return await inter.send("todo")

def setup(client):
    client.add_cog(ConnectFour(client))