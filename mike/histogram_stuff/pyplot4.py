import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

csvreader = csv.reader(open('data.csv', 'rb'), delimiter = ',')
for row in csvreader:
    for column in row:
        print column
