import disnake
from disnake.ext import commands
from api import tetrisAPI

class TetrisButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="🔀")
    async def button_hold(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.swap()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return

        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return



    @disnake.ui.button(emoji="⏬")
    async def button_hard_drop(self, button: disnake.ui.Button, inter:disnake.Interaction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.hard_drop()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return


    @disnake.ui.button(emoji="🔄")
    async def button_rotate(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.rotate()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return

        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return
    
    @disnake.ui.button(emoji="⬅️", row=1)
    async def button_left(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.left()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return

        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return

    @disnake.ui.button(emoji="⬇️", row=1)
    async def button_down(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.soft_drop()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return

        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return
    
    @disnake.ui.button(emoji="➡️", row=1)
    async def button_right(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game.right()
        self.inter.game.tick()
        if self.inter.game.playing == False:
            await inter.response.defer()
            msg  = await inter.original_message()
            self.inter.embed.title = "you lost"
            await msg.edit(embed=self.inter.embed,view=None)
            return

        self.inter.embed.description = tetrisAPI.render(self.inter.game)
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(self.inter.game))
        self.inter.embed.color = color
        self.inter.embed.set_thumbnail(url=url)
        self.inter.embed.set_footer(text="score " + str(self.inter.game.score))
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)
        return

class Tetris(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="tetris")
    async def tetris_game(self, inter:disnake.ApplicationCommandInteraction):
        """
        Play tetris game.
        """
        await inter.response.defer()
        game = tetrisAPI.create_game()
        color, url = tetrisAPI.color_detector(tetrisAPI.next_piece(game))
        embed = disnake.Embed(title="Tetris",color=color)
        embed.set_thumbnail(url=url)
        embed.description = tetrisAPI.render(game)
        embed.set_footer(text="score " + str(game.score))
        inter.game = game
        inter.embed = embed
        return await inter.edit_original_message(embed=embed, view=TetrisButton(inter))
        
        

def setup(client):
    client.add_cog(Tetris(client))