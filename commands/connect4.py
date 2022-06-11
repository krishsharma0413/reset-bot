import disnake
from disnake.ext import commands


class ConnectFour(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="connect4")
    async def connect4_game(self, inter:disnake.ApplicationCommandInteraction):
        return

    @connect4_game.sub_command(name="bet")
    async def connect4_game_bet(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member, bet:str):
        """
        Play connect4 with bets

        Parameters
        ----------
        user: User to bet on
        bet: betting amount
        """
        return await inter.send("todo")
    
    @connect4_game.sub_command(name="casual")
    async def connect4_game_casual(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member):
        """
        Play connect4 without bets

        Parameters
        ----------
        user: User to play connect4 with
        """
        return await inter.send("todo")

def setup(client):
    client.add_cog(ConnectFour(client))