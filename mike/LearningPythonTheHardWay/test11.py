print "how tall are you in inches?",
height = float(raw_input())
print "how much do you weigh in pounds?",
weight = float(raw_input())

cm = height * 2.54
kg = weight / 2.2

print "So, you're %r inches tall, and %r pounds in weight." % (height, weight)
print "Which is %r cm and %r kg." % (cm, kg)
