import disnake
from disnake.ext import commands
from api import sokobanAPI

class SOkobanButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="❌")
    async def quit_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)

        await inter.response.defer()
        msg  = await inter.original_message()
        self.inter.embed.set_footer(text=f"{self.inter.moves}, game stopped")
        await msg.edit(view=None)
        return

    @disnake.ui.button(emoji="⬆️")
    async def up_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game = sokobanAPI.up(self.inter.game)
        self.inter.embed.description = sokobanAPI.render_perm(self.inter.game)
        self.inter.moves += 1
        self.inter.embed.set_footer(text=f"number of moves: {self.inter.moves}")
        await inter.response.defer()
        msg  = await inter.original_message()
        if sokobanAPI.is_winning(self.inter.game):
            self.inter.embed.set_footer(text=f"{self.inter.moves}, you won!")
            self.inter.embed.color = disnake.Colour.green()
            await msg.edit(embed=self.inter.embed,view=None)
            return
        await msg.edit(embed=self.inter.embed)
        return


    @disnake.ui.button(emoji="⬛")
    async def level_show_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        # self.inter.game = sokobanAPI.up(self.inter.game)
        # self.inter.embed.description = sokobanAPI.render_perm(self.inter.game)
        # self.inter.moves += 1
        # self.inter.embed.set_footer(text=f"number of moves: {self.inter.moves}")
        # await inter.response.defer()
        # msg  = await inter.original_message()
        # if sokobanAPI.is_winning(self.inter.game):
        #     self.inter.embed.set_footer(text=f"{self.inter.moves}, you won!")
        #     self.inter.embed.color = disnake.Colour.green()
        #     await msg.edit(embed=self.inter.embed,view=None)
        #     return
        # await msg.edit(embed=self.inter.embed)
        return

    @disnake.ui.button(emoji="⬅️", row=1)
    async def left_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game = sokobanAPI.left(self.inter.game)
        self.inter.embed.description = sokobanAPI.render_perm(self.inter.game)
        self.inter.moves += 1
        self.inter.embed.set_footer(text=f"number of moves: {self.inter.moves}")
        await inter.response.defer()
        msg  = await inter.original_message()
        if sokobanAPI.is_winning(self.inter.game):
            self.inter.embed.set_footer(text=f"{self.inter.moves}, you won!")
            self.inter.embed.color = disnake.Colour.green()
            await msg.edit(embed=self.inter.embed,view=None)
            return
        await msg.edit(embed=self.inter.embed)
        return
    
    @disnake.ui.button(emoji="⬇️", row=1)
    async def down_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game = sokobanAPI.down(self.inter.game)
        self.inter.embed.description = sokobanAPI.render_perm(self.inter.game)
        self.inter.moves += 1
        self.inter.embed.set_footer(text=f"number of moves: {self.inter.moves}")
        await inter.response.defer()
        msg  = await inter.original_message()
        if sokobanAPI.is_winning(self.inter.game):
            self.inter.embed.set_footer(text=f"{self.inter.moves}, you won!")
            self.inter.embed.color = disnake.Colour.green()
            await msg.edit(embed=self.inter.embed,view=None)
            return
        await msg.edit(embed=self.inter.embed)
        return


    @disnake.ui.button(emoji="➡️", row=1)
    async def right_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        self.inter.game = sokobanAPI.right(self.inter.game)
        self.inter.embed.description = sokobanAPI.render_perm(self.inter.game)
        self.inter.moves += 1
        self.inter.embed.set_footer(text=f"number of moves: {self.inter.moves}")
        await inter.response.defer()
        msg  = await inter.original_message()
        if sokobanAPI.is_winning(self.inter.game):
            self.inter.embed.set_footer(text=f"{self.inter.moves}, you won!")
            self.inter.embed.color = disnake.Colour.green()
            await msg.edit(embed=self.inter.embed,view=None)
            return
        await msg.edit(embed=self.inter.embed)
        return

class SokobanCreatorButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="⬜")
    async def wall_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "⬜"
        self.inter.game += "1"
        self.inter.last = "wall"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)


    @disnake.ui.button(emoji="⬛")
    async def empty_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "⬛"
        self.inter.game += "0"
        self.inter.last = "empty"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)


    @disnake.ui.button(emoji="🟩")
    async def goal_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "🟩"
        self.inter.game += "4"
        self.inter.last = "goal"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)


    @disnake.ui.button(emoji="🟫")
    async def box_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "🟫"
        self.inter.game += "3"
        self.inter.last = "box"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)


    @disnake.ui.button(emoji="😔", row=1)
    async def player_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "😔"
        self.inter.game += "2"
        self.inter.last = "player"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)


    @disnake.ui.button(emoji="⬇️", row=1)
    async def down_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        self.inter.embed.description += "\n"
        self.inter.game += "/"
        self.inter.last = "down"
        self.inter.embed.set_footer(text=f"last operation: {self.inter.last}")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=self.inter.embed)

    @disnake.ui.button(emoji="❌", row=1)
    async def close_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=None)


    @disnake.ui.button(emoji="✅", row=1)
    async def complete_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you are not creator of this game.",ephemeral=True)
        await inter.response.defer()
        p = {
            "map": self.inter.game,
            "author": self.inter.author.display_name,
            "played":0
        }
        sokobanAPI.add(self.inter.name,p)
        msg  = await inter.original_message()
        self.inter.embed.set_footer(text="map complete.")
        await msg.edit(embed=self.inter.embed,view=None)


class SokobanSelectorButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="⬅️")
    async def left_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("get your own level selector.",ephemeral=True)
        level_list = self.inter.level_list
        levels = self.inter.levels
        self.inter.selected -=1
        embed = disnake.Embed(title=f"Sokoban levels selector: {level_list[self.inter.selected]}")
        game = sokobanAPI.create(level_list[self.inter.selected])
        game["map"] = sokobanAPI.raw_creator(game["map"])
        game = sokobanAPI.analyse(game)
        embed.description = sokobanAPI.render_perm(game)
        embed.set_footer(text=f"made by: {game['author']} | {game['played']} plays")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=embed)


    @disnake.ui.button(emoji="➡️")
    async def right_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("get your own level selector.",ephemeral=True)
        level_list = self.inter.level_list
        levels = self.inter.levels
        self.inter.selected += 1
        embed = disnake.Embed(title=f"Sokoban levels selector: {level_list[self.inter.selected]}")
        game = sokobanAPI.create(level_list[self.inter.selected])
        game["map"] = sokobanAPI.raw_creator(game["map"])
        game = sokobanAPI.analyse(game)
        embed.description = sokobanAPI.render_perm(game)
        embed.set_footer(text=f"made by: {game['author']} | {game['played']} plays")
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(embed=embed)


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
        await inter.response.defer()
        game = sokobanAPI.create(level)
        sokobanAPI.update_playcount(level)
        game["map"] = sokobanAPI.raw_creator(game["map"])
        game = sokobanAPI.analyse(game)
        embed = disnake.Embed(title="Sokoban level: " + level, description=sokobanAPI.render_perm(game))
        embed.description = sokobanAPI.render_perm(game)
        embed.set_footer(text="number of moves: 0")
        inter.moves = 0
        inter.embed = embed
        inter.game = game
        await inter.edit_original_message(embed=embed, view=SOkobanButton(inter))

    @sokoban_game.sub_command(name="selector")
    async def sokoban_game_selector(self,inter:disnake.ApplicationCommandInteraction):
        """
        Level selector for sokoban.
        """
        await inter.response.defer()
        levels = sokobanAPI.all()
        level_list = list(levels.keys())
        selected = 0
        inter.levels = levels
        inter.level_list = level_list
        inter.selected = selected
        embed = disnake.Embed(title=f"Sokoban levels selector: {level_list[selected]}")
        game = sokobanAPI.create(level_list[selected])
        game["map"] = sokobanAPI.raw_creator(game["map"])
        game = sokobanAPI.analyse(game)
        embed.description = sokobanAPI.render_perm(game)
        embed.set_footer(text=f"made by: {game['author']} | {game['played']} plays")
        await inter.edit_original_message(embed=embed, view=SokobanSelectorButton(inter))

    @sokoban_game.sub_command(name="info")
    async def sokoban_game_selector(self,inter:disnake.ApplicationCommandInteraction, level:str):
        """
        Level selector for sokoban.
        """
        await inter.response.defer()
        game = sokobanAPI.create(level)
        game["map"] = sokobanAPI.raw_creator(game["map"])
        game = sokobanAPI.analyse(game)
        embed = disnake.Embed(title="Sokoban level: " + level, description=sokobanAPI.render_perm(game))
        embed.set_footer(text=f"made by: {game['author']} | {game['played']} plays")
        await inter.edit_original_message(embed=embed)

    @sokoban_game.sub_command(name="creator")
    async def sokoban_game_creator(self,inter:disnake.ApplicationCommandInteraction, name:str):
        """
        Level creator for sokoban.

        """
        await inter.response.defer()
        if len(name) < 3:
            await inter.edit_original_message(content="name too short.")
            return

        if not sokobanAPI.name_checker(name):
            await inter.edit_original_message(content="name is not valid.")
            return
        embed = disnake.Embed(title="Sokoban level creator",description="")
        inter.game = ""
        inter.embed = embed
        inter.name = name
        inter.last = "none"
        await inter.edit_original_message(embed=embed, view=SokobanCreatorButton(inter))

def setup(client):
    client.add_cog(Sokoban(client))