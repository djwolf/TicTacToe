from __future__ import print_function

class Board(object):
    boardArr = [['a' for i in range(3)] for k in range(3)]
    
    def __init__(self):
        print ("class initialized. printing board")

    def printBoard(self):
        #print out the current state of the board
        print ("-------\n|",end='')
        for i in range(0,3):
            for k in range(0,3):
                print (self.boardArr[i][k], end='')
                print ("|",end='')
            print ("\n-------")
            if (i != 2):
                print ("|",end='')
    
    def checkConditions(self):
        possibleValues = ['X','O']
        for i in range(0,3):
            #check rows
            if (self.boardArr[i][0] in possibleValues):
                if ((self.boardArr[i][0] == self.boardArr[i][1]) and (self.boardArr[i][1] == self.boardArr[i][2])):
                    print ("row config met")
                    if (self.boardArr[i][0] == 'X'):
                        return [True, 1]
                    else:
                        return [True, 2]

        for i in range(0,3):
            #check collums
            if (self.boardArr[0][i] in possibleValues):
                if ((self.boardArr[0][i] == self.boardArr[1][i]) and (self.boardArr[1][i] == self.boardArr[2][i])):
                    print ("collumn config met")
                    if (self.boardArr[0][i] == 'X'):
                        return [True, 1]
                    else:
                        return [True, 2]
        
        if (self.boardArr[0][0] in possibleValues):
            #check diagonal
            if ((self.boardArr[0][0] == self.boardArr[1][1]) and (self.boardArr[1][1] == self.boardArr[2][2])):
                print ("diag config met")
                if (self.boardArr[0][0] == 'X'):
                    return [True, 1]
                else:
                    return [True, 2]
            
        if (self.boardArr[0][2] in possibleValues):
            #check the other diagonal
            if ((self.boardArr[0][2] == self.boardArr[1][1]) and (self.boardArr[1][1] == self.boardArr[2][0])):
                print ("diag config met2")
                if (self.boardArr[0][2] == 'X'):
                    return [True, 1]
                else:
                    return [True, 2]
        return [False,-1]