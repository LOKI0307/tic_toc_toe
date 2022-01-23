board={1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
def game_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])



def update_board(pos,val):
    board[pos] = val

def check_winner(player):
    if board[1] == board[2] == board[3] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[4] == board[5] == board[6] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[7] == board[8] == board[9] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[1] == board[4] == board[7] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[2] == board[5] == board[8] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[3] == board[6] == board[9] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[7] == board[5] == board[3] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[1] == board[5] == board[9] == 'x':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[1] == board[2] == board[3] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[4] == board[5] == board[6] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[7] == board[8] == board[9] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[1] == board[4] == board[7] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[2] == board[5] == board[8] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[3] == board[6] == board[9] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[7] == board[5] == board[3] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"

    if board[1] == board[5] == board[9] == 'o':
        print(5*"*"+"{} win".format(player)+"*"*5)
        return "True"


def pos_check(pos,val):
    if board[pos] == "":
        update_board(pos, val)
        return True
    else:
        return False
    #pos = int(input("user 1 enter the position for o value:-  "))

def default_message():
    print(5 * "*" + "Hey Friends let's play Tic-Toc-Toe" + "*" * 5)
    print (80*"*")
    print (80*"*")
    print('''
    There are two modes of game.
    press 1 for play game with computer
    press 2 for play game with friend
    ''')
    print (80 * "*")
    print (80 * "*")
    try:
        game_mode = int(input("Enter the game mode:- "))
    except NameError:
        print(" NameError occurred. Some input isn't defined. Please enter either 1 or 2 ")
        default_message()
    if game_mode not in [1,2]:
        default_message()
    else:
        return game_mode

def user_info(mode):
    cmp = "Computer"
    if mode == 1:
        user1 = str(raw_input("Please enter player 1 name:- "))
        return user1,cmp
    elif mode == 2:
        user1 = str(raw_input("Please enter player 1 name:- "))
        user2 = str(raw_input("Please enter player 2 name:- "))
        return user1,user2




