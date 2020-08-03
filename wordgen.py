#!/usr/bin/python3.8
import string
import os
import time

low = string.ascii_lowercase
up = string.ascii_uppercase
limit = 8
start = 8
actual = 0

def banniere():
    os.system('figlet WORDGEN')
    print("V:1.0.1")

def stringToChars(strng):
    charList = []
    for c in strng:
        charList.append(c)
    return charList

def generate(wordlist,low,up,*props):
    if len(props) == 3:
        start,limit,actual = props[0],props[1],props[2]
    if len(props) == 2:
        start,limit,actual = props[0],props[1],0
    if len(props) == 1:
        start,limit,actual = props[0],props[0],0 
    if not len(props):
        start,limit,actual = 4,4,0 
    word = ""
    col = 0
    cn = 0
    while col < limit:

        for char in str(low):

            while actual < start:
                word += stringToChars(low)[col]
                actual += 1

            wordlist.append(word)
            actual = 0
            tabWord = stringToChars(wordlist[0])
            tabWord[col] = char
            wordlist.append("".join(tabWord))

            while actual < start:
        
                tabWord = stringToChars(wordlist[-1])
        
                if actual != 0:

                    for c in str(low): #stringToChars(low)[colChar] 

                        tabWord[len(tabWord)-actual] = c 
                        # time.sleep(0.04)
                        word = ""

                        for ch in tabWord:
                            word+=ch

                        time.sleep(0.005)
                        os.system('clear')
                        # banniere()

                        # print(f"mot actuel:                                           {word}")
                        print(f"{word}")

                        wordlist.append(word)
                # word = wordlist[-1]
                # tabWord = stringToChars(word)
                # for c in stringToChars(low):
                #     word = ""

                actual+=1

            actual = 0
            
        col+=1
        


    return wordlist

banniere()

wordlist = generate([],low,up,start,limit,actual)


# print(wordlist)