import disnake
from disnake.ext import commands
from api import connect4API

def places(board,column,player):
    if connect4API.is_valid_location(board,column):
        row = connect4API.get_next_open_row(board,column)
        board = connect4API.drop_piece(board,row,column,player)
    return board

class ConnectFourButtonCasual(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=None)
        self.inter = inter

    @disnake.ui.button(emoji="1️⃣")
    async def button_1(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,0,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
        
    @disnake.ui.button(emoji="2️⃣")
    async def button_2(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,1,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return

    @disnake.ui.button(emoji="3️⃣")
    async def button_3(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,2,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
    

    @disnake.ui.button(emoji="4️⃣")
    async def button_4(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,3,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
    

    @disnake.ui.button(emoji="5️⃣", row=1)
    async def button_5(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,4,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
    

    @disnake.ui.button(emoji="6️⃣", row=1)
    async def button_6(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,5,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
    

    @disnake.ui.button(emoji="7️⃣", row=1)
    async def button_7(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        await inter.response.defer()
        msg  = await inter.original_message()

        self.inter.board = places(self.inter.board,6,self.inter.holder[self.inter.current.id])
        if connect4API.winning_move(self.inter.board,self.inter.holder[self.inter.current.id]):
            self.inter.embed.title = f"{self.inter.current.name} wins!"
            self.inter.embed.description = connect4API.current_board(self.inter.board)
            await msg.edit(embed=self.inter.embed,view=None)
            return
        self.inter.embed.description = connect4API.current_board(self.inter.board)
        self.inter.current,self.inter.other = self.inter.other,self.inter.current
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name}'s turn")
        await msg.edit(embed=self.inter.embed)
        return
    

    @disnake.ui.button(emoji="❌", row=1)
    async def button_close(self, button: disnake.ui.Button, inter:disnake.MessageInteraction):
        if inter.author.id != self.inter.current.id:
            return await inter.send("not your game/turn.",ephemeral=True)
        self.inter.embed.title = f"{self.inter.other.display_name} won!"
        await inter.response.defer()
        msg  = await inter.original_message()
        self.inter.embed.set_footer(text=f"{self.inter.current.display_name} withdrew.")
        await msg.edit(embed=self.inter.embed,view=None)
        return      


class ConnectFour(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="connect4")
    async def connect4_game(self, inter:disnake.ApplicationCommandInteraction):
        return

    # @connect4_game.sub_command(name="bet")
    # async def connect4_game_bet(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member, bet:str):
    #     """
    #     Play connect4 with bets

    #     Parameters
    #     ----------
    #     user: User to bet on
    #     bet: betting amount
    #     """
    #     return await inter.send("todo")
    
    @connect4_game.sub_command(name="casual")
    async def connect4_game_casual(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member):
        """
        Play connect4 without bets

        Parameters
        ----------
        user: User to play connect4 with
        """
        await inter.response.defer()
        board = connect4API.create_board()
        embed = disnake.Embed(title=f"{inter.author.display_name} vs {user.display_name}", color=disnake.Colour.red())
        embed.set_footer(text=f"{inter.author.display_name}'s turn")
        embed.description = connect4API.current_board(board)
        inter.board = board
        inter.embed = embed
        inter.current = inter.author
        inter.other = user
        inter.holder = {
            inter.author.id: 1,
            user.id: 2
        }
        return await inter.edit_original_message(embed=embed, view=ConnectFourButtonCasual(inter))



def setup(client):
    client.add_cog(ConnectFour(client))