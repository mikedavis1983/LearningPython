def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes_of_crackers." % boxes_of_crackers
    print "Man, thats enough for a party!"
    print "Get a blanket.\n"

print "we can just give the functin numbers directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_crackers = 50
amount_of_cheese = 10

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do maths inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 
