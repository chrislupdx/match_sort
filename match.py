from random import randrange
#this is a python 3 implementation of a brute-force matching sort algorithm
def bfmatch(text, pattern):
    textlen = len(text)
    patlen = len(pattern)
    deltlen = textlen - patlen
    i = 0 # pattern iterator
    success = False
    while(i < deltlen):  
        j = 0
        for a in text:
            print(a, end="")
        print("")
        while(j < patlen and (pattern[j] == text[i + j])):
            x = 0
            while (x < i + j):
                print(" ", end="")
                x += 1
            print(pattern[j])
            j += 1
        if(j == patlen): #if we reached the end of the pattern
            success = True
            return
        i += 1
    print(success) 

def interface():
    print("Match Sort Algorithm, pick a size of your base string")
    text_size = int(input())
    rand_text = [text_size]
    
    for char in range(len(rand_text)):
        temp = randrange(128)
        temp_char = chr(temp)
        #rand_text.append(temp_char)a
        rand_text[char] = temp_char
    
    for a in rand_text:
        print(a)

    print("pign")
    #generate pattern of  the same type as 
    #generate an interface funciton
    #default_text = "There are woundrous things. There are magical things. There are dangerous things. We get what we deserve."
    #default_pattern  = "There are dangerous things."
    text = ""
    pattern = ""

    bfmatch(text, pattern)

    #how to design wall clock experimetns
        #upon execution start time
        #upon execution end, 
        #calculate the difference
    #wall_clock_data = []
    #display the wall clock experiment data

interface()
