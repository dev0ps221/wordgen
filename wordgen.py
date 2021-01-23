#!/usr/bin/python3.8
import time
from hashlib import md5
from os import system as cmd
import string
size = 4
low = string.ascii_lowercase
up = string.ascii_uppercase

def banniere():
	cmd("figlet Wordgen 0.01")

def clear():
	cmd('clear')

def rev(array):
	n = len(array)-1
	arr = []
	while n >= 0 :
		arr.append(array[n])
		n-=1
	return arr

def fill(word,cursor,set):
	if not hasattr(fill, "ran"):
		fill.ran = 0
	print(fill.ran)
	for letter in set:
		if (cursor+1) < len(word) and letter == set[0] and fill.ran !=0 :
			fill.ran+=1
			continue
		word[cursor] = letter
		if (cursor+1) < len(word):
			word = fill(word,cursor+1,set)
		clear()
		print(word)
		time.sleep(0.009)
	fill.ran+=1
	return word

def initialize(size,set):
	cursors = []
	word = []
	for n in range(size):
		word.append(set[0])
		cursors.append(n)
	return (cursors,word)

def generate(size,set):
	cursors,word = initialize(size,set)
	for cursor in rev(cursors):
		word = fill(word,cursor,set)

banniere()
generate(size,string.ascii_lowercase)




