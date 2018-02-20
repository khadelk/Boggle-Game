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
class Boggle():     
    def __init__(self, file='sample.dat', N = 5):
        '''Create a representation of a 5x5 Boggle board''' 
        self.size = N
        self.readData(file)
        self.F 
        #self.F = F
        #lettersForBoard = random.choices(self.F.keys(), self.F.values(), k=size)
        #self.board = [ [''] * self.size for i in range(self.size)]
        self.window = Tk()
        self.window.title('Boggle')
        self.canvas = Canvas(self.window, width = self.size*20, height = self.size*20, bg='white')
        self.canvas.pack()
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i*20, j*20, (i+1)*20, (j+1)*20)
        self.canvas.bind("<Button-1>")
        self.canvas.bind("<Button-3>") 
        self.canvas.focus_set()
        
        #def new method
        
        
        
        
        
    def readData(self, file='sample.dat'):
        myFile = open(file, 'r') 
        contents = myFile.read() 
        aList = contents.split('\n')
        myLetters = ''.join(aList)
        self.F = {}
        aDictionary = {}
        totalLetters = len(myLetters)
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
                if word[index] not in trie:
                    trie[word[index]] = {}
                x = makeTrie(trie[word[index]], index+1, word)
                trie[word[index]] = x
            return trie  
        for i in aList:
            aDictionary = makeTrie(aDictionary,0,i)
        #return F, aDictionary 
     
def makeABoard(words,size):
    return([[words[x] for x in range(0,size)] for y in range(0,size)])  
   

def useRandomChoices(diction):
    newList = []
    for i in diction.values():
        pass 
        
    