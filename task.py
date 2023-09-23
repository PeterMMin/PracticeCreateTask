player1 = {
    
    'lives': 1,

    'position': "undef",

    'choice': "under",

} 

player2 = {
    
    'lives': 1,

    'position': "undef",

    'choice': "under",

} 

winner="undef"

def playGame(input1,input2,input3,input4):
    global winner

    if input2== input3:
        print("Player 1 was hit!")
        player1['lives']= 0
        winner="Player 2"

    if input2 != input3:
        print("Player 1 was missed!")

    if input1== input4:
        print("Player 2 was hit!")
        player2['lives']= 0
        winner="Player 1"
        
    if input1 != input4:
        print("Player 2 was missed!")

    



while player1['lives'] !=0 and player2['lives'] !=0: 
    player1['choice']= input("Player 1, where would you like to shoot? L(Left), C(Center), or R(Right)")
    player1['position']= input("Player 1, where would you like to hide? L(Left), C(Center), or R(Right)")

    player2['choice']= input("Player 2, where would you like to shoot? L(Left), C(Center), or R(Right)")
    player2['position']= input("Player 2, where would you like to hide? L(Left), C(Center), or R(Right)")

    playGame(player1['choice'], player1['position'],player2['choice'], player2['position'])


    


if player1['lives']== player2['lives']:
    print("It is a tie!")
else:
    print("The winner is ", winner, "!!!")
