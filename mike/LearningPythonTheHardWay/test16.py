from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating file. Goodbye!"
target.truncate()

print "now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to wite these to the file."


target.write(line1 + "\n" + line2 + "\n" + line2 + "\n")

print "And finally, we close it."
target.close()
