#!/usr/local/anaconda/bin/python
######################################################################
# Khadidja Elkeurti
# A01
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("kelkeurti",))

######################################################################
import random 
from tkinter import *

def lettersForBoard(lettersDict, weightsDict, size):
    return random.choices(list(lettersDict),weights = list(weightsDict), k=size)
    
class Boggle():     
    def __init__(self, file='words.dat', N = 5):
        '''Creates a representation of a 5x5 Boggle board and initializes methods used to play the Boggle game.'''
        print("Welcome to game Boggle! Let's play!")
        self.size = N
        self.readData(file)
        self.board = [lettersForBoard(self.F.keys(),self.F.values(), N) for i in range(self.size)]
        self.window = Tk()
        self.window.title('Boggle')
        self.canvas = Canvas(self.window, width = self.size*100, height = self.size*100, bg='white')
        self.canvas.pack()
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*100, j*100, (i+1)*100, (j+1)*100)
                self.canvas.create_text((i*100)+50, (j*100)+50, font="Times 100 italic bold", fill="blue", text=self.board[i][j])
        self.canvas.bind("<Button-1>", self.extend)
        self.canvas.bind("<n>", self.new)
        self.canvas.bind("<r>", self.reset) 
        self.canvas.focus_set()
        self.aDictionary
        self.ckSoln
        self.solve
        self.soln = []
        self.aList
                      
    
    def ckSoln(self, soln):
        '''Checks to see if a path created in our solution is a path that leads to a valid word in our trie dictionary'''
        listofRow = []
        listofCol = []
        # Here we check to see that each coordinate is only one unit away from the next one, i.e., the letters clicked on
        # the board are directly to the left, right, or diagonal of each other
        for coord in range(len(soln)):
            row = soln[coord][0]
            listofRow.append(row)
            col = soln[coord][1]
            listofCol.append(col)
        for i in range(len(listofRow)):
            if i < (len(listofRow) -1):
                if (abs(listofRow[i+1] - listofRow[i]) > 1):
                    return False
        for i in range(len(listofCol)):
            if i < (len(listofCol) -1):
                if (abs(listofCol[i+1] - listofCol[i]) > 1):
                    return False
        # This helper function recursively checks to see if the coordinates in the solution tuple list create a
        # path in our trie dictionary 
        def isitAPath(soln, aDictionary):
            myCol = soln[0][1]
            myRow = soln[0][0]
            letter = self.board[myCol][myRow]
            if len(soln) > 5:
                return False
            if len(soln) == 1 and letter in aDictionary:
                return aDictionary[letter]
            if letter in aDictionary:
                recursiveFcn = isitAPath(soln[1:], aDictionary[letter])
                return recursiveFcn
            if letter not in aDictionary.keys():
                return False 
        return isitAPath(soln, self.aDictionary)
    
    def extend(self, event):
        '''Checks to see if each tile clicked is a viable solution, i.e., leads to a word. If the tile is
        viable, color it green. If the path is not viable, color the tile red.'''
        row = event.x//100
        col = event.y//100
        print(event)
        print(self.board[event.x//100])
        self.soln.append((col, row))
        if self.ckSoln(self.soln) != False:
            self.canvas.create_oval(row*100, col*100, (row+1)*100, (col+1)*100, fill = 'green')
            self.canvas.create_text((row*100)+50, (col*100)+50, font="Times 100 italic bold", fill="blue", text=self.board[row][col])
            #when a word is found, a print statement is made that tells the user to reset the board
            if len(self.soln) == 5:
                print("You have found word '{}'! Press key 'r' to reset your board. Press key 'n' to create a new board.".format(self.ckSoln(self.soln)))
        else:
            print("Uh oh, not a valid move. Press key 'r' to restart your current board. Press key 'n' to create a new board.")
            self.canvas.create_oval(row*100, col*100, (row+1)*100, (col+1)*100, fill = 'red')
            self.canvas.create_text((row*100)+50, (col*100)+50, font="Times 100 italic bold", fill="blue", text=self.board[row][col])           

    def new(self, event):
        '''This method lets the user reset the game and creates a new board'''
        newBoard = [lettersForBoard(self.F.keys(),self.F.values(), self.size) for i in range(self.size)]
        del self.soln[:]
        self.board = newBoard
        for i in range(self.size):
            for j in range(self.size):                
                self.canvas.create_rectangle(i*100, j*100, (i+1)*100, (j+1)*100, fill = "white")
                self.canvas.create_text((i*100)+50, (j*100)+50, font="Times 100 italic bold", fill="blue", text=newBoard[i][j])
        self.new
        
                
    
    def reset(self,event):
        '''This resets the game but preserves the letters in the current board'''
        del self.soln[:]
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*100, j*100, (i+1)*100, (j+1)*100, fill = "white")
                self.canvas.create_text((i*100)+50, (j*100)+50, font="Times 100 italic bold", fill="blue", text=self.board[i][j])
        self.reset
    
    def solve(self):
        '''This method finds all of the viable words in the board and creates an answer key using those words
        It creates a list of all the x and y coordinates on the board
        and attempts to recursively compare them with the next possible moves and adds them to a list if they are
        a path in the trie.'''
        def legalMove(coord, board):
            row = coord[0]
            col = coord[1]
            return row in range(len(board)) and col in range(len(board))
                
        def isPath(coord, dictionary):
            row = coord[0]
            col = coord[1]
            return self.board[row][col] in list(dictionary.keys())
            
        def getDirections(currentCoord):
            moves = []
            row = currentCoord[0]
            col = currentCoord[1]
            moves.append((row+1, col))
            moves.append((row-1, col))
            moves.append((row-1,col-1))
            moves.append((row+1,col+1))
            moves.append((row, col+1))
            moves.append((row, col-1))
            legal = []
            for move in moves:
                if legalMove(move, self.board):
                    legal.append(move)
            return legal
            
        def solveHelper(coord, trie, currentKey):
            row = coord[0]
            col = coord[1]
            if isPath(coord, trie):
                currentKey += [coord]
                if trie[self.board[row][col]] in self.aList:
                    return currentKey
                if len(currentKey) == 5:
                    return currentKey
                else:
                    newTrie = trie[self.board[row][col]]
                    legalMoves = getDirections(coord)
                    for move in legalMoves:
                        if move != coord:
                            return solveHelper(move, newTrie, currentKey)
                print(currentKey)

        listOfCoords = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                coord = (row, col)
                if coord not in listOfCoords:
                    listOfCoords.append(coord)

        answerKey = []
        for pos in listOfCoords:
            currentKey = []
            if isPath(pos, self.aDictionary):
                trie = self.aDictionary[self.board[pos[0]][pos[1]]]
                currentKey += [pos]
                possibleNextMoves = getDirections(pos)
                for move in possibleNextMoves:
                    return(solveHelper(move, trie, currentKey)) 
        
    def readData(self, file='words.dat'):
        '''This function takes a file and parses the words in that file and creates a frequency dictionary, which represents how often the letters occur in the file and a Trie, which creates a path between the letters and the words'''
        myFile = open(file, 'r')
        contents = myFile.read() 
        self.aList = contents.split('\n')
        myLetters = ''.join(self.aList)
        totalLetters = len(myLetters)
        self.F = {}
        self.aDictionary = {}
        for letter in myLetters:               
            # count the frequency that each letter appears
            if letter in self.F:
                self.F[letter] += 1/totalLetters 
            else:
                self.F[letter] = 1/totalLetters 
        # make a helper function that incorporates recursion
        def makeTrie(trie, index, word):
            if index == len(word) - 1:
                trie[word[index]] = word
                return trie 
            else:
                if(index < len(word)):
                    if word[index] not in trie:
                        trie[word[index]] = {}
                    x = makeTrie(trie[word[index]], index+1, word)
                    trie[word[index]] = x
            return trie
        for i in self.aList:
            self.aDictionary = makeTrie(self.aDictionary,0,i)
        return self.F 
