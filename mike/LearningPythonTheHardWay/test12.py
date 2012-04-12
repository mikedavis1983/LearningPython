height = float(raw_input("how tall are you in inches?"))
weight = float(raw_input("how much do you weigh in pounds?"))

cm = height * 2.54
kg = weight / 2.2

print "So, you're %r inches tall, and %r pounds in weight." % (height, weight)
print "Which is %r cm and %r kg." % (cm, kg)
