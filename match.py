#this is a python 3 implementation of a brute-force matching sort algorithm
def bfmatch(text, pattern):
    #for textword in text:
    #    for patword in pattern:
    #        if textword == patword: 
    i = 0
    textlen = len(text)
    j = 0
    patlen = len(pattern)

    deltlen = textlen - patlen
    while(i < deltlen): 
        while(j < patlen and pattern[j] == text[i + j]):
            for a in text:
                print(a, end="")
            print("")
            x = 0
            while (x < j):
                print(" ", end="")
                x += 1
            #if we did not find a matching char we should reset the pattern search for this character/ratchet forward or somethign
            print(pattern[j])
            
            j += 1
            if(j == patlen):
                print("success") 
                return #might be redundant
            else:  #that doesnt work right
                print("fail")
                return  
    #    i += 1
    #print("fail")
    #return
            #if(pattern[j] == text[i + j]
            #if(text[i] == pattern[j]): #if these letters match
            #    print(text[i]) 
            #    j += 1
            #else:
            #    print(text[i])
            #    break
            #i += 1 #increment
        #how do we detect complltion
        #for each character 
            #iterate through the pattern
                #if the current character matches the current pattern character 
                    #continue advancing through the pattern
                #else we should move to the next character in the text
text = "There are woundrous things. There are magical things. There are dangerous things. We cake"
pattern  = "There are dangerous things."
#text = "N O B O D Y _ N O T I C E D _ H I M"
#pattern = "N O T"
bfmatch(text, pattern)
#@ each iteration, print out like its progress
