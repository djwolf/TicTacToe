import Board
b = Board.Board()
b.printBoard()

gameOver = False
curTurn = 1
while (gameOver == False):
    b.printBoard()
    if (curTurn == 1):
        validInputRow = False
        validInputCol = False
        while (validInputRow == False or validInputCol == False):
            try:
                print ("Player One: type a row number and hit enter")
                r = int(input())
                if (r > 0 and r <= 3):
                    validInputRow = True
                    print ("Player One: type a collumn number and hit enter")
                    c = int(input())
                    if (c > 0 and c <= 3):
                        validInputCol = True
                    else:
                        print ("Invalid Input!")
                else:
                    print ("Invalid Input!")
            except ValueError as e:
                print ("Invalid Input!")
        
        b.boardArr[r-1][c-1] = 'X'
        curTurn += 1
    else:
        print ("Player Two: type a row number and hit enter")
        r = int(input())
        print ("Player Two: type a collumn number and hit enter")
        c = int(input())
        b.boardArr[r-1][c-1] = 'O'
        curTurn -= 1

    results = b.checkConditions()
    if (results[0] == True):
        if (results[1] == 1):
            print ("board config met. player 1 wins!!")
        else:
            print ("board config met. player 2 wins!!")
        gameOver = True

    if (gameOver == False):
        if (b.checkDraw()):
            b.printBoard()
            print ("board config met. game is a draw")
            gameOver = True
