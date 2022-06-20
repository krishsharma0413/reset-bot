from pickletools import pybool
import disnake
from disnake.ext import commands
from pyboy import PyBoy, WindowEvent
from threading import Thread
from asyncio import sleep as slep
from time import sleep
import io

def ticker(game):
    for _ in range(100):
        game.tick()


def save_state(boy):
	file_like_object = io.BytesIO()
	file_like_object.seek(0)
	boy.save_state(file_like_object)
	return file_like_object



class PokeMonButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(label="start")
    async def start_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_BUTTON_START)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_BUTTON_START)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return

    @disnake.ui.button(label="select")
    async def select_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="a")
    async def a_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_BUTTON_A)
        self.inter.game.tick()
        self.inter.game.tick()
        print("aaa  ")
        self.inter.game.send_input(WindowEvent.RELEASE_BUTTON_A)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="b")
    async def b_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_BUTTON_B)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_BUTTON_B)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="up")
    async def up_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_ARROW_UP)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_ARROW_UP)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="down")
    async def down_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_ARROW_DOWN)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="left")
    async def left_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_ARROW_LEFT)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


    @disnake.ui.button(label="right")
    async def right_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        self.inter.game.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        self.inter.game.tick()
        self.inter.game.tick()
        self.inter.game.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        ticker(self.inter.game)
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return

    @disnake.ui.button(label="save game")
    async def speed_up_button(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.author.id:
            return await inter.send("you cant play this game.",ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        ticker(self.inter.game)
        self.inter.game.save_state(open(f"./saves/{self.inter.author.id}.state", "wb"))
        self.inter.game.screen_image().resize((256,256)).save("game.png")
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        embed.set_image(file=disnake.File("./game.png"))
        await msg.edit(embed=embed)
        return


class PokePoke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="pokemon-red")
    async def hello(self, inter:disnake.ApplicationCommandInteraction):
        """
        play pokemon red on discord!!!!
        """
        await inter.response.defer()
        quiet = True
        game = PyBoy("./pokemonred.gb", window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
        game.set_emulation_speed(0)
        embed = disnake.Embed(title="Pokemon Red", color=disnake.Colour.red())
        game.screen_image().resize((256,256)).resize((256,256)).save("game.png")
        embed.set_image(file=disnake.File("./game.png"))
        inter.game = game
        inter.embed = embed
        # thread = Thread(target=ticker,args=(game, ))
        # thread.start()
        # inter.thread = thread
        try:
            game.load_state(open(f"./saves/{inter.author.id}.state", "rb"))
        except:
            pass
        await inter.edit_original_message(embed=embed, view=PokeMonButton(inter))


def setup(client):
    client.add_cog(PokePoke(client))