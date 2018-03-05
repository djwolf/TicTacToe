import Board
b = Board.Board()

b.printBoard()

gameOver = False
curTurn = 1
while (gameOver == False):
    b.printBoard()
    if (curTurn == 1):
        print ("Player One: type a row number and hit enter")
        r = input()
        print ("Player One: type a collumn number and hit enter")
        c = input()
        b.boardArr[r-1][c-1] = 'X'
        curTurn += 1
    else:
        print ("Player Two: type a row number and hit enter")
        r = input()
        print ("Player Two: type a collumn number and hit enter")
        c = input()
        b.boardArr[r-1][c-1] = 'O'
        curTurn -= 1

    results = b.checkConditions()
    if (results[0] == True):
        if (results[1] == 1):
            print ("board config met. player 1 wins!!")
        else:
            print ("board config met. player 2 wins!!")
        gameOver = True
