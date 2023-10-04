board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board():
    print(" +-------+-------+-------+\n",
          "|        |       |       |\n",
          "|  ",board[0][0],"   |  ",board[0][1],"  |  ",board[0][2],"  |   \n",
          "|        |       |       |\n",
          " +-------+-------+-------+\n",
          "|        |       |       |\n",
          "|  ",board[1][0],"   |  ",board[1][1],"  |  ",board[1][2],"  |   \n",
          "|        |       |       |\n",
          " +-------+-------+-------+\n",
          "|        |       |       |\n",
          "|  ",board[2][0],"   |  ",board[2][1],"  |  ",board[2][2],"  |   \n",
          "|        |       |       |\n",
          " +-------+-------+-------+\n",)

board[1][1] = "X"
free_spots = ["-"]
free_fields = ["-"]
computer_move = "-"

def make_list_of_free_fields():
    global board, free_spots, free_fields
    free_spots.clear()
    free_fields.clear()
    for i in range(0,3):
        for j in range(0,3):
            if isinstance(board[i][j],int) == True:
                free_fields.append((i, j))
    for i in range(len(free_fields)):
        board_number = (free_fields[i][0] * 3) + (free_fields[i][1] + 1)
        free_spots.append(board_number)

def victory_for():
    global free_spots
    if board[0][0] == board[0][1] == board[0][2]:
        display_board()
        print(board[0][0],"wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        display_board()
        print(board[1][0], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        display_board()
        print(board[2][0], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[0][0] == board[1][0] == board[2][0]:
        display_board()
        print(board[0][0], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        display_board()
        print(board[0][1], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        display_board()
        print(board[0][2], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        display_board()
        print(board[0][0], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        display_board()
        print(board[0][2], "wins!")
        input("Press enter to exit the game:")
        exit()
        return True
    elif len(free_spots) == 0:
        display_board()
        print("It`s a tie!")
        input("Press enter to exit the game:")
        exit()
        return True
    else:
        return False

def draw_move():
    global computer_move, free_spots
    import random
    computer_move = random.choice(free_spots)

def enter_move():
    global free_spots
    while victory_for() == False:
        try:
            make_list_of_free_fields()
            display_board()
            player_move = int(input("Enter your move: "))
            while player_move not in free_spots:
                    player_move = int(input("That is not a valid spot. Try again."))
            if player_move == 1:
                board[0][0] == "O"
            if player_move == 2:
                board[0][1] == "O"
            if player_move == 3:
                board[0][2] == "O"
            if player_move == 4:
                board[1][0] == "O"
            if player_move == 5:
                board[1][1] == "O"
            if player_move == 6:
                board[1][2] == "O"
            if player_move == 7:
                board[2][0] == "O"
            if player_move == 8:
                board[2][1] == "O"
            if player_move == 9:
                board[2][2] == "O"
            if victory_for() == True:
                victory_for()
            display_board()
            make_list_of_free_fields()
            draw_move()
            if computer_move == 1:
                board[0][0] = "X"
            if computer_move == 2:
                board[0][1] = "X"
            if computer_move == 3:
                board[0][2] = "X"
            if computer_move == 4:
                board[1][0] = "X"
            if computer_move == 5:
                board[1][1] = "X"
            if computer_move == 6:
                board[1][2] = "X"
            if computer_move == 7:
                board[2][0] = "X"
            if computer_move == 8:
                board[2][1] = "X"
            if computer_move == 9:
                board[2][2] = "X"
            make_list_of_free_fields()
            continue
        except:
            print("That is not a valid spot. Try again.")
            continue
        else:
            print("I don`t know what happend. Check enter_move() function.")
            input("Press enter to exit the game: ")
            exit()

enter_move()

