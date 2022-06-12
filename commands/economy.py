import disnake
from disnake.ext import commands

def embed_render(author,cash):
    embed = disnake.Embed(title="resbot economy", description=f"money: {cash}", color=disnake.Colour.blue())
    embed.set_author(name=author.name, icon_url=author.avatar.url)
    return embed

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
        await inter.response.defer()
        user = user or inter.author
        balance = await self.client.database.main.find_one({"_id": user.id})
        if balance is None:
            await self.client.database.main.insert_one({"_id": user.id, "money": 10000})
            embed = embed_render(user, 10000)
        else:
            embed = embed_render(user, balance["money"])
        await inter.edit_original_message(embed=embed)


    # @economy.sub_command(name="inventory")
    # async def economy_inventory(self, inter:disnake.ApplicationCommandInteraction):
    #     """
    #     Shows inventory of the user.
    #     """
    #     return await inter.send("todo")
        
def setup(client):
    client.add_cog(Economy(client))