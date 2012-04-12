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
wordcountlist.reverse()

newwordcountlist = []

for (word, count) in wordcountlist:
    newwordcountlist.append( (count, word) )

newwordcountlist.sort()
newwordcountlist.reverse()

print "First 10 words and counts: ", newwordcountlist[0:10]

opf = open(output_file, "w")
for (count, word) in newwordcountlist:
    opf.write("%d, %s\n" % (count, word))   

