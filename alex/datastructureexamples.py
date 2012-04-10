

# A list of integers
a = [4,5,1,2,8,6,3,6,7]
print "A list of integers:", a

print "Number of elements in the list:", len(a)

# The sorted list
a.sort()
print "The list sorted:", a

# The first element of the sorted list - the lowest number (we start counting from zero)
print "Lowest number:", a[0]
print "Second lowest number:", a[1]

print "Highest number:", a[-1]
print "Second highest number:", a[-2]


# A dictionary (here countries to their populations)
populations = { "Monaco" : 31987, "Gibraltar" : 27714, "Vatican city" : 900 }

print "The population of Monaco is:", populations["Monaco"]

print "Do we currently know the population of the UK:", "United kingdom" in populations

populations["United kingdom"] = 60587000

print "The population of the UK is:", populations["United kingdom"]

# Convert the dictionary to a list
popList = populations.items()

# Have a look at the first element of the list. This is two things separated by a comma
# called a 'tuple'. e.g. ('United kingdom', 60587000)
print "First element of the pop list:", popList[0]

print "Arbitrarily sorted populations:", popList

# Sort the populations alphabetically. When we sort lists with tuples, it sorts by the first
# element first (in this case the name)
popList.sort()
print "Populations sorted alphabetically by name:", popList

# And now we try sorting by size. To do this we want to re-make the list, also with tuple elements
# but this time with the size first, so when we sort we sort by size not name.
newList = []
for (name, size) in popList:
    newList.append( (size, name) )
    
newList.sort()
print "Populations sorted by size:", newList
