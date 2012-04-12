from sys import argv

script, cheese, goes, well, wine = argv

print "Your script is:", script
print "How was your meal?", cheese
cheese = raw_input("Was it good or bad?")
print "What did you get?", goes
goes = raw_input("Steak, eggs, cheese, what did you get?")
print "Did you eat desert?", well
well = raw_input("This is a yes or no question...")
wine = raw_input("Just do it.")
print "Say goodbye!", wine
