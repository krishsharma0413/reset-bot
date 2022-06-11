import disnake
from disnake.ext import commands


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="economy")
    async def economy(self, inter:disnake.ApplicationCommandInteraction):
        return

    @economy.sub_command(name="cash")
    async def economy_cash(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member=None):
        """
        Shows balance of the user.

        Parameters
        ----------
        user : User to find the balanace of.
        """
        return await inter.send("todo")
    
    @economy.sub_command(name="inventory")
    async def economy_inventory(self, inter:disnake.ApplicationCommandInteraction):
        """
        Shows inventory of the user.
        """
        return await inter.send("todo")
        
def setup(client):
    client.add_cog(Economy(client))