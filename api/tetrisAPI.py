from disnake import Colour
from tetris import BaseGame, Move, MoveKind, MoveDelta, PieceType, MinoType
from tetris.engine import Gravity
from tetris.impl import custom
from tetris.impl import scorer
from typing import Optional

class PerMoveGravity(Gravity):
    TILES_PER_MOVE = 1
    MAX_MOVES_AFTER_TOUCH = 5

    def __init__(self, game: BaseGame):
        super().__init__(game)
        self.touched = False
        self.before_lock = 0

    def calculate(self, delta: Optional[MoveDelta] = None) -> None:
        if delta is not None:
            # We were called inside `push()`
            if delta.auto:
                return

            if delta.kind == MoveKind.hard_drop or delta.kind == MoveKind.swap:
                self.touched = False

            piece = self.game.piece
            if self.touched:
                self.before_lock -= 1

            elif self.game.rs.overlaps(minos=piece.minos, px=piece.x + 1, py=piece.y):
                # The piece is resting on a tile
                self.touched = True
                self.before_lock = self.MAX_MOVES_AFTER_TOUCH

            if self.touched and self.before_lock == 0:
                self.game.push(Move(kind=MoveKind.hard_drop, auto=True))
                self.touched = False

            self.game.push(Move(kind=MoveKind.soft_drop, x=self.TILES_PER_MOVE, auto=True))




tiles = {
    MinoType.I:"🟦",
    MinoType.J:"🟫",
    MinoType.L:"🟧",
    MinoType.O:"🟨",
    MinoType.S:"🟩",
    MinoType.T:"🟪",
    MinoType.Z:"🟥",
    MinoType.EMPTY:"⬛",
    MinoType.GHOST:"◽"
}

def color_detector(piece):
    return {
        "I": [Colour(int("#4287f5".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451973925044244/unknown.png"],
        "J": [Colour(int("#6b2e2e".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451884649267270/unknown.png"],
        "L": [Colour(int("#e3a220".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451422969655356/unknown.png"],
        "O": [Colour(int("#f5d800".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451826709164052/unknown.png"],
        "S": [Colour(int("#00d851".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451980736577556/unknown.png"],
        "T": [Colour(int("#6307f7".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451957818896404/unknown.png"],
        "Z": [Colour(int("#f70006".strip("#"), 16)), "https://cdn.discordapp.com/attachments/907213435358547968/985451967755198494/unknown.png"]
    }[piece]

def render(game):
    return game.render(tiles=tiles)

def next_piece(game):
    try:
        nex = game.queue[0]
        if nex == PieceType.I:
            return "I"
        elif nex == PieceType.J:
            return "J"
        elif nex == PieceType.L:
            return "L"
        elif nex == PieceType.O:
            return "O"
        elif nex == PieceType.S:
            return "S"
        elif nex == PieceType.T:
            return "T"
        elif nex == PieceType.Z:
            return "Z"
        else:
            return "none"
    except:
        return "none"

def create_game():
    game = BaseGame(custom.CustomEngine,board_size=(15,10), scorer=scorer.GuidelineScorer)
    game.engine.parts["gravity"] = PerMoveGravity
    game.reset()
    return game