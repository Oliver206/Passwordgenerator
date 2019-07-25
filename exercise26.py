game = [[1, 2, 0], 
        [2, 1, 0], 
        [2, 1, 1]]

def get_winner(x, y):
    if game[x][y] == 1:
        return "Player one won!"
    if game[x][y] == 2:
        return "Player two won!"

def is_winner():
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2]:    # rows
            if game[i][0] != 0:
                return get_winner(i, 0)
        if game[0][i] == game[1][i] == game[2][i]:   # columns
            if game[0][i] != 0:
                return get_winner(0, i)
        if game[0][0] == game[1][1] == game[2][2]:
            if game[0][0] != 0:
                return get_winner(0, 0)
        if game[0][2] == game[1][1] == game[2][0]:
            if game[0][2] != 0:
                return get_winner(0, 2)
        else:
            return "We don't have any winner."

print(is_winner())