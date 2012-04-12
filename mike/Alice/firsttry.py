from sys import argv
from collections import defaultdict

script, input_file, output_file = argv

def isnotpunctutation(c):
    return c not in "$()',.!?-;:_*[]\""

testtext = open(input_file,"r").read()

filteredstring = filter(isnotpunctutation, testtext)

naiveSplit = filteredstring.lower().split()

wordcount = defaultdict(lambda : 0)
for word in naiveSplit:
    oldcount = wordcount[word]
    wordcount[word] = oldcount + 1

wordcountlist = wordcount.items()
wordcountlist.sort()

opf = open(output_file, "w")
for (word, count) in wordcountlist:
    opf.write("%s, %d\n" % (word, count))   


#    print " ", word, count

#opf = open(output_file, "w")
#for word in naivesplit():
#    opf.write(word + "\n")




