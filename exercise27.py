game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player_one = "X"
player_two = "O"

turn = player_one


while True:      
    print(game[0])
    print(game[1])
    print(game[2])

    print("Turn of ",turn)
    move = input("Where do you want to move(row, col): ")

    # move will now be a list (row, col)
    move = move.split(",")
    print(move)

    game[move[0]][move[1]] = turn

