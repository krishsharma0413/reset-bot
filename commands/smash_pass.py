import disnake
from disnake.ext import commands
import aiohttp

async def fetch():
    async with aiohttp.ClientSession() as client:
        async with client.get("https://danbooru.donmai.us/posts/random.json") as resp: 
            json = await resp.json()
            return json

async def fetchimage(imageurl):
    async with aiohttp.ClientSession() as client:
        async with client.get(imageurl) as resp: 
            json = await resp.read()
            return json


class DanbooruButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(label="accept")
    async def button_accept(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id not in [684863269139513355, 424133185123647488]:
            return await inter.send("you dont have permission to accept/deny.",ephemeral=True)
        await inter.response.defer()
        
        channel = await inter.guild.fetch_channel(988874063726387320)
        imagebyte = await fetchimage(self.inter.json["file_url"])
        with open("./accept.png", "wb") as file:
            file.write(imagebyte)
        await channel.send(file=disnake.File("./accept.png"))
        
        embed = disnake.Embed(title="smash or pass")
        self.inter.json = await fetch()
        embed.set_image(url=self.inter.json["file_url"])
        msg = await inter.original_message()
        await msg.edit(embed=embed)
        return
        


    @disnake.ui.button(label="deny")
    async def button_deny(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id not in [684863269139513355, 424133185123647488]:
            return await inter.send("you dont have permission to accept/deny.",ephemeral=True)

        await inter.response.defer()
        msg = await inter.original_message()
        embed = disnake.Embed(title="smash or pass")
        self.inter.json = await fetch()
        embed.set_image(url=self.inter.json["file_url"])
        await msg.edit(embed=embed)
        return


class Danbo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="smash-pass")
    async def main_smash_pass(self, inter:disnake.ApplicationCommandInteraction):
        pass

    @main_smash_pass.sub_command(name="approve")
    async def approve_smash_pass(self, inter:disnake.ApplicationCommandInteraction):
        """
        approve images for smash/pass game.
        """
        await inter.response.defer()
        embed = disnake.Embed(title="smash or pass")
        json = await fetch()
        inter.json = json
        embed.set_image(url=json["file_url"])
        return await inter.edit_original_message(embed=embed, view=DanbooruButton(inter))

    @main_smash_pass.sub_command(name="smash")
    async def approve_smash_pass(self, inter:disnake.ApplicationCommandInteraction):
        """
        images to smash/pass.
        """
        return
    

    
    @main_smash_pass.sub_command(name="all")
    async def approve_smash_pass(self, inter:disnake.ApplicationCommandInteraction):
        """
        all the images you have smashed till now.
        """
        await inter.response.defer()
        db = await self.client.smashdb.find_one({"_id":inter.author.id})
        if db == None:
            return await inter.edit_original_message(content="start smashing to get some images here.")
        



        

def setup(client):
    client.add_cog(Danbo(client))