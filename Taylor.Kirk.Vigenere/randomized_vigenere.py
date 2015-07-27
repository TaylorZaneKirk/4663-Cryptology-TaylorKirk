# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:45:10 2015

@author: Taylor
"""
import random

class Vigenere(object):
    
    #Initialize Vigenere object.
        #Sets the random seed based on integer passed to the object
        #Establishes all valid symbols
        #Generates empty matrix which will contain values for encryption/decryption
        #Generates a keyword based on the integer passed to the object
    def __init__(self, seed):
        random.seed(seed)
        self.seed = seed
        self.symbols= """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        self.Table = [[0 for i in range(len(self.symbols))] for i in range(len(self.symbols))]
        self.keyWord = ""
        self.message = ""
        self.ciphertext = ""
        self.keywordFromSeed(seed)
     
    #Sets the plaintext that will be encrypted/decrypted
    def setMessage(self,message):
        self.message = message
        
    #Generate psuedorandom keyword from seed
    def keywordFromSeed(self,seed):
        Letters = []
        
        while seed > 0:
            Letters.insert(0,chr((seed % 100) % 26 + 65))
            seed = seed // 100
        self.keyWord = "".join(Letters)
        self.buildVigenere()
    
    #Contructs a 95 x 95 matrix filled randomly with no repeats within same line
    def buildVigenere(self):
        random.seed(self.seed)
        temp = list(self.symbols)
        random.shuffle(temp)
        temp = ''.join(temp)
        
        for sym in temp:
            random.seed(self.seed)
            myList = []
            for i in range(len(temp)):
                r = random.randrange(len(temp))
                if r not in myList:
                    myList.append(r)
                else:
                    while(r in myList):
                        r = random.randrange(len(temp))
                    myList.append(r)
                while(self.Table[i][r] != 0):
                    r = (r + 1) % len(temp)
                self.Table[i][r] = sym
    
    #Encryption function that iterates through both the message and the keyword
        #and grabs values from Table based on the ordinal value of the current
        #character being pointed to be the iterator
    def encrypt(self):
        for i in range(len(self.message)):
            mi = i
            ki = i % len(self.keyWord)
            self.ciphertext = self.ciphertext + self.eRetrieve(ki,mi)
            
    def eRetrieve(self,ki,mi):       
        row = ord(self.message[mi]) - 32
        col = ord(self.keyWord[ki]) - 32
        return self.Table[row][col]
        
    #Decryption function that iterates through both the message and the keyword
        #and grabs values from Table based on the ordinal value of the current
        #keyWord character being pointed to be the iterator, then traversing the
        #row that corresponds to that value. While traversing that row, once there
        #is a match of the message value being searched for, take the iterator value
        #and convert it to an ascii character. This is the decrypted character
    def decrypt(self):
        self.ciphertext = ""
        for i in range(len(self.message)):
            emi = i
            ki = i % len(self.keyWord)
            self.ciphertext = self.ciphertext + self.dRetrieve(ki,emi)
        
    def dRetrieve(self,ki,emi):
        n = len(self.symbols)
        whichRow = ord(self.keyWord[ki]) - 32
        for i in range(n):
            if self.Table[i][whichRow] == self.message[emi]:
                decryptChar = chr(i + 32)
                return(decryptChar)