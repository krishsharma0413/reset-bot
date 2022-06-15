import disnake
from disnake.ext import commands
from disnake.ui.select import S
from api import mazeAPI

class MazeButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="❌")
    async def quit_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()
        self.inter.embed.set_footer(text="game stopped")
        await msg.edit(embed=self.inter.embed, view=None)
        return

    @disnake.ui.button(emoji="⬆️")
    async def up_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        self.inter.game = mazeAPI.up(self.inter.game)
        msg  = await inter.original_message()
        if mazeAPI.is_winning(self.inter.game):
            self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
            self.inter.embed.color = disnake.Colour.green()
            self.inter.embed.set_footer(text="you won")
            await msg.edit(embed=self.inter.embed, view=None)
            return
        self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
        await msg.edit(embed=self.inter.embed)
        return


    @disnake.ui.button(emoji="⬛")
    async def level_show_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        return

    @disnake.ui.button(emoji="⬅️", row=1)
    async def left_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        self.inter.game = mazeAPI.left(self.inter.game)
        msg  = await inter.original_message()
        if mazeAPI.is_winning(self.inter.game):
            self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
            self.inter.embed.color = disnake.Colour.green()
            self.inter.embed.set_footer(text="you won")
            await msg.edit(embed=self.inter.embed, view=None)
            return
        self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
        await msg.edit(embed=self.inter.embed)
        return
    
    @disnake.ui.button(emoji="⬇️", row=1)
    async def down_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        self.inter.game = mazeAPI.down(self.inter.game)
        msg  = await inter.original_message()
        if mazeAPI.is_winning(self.inter.game):
            self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
            self.inter.embed.color = disnake.Colour.green()
            self.inter.embed.set_footer(text="you won")
            await msg.edit(embed=self.inter.embed, view=None)
            return
        self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
        await msg.edit(embed=self.inter.embed)
        return

    @disnake.ui.button(emoji="➡️", row=1)
    async def right_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        self.inter.game = mazeAPI.right(self.inter.game)
        msg  = await inter.original_message()
        if mazeAPI.is_winning(self.inter.game):
            self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
            self.inter.embed.color = disnake.Colour.green()
            self.inter.embed.set_footer(text="you won")
            await msg.edit(embed=self.inter.embed, view=None)
            return
        self.inter.embed.description = mazeAPI.rendermaze(self.inter.game["board"])
        await msg.edit(embed=self.inter.embed)
        return


class MazeSelectorButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(label="random")
    async def random_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("get your own level selector.",ephemeral=True)
        await inter.response.defer()
        game = mazeAPI.create()
        self.inter.embed.description = mazeAPI.rendermaze(game["board"])
        self.inter.game = game
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return


    @disnake.ui.button(label="play")
    async def play_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("get your own level selector.",ephemeral=True)
        await inter.response.defer()
        game = self.inter.game
        self.inter.embed.description = mazeAPI.rendermaze(game["board"])
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed,view=MazeButton(self.inter))
        return

class MazeCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="maze")
    async def maze_game(self,inter:disnake.ApplicationCommandInteraction):
        """
        play random mazes!
        """
        await inter.response.defer()
        game = mazeAPI.create()
        embed = disnake.Embed(title="random maze")
        inter.game = game
        inter.embed = embed
        embed.description = mazeAPI.rendermaze(game["board"])
        await inter.edit_original_message(embed=embed,view=MazeSelectorButton(inter))
        return

def setup(client):
    client.add_cog(MazeCommand(client))