from collections import defaultdict

# A string to split
exampleString = "Hit musical adaptation The Lion King has become the highest earning show in Broadway history, according to figures released by its producers Disney. The musical has earned $853.8 million (536.7 million pounds) since opening in 1997. Its closest rival, The Phantom of the Opera, has made $853.1m. Andrew Lloyd Webber's show has been running in New York since 1988."

# The string
print "Example string", exampleString


# The string split naively with unhelpful characters still present
naiveSplit = exampleString.split()
print "Naive split", naiveSplit

# The string with unhelpful chars removed
def isNotPunctuation(c):
    return c not in "$()',"
    
filteredString = filter( isNotPunctuation, exampleString )
print "Filtered string", filteredString

allLowerCase = filteredString.lower()
print "Lower case", allLowerCase


betterSplit = allLowerCase.split()
print "Better split", betterSplit


wordCount = defaultdict( lambda : 0 )
for word in betterSplit:
    oldCount = wordCount[word]
    wordCount[word] = oldCount + 1
    
print "Nicely formatted words:"
for (word, count) in wordCount.items():
	print "  ", word, count
    
