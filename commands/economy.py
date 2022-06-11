import disnake
from disnake.ext import commands


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="economy",description="economy commands.")
    async def economy(self, inter:disnake.ApplicationCommandInteraction):
        return await inter.send("todo")

    @economy.sub_command(name="cash", description="shows your wallet")
    async def economy_cash(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member=None):
        return await inter.send("todo")
    
    @economy.sub_command(name="inventory", description="inventory if you have any")
    async def economy_inventory(self, inter:disnake.ApplicationCommandInteraction):
        return await inter.send("todo")
        
def setup(client):
    client.add_cog(Economy(client))