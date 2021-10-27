#this is a python 3 implementation of a brute-force matching sort algorithm
def bfmatch(text, pattern):
    textlen = len(text)
    patlen = len(pattern)
    deltlen = textlen - patlen
    j = 0 # text iterator
    i = 0 # pattern iterator

    while(i < deltlen):  
        while(j < patlen and (pattern[j] == text[i + j])):  
        #while(j < patlen):  
            #print the base text 
            #for a in text:
            #    print(a, end="")
            #print("")
            #produce spaces + display pattern[j]
            #x = 0
            #while (x < j):
            #    print(" ", end="")
            #    x += 1
            print(pattern[j])
            #print("j is ", j)
            j += 1
        if(j == patlen): #if we reached the end of the pattern
            print("success") 
            return #might be redundant
        print("i is", i)
    i += 1

text = "There are woundrous things. There are magical things. There are dangerous things. We cake"
pattern  = "There are dangerous things."
bfmatch(text, pattern)
