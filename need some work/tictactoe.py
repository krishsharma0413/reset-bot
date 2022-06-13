import disnake
from disnake.ext import commands
from api import tictactoeAPI
import asyncio

def places(board, player, pos):
    return board[pos[0]][pos[1]] == player

class challenge(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @disnake.ui.button(label="accept",style=disnake.ButtonStyle.green,custom_id="accept")
    async def accept(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        return
    
    @disnake.ui.button(label="decline",style=disnake.ButtonStyle.red, custom_id="decline")
    async def decline(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        return 

async def money_transfer(client, bet_amount,winner,looser):
    await client.database.main.update_one({"_id": winner.id}, {"$inc": {"money": bet_amount}})
    await client.database.main.update_one({"_id": looser.id}, {"$inc": {"money": -bet_amount}})

class TicTacToeButton(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="⬛")
    async def button_1(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[0,0])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛")
    async def button_2(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[0,1])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛")
    async def button_3(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[0,2])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛", row=1)
    async def button_4(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[1,0])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛", row=1)
    async def button_5(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[1,1])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛", row=1)
    async def button_6(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[1,2])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛", row=2)
    async def button_7(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[2,0])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        
    @disnake.ui.button(emoji="⬛", row=2)
    async def button_8(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[0,0])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return

    @disnake.ui.button(emoji="⬛", row=2)
    async def button_9(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)

        self.inter.board = places(self.inter.board, self.inter.holder[self.inter.current.id],[0,0])
        button.emoji = self.inter.emojis[self.inter.current.id]
        await inter.response.defer()
        msg  = await inter.original_message()
        await msg.edit(view=self) 
        if tictactoeAPI.is_wining(self.inter.board, self.inter.holder[self.inter.current.id]):
            embed = disnake.Embed(f"{self.inter.current.display_name} vs {self.inter.other.display_name}")
            embed.description = f"{self.inter.current.display_name} won!"
            embed.set_footer(text=f"{self.inter.other.display_name} lost")
            await msg.edit(embed=embed, view=None)
        self.inter.current, self.inter.other = self.inter.other, self.inter.current
        return
        

class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="tic-tac-toe")
    async def ttt_game(self, inter:disnake.ApplicationCommandInteraction):
        return

    @ttt_game.sub_command(name="bet")
    async def ttt_game_bet(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member, bet:int):
        """
        Play tic tac toe with bets

        Parameters
        ----------
        user: User to bet on
        bet: betting amount
        """
        await inter.response.defer()
        user1 = await self.client.database.main.find_one({"_id":user.id})
        if user1 is None:
            return await inter.edit_original_message(content="user doesnt use economy")
        if user1["money"] < bet:
            return await inter.edit_original_message(content="user doesnt have enough money")

        user1 = await self.client.database.main.find_one({"_id":inter.author.id})
        if user1 is None:
            return await inter.edit_original_message(content="you don't use economy.",ephemeral=True)
        if user1["money"] < bet:
            return await inter.edit_original_message(content="you don't have enough money.",ephemeral=True)       

        await inter.edit_original_message(content=f"{user.mention} do you accept this game?", view=challenge())
        try:
            interact = await self.client.wait_for("button_click", check = lambda x: x.author.id == user.id and x.channel.id == inter.channel_id, timeout = 30)
            if interact.component.custom_id == "decline":
                return await inter.edit_original_message(content="user didnt accept.",view=None)
            elif interact.component.custom_id != "accept":
                return await inter.edit_original_message(content="user didnt accept",view=None) 
        except asyncio.TimeoutError:
            return await inter.edit_original_message(content="user didnt accept",view=None)

        # board = connect4API.create_board()
        # embed = disnake.Embed(title=f"{inter.author.display_name} vs {user.display_name}", color=disnake.Colour.blue())
        # embed.set_footer(text=f"{inter.author.display_name}'s turn")
        # embed.description = connect4API.current_board(board)
        # inter.board = board
        # inter.embed = embed
        # inter.current = inter.author
        # inter.other = user
        # inter.bet_amount = bet
        # inter.client = self.client
        # inter.holder = {
        #     inter.author.id: 1,
        #     user.id: 2
        # }
        
        # return await inter.edit_original_message(content=None, embed=embed, view=ConnectFourButtonCasual(inter))
    
    @ttt_game.sub_command(name="casual")
    async def ttt_game_casual(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member):
        """
        play tic tac toe without bets.

        Parameters
        ----------
        user: User to play tic tac toe with
        """
        await inter.response.defer()
        board = tictactoeAPI.create_board()
        inter.board = board
        inter.current = inter.author
        inter.bet_amount = 0
        inter.other = user
        inter.holder = {
            inter.author.id: 1,
            user.id: 2
        }
        inter.emojis = {
            inter.author.id: "⭕",
            user.id: "❌"
        }
        return await inter.edit_original_message(view=TicTacToeButton(inter))



def setup(client):
    client.add_cog(TicTacToe(client))