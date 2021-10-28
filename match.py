#this is a python 3 implementation of a brute-force matching sort algorithm
def bfmatch(text, pattern):
    textlen = len(text)
    patlen = len(pattern)
    deltlen = textlen - patlen
    i = 0 # pattern iterator
    success = False

    while(i < deltlen):  
        j = 0
        #print the base text 
        for a in text:
            print(a, end="")
        print("")

        while(j < patlen and (pattern[j] == text[i + j])):  
            #produce spaces + display pattern[j]
            x = 0
            while (x < i + j):
                print(" ", end="")
                x += 1
            print(pattern[j])
            j += 1

        if(j == patlen): #if we reached the end of the pattern
            success = True
            return #might be redundant
        #print("i is", i)
        i += 1
    print(success) 
text = "There are woundrous things. There are magical things. There are dangerous things. We cake"
pattern  = "There are dangerous things."
bfmatch(text, pattern)
