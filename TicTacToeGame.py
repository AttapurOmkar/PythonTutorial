import  random
game_input=["Null","X","0","X","0","X","0","X","0","X"]
def Board(input_game):
    print(input_game[7]+ '|' + input_game[8]+'|'+input_game[9])
    print(input_game[4]+ '|' + input_game[5]+'|'+input_game[6])
    print(input_game[1]+ '|' + input_game[2]+'|'+input_game[3])
#Board(input_game)

# Take inputs from user to select his marker
def player_input():
    marker =''
    while marker!='X' and marker != '0':
        marker =input('Player1: Please chose your marker(X or 0):')
    if marker == 'X':
     return ('X','0')
    else:
     return ('0', 'X')

#player_1,player_2=player_input()
#print("Player1:"+player_1)
#print("Player2:"+player_2)
def put_marker(game_input,marker,position):
    game_input[position]=marker

def win(game_input,marker):
    return (
        (game_input[1] == game_input[2] == game_input[3]==marker) or
        (game_input[4] == game_input[5] == game_input[6]==marker) or
        (game_input[7] == game_input[8] == game_input[9]==marker) or
        (game_input[7] == game_input[5] == game_input[3]==marker) or
        (game_input[1] == game_input[5] == game_input[9]==marker) or
        (game_input[1] == game_input[4] == game_input[4]==marker) or
        (game_input[2] == game_input[8] == game_input[8]==marker) or
        (game_input[3] == game_input[9] == game_input[9]==marker)

    )

#print(win(game_input,'X'))

def chose_player():
    player=random.randint(1,2)
    if player==1:
        return 'player 1'
    else:
        return 'player 2'

def space(game_input,position):
    return game_input[position]== ' '

def full_board_check(game_input):
    for i in range(1,10):
        if space(game_input,i):
            return  False
    return True

def player_choice(game_input):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
        position=int(input('Please choose your position(1-9) on NumPad:'))
    return position

def play_again():
    choice=input('Would you like to play again[Y/N]:')
    return choice=='Y'

while True:
    the_Board=[' ']*10
    player_1,player_2=player_input()
    print("Player1:"+player_1)
    print("Player2:" + player_2)
    turn=chose_player()
    print(turn+"will play first")

    play_game=input('Ready to play[Y/N]:')
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'player_1':
            Board(the_Board)
            position=player_choice(the_Board)
            put_marker(the_Board,player_1,position)
            if win(the_Board,player_1):
                Board(the_Board)
                print('Player 1 has Won,Yeyeyeyeye')
                game_on=False
            else:
                if full_board_check(the_Board):
                    Board(the_Board)
                    print('Game Tie')
                    game_on=False
                else:
                    turn='player_2'
        else:
            Board(the_Board)
            position = player_choice(the_Board)
            put_marker(the_Board, player_2, position)
            if win(the_Board, player_2):
                Board(the_Board)
                print('Player 2 has Won,Yeyeyeyeye')
                game_on = False
            else:
                if full_board_check(the_Board):
                    Board(the_Board)
                    print('Game Tie')
                    game_on = False
                else:
                    turn = 'player_1'

    if not play_again():
         break

