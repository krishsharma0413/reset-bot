"""
modified code from https://github.com/Jack92829/Maze-Generation
"""
import random

class Cell:
    """Cell class that defines each walkable Cell on the grid"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True] # Left, Right, Up, Down


    def getChildren(self, grid: list) -> list:
        """Check if the Cell has any surrounding unvisited Cells that are walkable"""
        a = [(1, 0), (-1,0), (0, 1), (0, -1)]
        children = []
        for x, y in a:
            if self.x+x in [len(grid), -1] or self.y+y in [-1, len(grid)]:
                continue
            
            child = grid[self.y+y][self.x+x]
            if child.visited:
                continue
            children.append(child)
        return children


def removeWalls(current: Cell, choice: Cell):
    """Removeing the wall between two Cells"""
    if choice.x > current.x:     
        current.walls[1] = False
        choice.walls[0] = False
    elif choice.x < current.x:
        current.walls[0] = False
        choice.walls[1] = False
    elif choice.y > current.y:
        current.walls[3] = False
        choice.walls[2] = False
    elif choice.y < current.y:
        current.walls[2] = False
        choice.walls[3] = False


def drawWalls(grid: list, binGrid: list) -> list:
    """Draw existing walls around Cells"""
    for yindex, y in enumerate(grid):
        for xindex, x in enumerate(y):
            for i, w in enumerate(x.walls):
                if i == 0 and w:
                    binGrid[yindex*2+1][xindex*2] = 1
                if i == 1 and w:
                    binGrid[yindex*2+1][xindex*2+2] = 1
                if i == 2 and w:
                    binGrid[yindex*2][xindex*2+1] = 1
                if i == 3 and w:
                    binGrid[yindex*2+2][xindex*2+1] = 1
    return binGrid


def drawBorder(grid: list) -> list:
    """Draw a border around the maze"""
    length = len(grid)
    for row in grid:
        row[0] = row[length-1] = 1
        
    grid[0] = grid[length-1] = [1] * length
    return grid

def displayMaze(grid: list):
    """Draw the maze using ASCII characters and display the maze"""
    binGrid = []
    length = len(grid)*2+1
    for x in range(length):
        if x % 2 == 0:
            binGrid.append([0 if x % 2 != 0 else 1 for x in range(length)])
        else:
            binGrid.append([0] * length)
    
    binGrid = drawWalls(grid, binGrid)
            
    binGrid = drawBorder(binGrid)
    # print(binGrid)
    return binGrid

def makemaze():
    size = 6
    grid = [[Cell(x, y) for x in range(size)] for y in range(size)]
    current = grid[0][0]
    stack = []

    # Main loop to generate the maze
    while True:
        current.visited = True
        children = current.getChildren(grid)

        if children:
            choice = random.choice(children)
            choice.visited = True

            stack.append(current)

            removeWalls(current, choice)

            current = choice
        
        elif stack:
            current = stack.pop()
        else:
            break



    # Display the maze
    grid = displayMaze(grid)
    grid[1][1] = 2
    grid[11][11] = 3
    return grid

def analyse(game):
    game["goal"] = []
    for x in range(len(game["board"])):
        for y in range(len(game["board"][x])):
            if game["board"][x][y] == 3:
                game["goal"].append([x, y])
    return game

def rendermaze(grid):
    ret = ""
    for x in grid:
        for y in x:
            if y == 1:
                ret += '⬛'
            elif y == 2:
                ret += '😔'
            elif y == 3:
                ret += '🟩'
            else:
                ret += '⬜'
        ret += '\n'
    return ret

def goal_render(game):
    for x in game["goal"]:
        if game["board"][x[0]][x[1]] in [0]:
            game["board"][x[0]][x[1]] = 3

def up(game):
    board = game["board"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]-1][player_pos[1]] in [0, 3]:
        board[player_pos[0]-1][player_pos[1]] = 2
        board[player_pos[0]][player_pos[1]] = 0
    goal_render(game)
    game["board"] = board
    return game

def down(game):
    board = game["board"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]+1][player_pos[1]] in [0, 3]:
        board[player_pos[0]+1][player_pos[1]] = 2
        board[player_pos[0]][player_pos[1]] = 0
    goal_render(game)
    game["board"] = board
    return game

def left(game):
    board = game["board"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]][player_pos[1]-1] in [0, 3]:
        board[player_pos[0]][player_pos[1]-1] = 2
        board[player_pos[0]][player_pos[1]] = 0
    goal_render(game)
    game["board"] = board
    return game

def right(game):
    board = game["board"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]][player_pos[1]+1] in [0, 3]:
        board[player_pos[0]][player_pos[1]+1] = 2
        board[player_pos[0]][player_pos[1]] = 0
    goal_render(game)
    game["board"] = board
    return game

def create():
    game = {}
    game["board"] = makemaze()
    game["playing"] = True
    game = analyse(game)
    return game

def is_winning(game):
    compelete = 0
    for x in game["goal"]:
        if game["board"][x[0]][x[1]] in [2]:
            compelete+=1
        else:
            return False
    return compelete == len(game["goal"])