from random import randint
from test import *


game_state = True


if __name__ == "__main__":

    mode = default_message()
    Player1,Player2 = user_info(mode)
    print ('say hello {} to {}. Game is going to start now'.format(Player1,Player2))
    if mode == 1:
        i = 1
        while i < 10:
            if i % 2 != 0:
                pos = int(input("{} please enter the position between (0-9) for o value:-  ".format(Player1)))
                while pos_check(pos, 'o') is False:
                    # print("i am here2")
                    pos = int(input("Given position already has a value choose other place for o value:-  "))

                game_board(board)
                if check_winner(Player1):
                    i = 100

                    # game_state == False
                    break
            else:
                pos = randint(1,9)
                print ("Computer enter value at {} position ".format(pos))
                while pos_check(pos, 'x') is False:
                    # print("i am here2")
                    pos = randint(1,9)

                game_board(board)
                if check_winner("Computer"):
                    i = 100
                    # game_state == False
                    break

            i += 1

    elif mode == 2:
        i = 1
        while i < 10:
            if i % 2 != 0:
                pos = int(input("{} please enter the position between (0-9) for o value:-  ".format(Player1)))
                while pos_check(pos,'o') is  False:
                    #print("i am here2")
                    pos = int(input("Given position already has a value choose other place for o value:-  "))

                game_board(board)
                if check_winner(Player1):
                    i = 100

                    # game_state == False
                    break
            else:
                pos = int(input("{} please enter the position between (0-9) for x value:-  ".format(Player2)))
                while pos_check(pos,'x') is False:
                    #print("i am here2")
                    pos = int(input("Given position already has a value choose other place for x value:-  "))

                game_board(board)
                if check_winner(Player2):
                    i = 100
                    # game_state == False
                    break

            i += 1

        game_board(board)
else:
    print ("No one win this game try next time")

