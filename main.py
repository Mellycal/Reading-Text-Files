# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#openfile = open(".\story.txt","r")
def readfile(filename):
     with open(".\story.txt","r") as openfile:
         read_file = openfile.read()
     return read_file    
    
def countwords():
    text = readfile(".\story.txt")
    split_text = text.split()
    #print(split_text)
    count ={}
    for e in split_text:
        if e in count:
            count[e] =+1
        else:
            count[e] =1 
    return count           

print (countwords())    