from matplotlib import pyplot as plt
import numpy as np

#with open('gpc_alldata.csv') as f:
#    v = np.loadtxt(f, delimiter = ',', dtype = 'float', comments = '#', skiprows = 1, usecols = [3])
#v_hist = np.ravel(v)

dataValues = []
with open( 'gpc_alldata.csv' ) as f:
    for l in f.readlines()[1:]:
        try:
            items = l.split(',')
            dataValues.append( float(items[3].strip()) )
        except ValueError:
            print "Invalid line:", l


fig =  plt.figure()
ax1 = fig.add_subplot(111)
n, bins, patches = ax1.hist(dataValues, bins = 40, normed = 0, facecolor = 'green')
plt.title('distribution of cabinet office expenditure')
plt.xlabel('expenditure in pounds')
plt.ylabel('frequency')
plt.show()
