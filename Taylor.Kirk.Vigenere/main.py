###############################################
# Name: Taylor Kirk
# Class: CMPS XXXX Cryptography
# Date: 27 July 2015
# Program 2 - Randomized Vigenere Cipher
###############################################

import argparse
import randomized_vigenere as rv

def main():
    
    #Parse parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", default = "inputFile.txt", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", default = "outputFile.txt", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed", default =7487383487438734, help="Integer seed")
    args = parser.parse_args()
    
    #Set seed and generate keyword
    seed = args.seed
    
    #Construct Matrix
    f = open(args.inputFile,'r')
    message = f.read()
    Matrix = rv.Vigenere(seed)
    Matrix.setMessage(message)
    
    if(args.mode == 'encrypt'):
        Matrix.encrypt()
    else:
        Matrix.decrypt()
    
    o = open(args.outputFile,'w')
    o.write(str(Matrix.ciphertext))
    
    print("Seed used:",Matrix.seed)
    print("Key Generated:",Matrix.keyWord)
    print("Original Message:",Matrix.message)
    print("Decoded Message:",Matrix.ciphertext)
    
if __name__ == '__main__':
    main()