import json

def is_winning(game):
    compelete = 0
    for x in game["goal"]:
        if game["map"][x[0]][x[1]] in [3]:
            compelete+=1
        else:
            return False
    return compelete == len(game["goal"])


def goal_render(game):
    for x in game["goal"]:
        if game["map"][x[0]][x[1]] in [0]:
            game["map"][x[0]][x[1]] = 4


def analyse(game):
    game["goal"] = []
    for x in range(len(game["map"])):
        for y in range(len(game["map"][x])):
            if game["map"][x][y] == 4:
                game["goal"].append([x, y])
    return game


def name_checker(name):
    with open("./asset/levels.json", "r") as f:
        levels = json.load(f)
    if name in levels:
        return False
    return True


def left(game):
    board = game["map"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]][player_pos[1]-1] in [0, 4]:
        board[player_pos[0]][player_pos[1]-1] = 2
        board[player_pos[0]][player_pos[1]] = 0

    elif board[player_pos[0]][player_pos[1]-1] == 3:
        if board[player_pos[0]][player_pos[1]-2] in [0, 4]:
            board[player_pos[0]][player_pos[1]-2] = 3
            board[player_pos[0]][player_pos[1]-1] = 2
            board[player_pos[0]][player_pos[1]] = 0
    goal_render(game)

    game["map"] = board
    return game


def update_playcount(level):
    try:
        with open("./asset/levels.json", "r") as f:
            levels = json.load(f)
        levels[str(level)]["played"] += 1
        with open("./asset/levels.json", "w") as f:
            json.dump(levels, f, indent=4)
    except:
        pass


def raw_creator(string):
    ret = []
    string = string.split("/")
    for x in string:
        ret.append(list(map(lambda x: int(x), list(x))))
    return ret


def right(game):
    board = game["map"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]][player_pos[1]+1] in [0, 4]:
        board[player_pos[0]][player_pos[1]+1] = 2
        board[player_pos[0]][player_pos[1]] = 0
    elif board[player_pos[0]][player_pos[1]+1] == 3:
        if board[player_pos[0]][player_pos[1]+2] in [0, 4]:
            board[player_pos[0]][player_pos[1]+2] = 3
            board[player_pos[0]][player_pos[1]+1] = 2
            board[player_pos[0]][player_pos[1]] = 0  
    goal_render(game)
    game["map"] = board
    return game



def up(game):
    board = game["map"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    if board[player_pos[0]-1][player_pos[1]] in [0, 4]:
        board[player_pos[0]-1][player_pos[1]] = 2
        board[player_pos[0]][player_pos[1]] = 0

    elif board[player_pos[0]-1][player_pos[1]] == 3:
        if board[player_pos[0]-2][player_pos[1]] in [0, 4]:
            board[player_pos[0]-2][player_pos[1]] = 3
            board[player_pos[0]-1][player_pos[1]] = 2
            board[player_pos[0]][player_pos[1]] = 0

    goal_render(game)
    game["map"] = board
    return game


def down(game):
    board = game["map"]
    for x in board:
        for y in x:
            if y == 2:
                player_pos = [board.index(x), x.index(y)]
    try:
        if board[player_pos[0]+1][player_pos[1]] in [0, 4]:
            board[player_pos[0]+1][player_pos[1]] = 2
            board[player_pos[0]][player_pos[1]] = 0

        elif board[player_pos[0]+1][player_pos[1]] == 3:
            try:
                if board[player_pos[0]+2][player_pos[1]] in [0, 4]:
                    board[player_pos[0]+2][player_pos[1]] = 3
                    board[player_pos[0]+1][player_pos[1]] = 2
                    board[player_pos[0]][player_pos[1]] = 0
            except:
                board[player_pos[0]+1][player_pos[1]] = 2
                board[player_pos[0]][player_pos[1]] = 0

    except:
        pass
    goal_render(game)
    game["map"] = board
    return game

# def sokoban_render_temp(game):
#     for x in game["map"]:
#         print(x)

def render_perm(game):
    ret = ""
    for x in range(len(game["map"])):
        for y in range(len(game["map"][x])):
            if game["map"][x][y] == 0:
                ret += "⬛"
            elif game["map"][x][y] == 1:
                ret += "⬜"
            elif game["map"][x][y] == 2:
                ret += "😔"
            elif game["map"][x][y] == 3:
                ret += "🟫"
            elif game["map"][x][y] == 4:
                ret += "🟩"
        ret += "\n"
    return ret


def create(level):
    level = str(level)
    with open("./asset/levels.json", "r") as f:
        levels = json.load(f)
    if level not in levels:
        return levels["1"]
    else:
        return levels[level]

def add(name, custom_creator):
    with open("./asset/levels.json", "r") as f:
        levels = json.load(f)
    levels[name] = custom_creator
    with open("./asset/levels.json", "w") as f:
        json.dump(levels, f, indent=4)