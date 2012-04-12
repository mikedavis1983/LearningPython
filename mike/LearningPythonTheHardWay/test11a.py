inch = float(raw_input("Please type how tall you are in inches."))
pound = float(raw_input("Please type how fat you are in pounds."))

cm = inch * 2.54
kg = pound / 2.2

print "You are %d kg fat and %d cm tall!" % (kg, cm)
