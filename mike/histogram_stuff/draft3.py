from matplotlib import pyplot as plt
from pylab import arange
import numpy as np
import sys

class HistogramStats(object):
    def __init__( self, numBins, minValue, maxValue ):
        self.numBins = numBins
        self.minValue = minValue
        self.maxValue = maxValue

        self.bins = [0 for i in range(0, numBins)]
        
        binWidth = (maxValue - minValue)/float(numBins)
        self.binStarts = []
        binStart = minValue
        for i in range(0, numBins): 
            self.binStarts.append( binStart )
            binStart += binWidth

    def update( self, value ):
        binIndex = int(self.numBins * ((value - self.minValue)/(self.maxValue - self.minValue)))
        if ( binIndex < 0 ):
            binIndex = 0
        if ( binIndex >= self.numBins):
            binIndex = self.numBins-1
        self.bins[binIndex] += 1
        

class StatsAccumulator(object):
    def __init__( self, name, histoBins, histoMin, histoMax ):
        self.name = name
        self.numLines = 0
        self.minValue = sys.float_info.max
        self.maxValue = sys.float_info.min
        self.totalValue = 0.0

        self.histo = HistogramStats( histoBins, histoMin, histoMax )

    def update( self, value ):
        self.numLines += 1
        self.maxValue = max( value, self.maxValue )
        self.minValue = min( value, self.minValue )
        self.totalValue += value

        self.histo.update( value )

    def report( self ):
        print "** %s **" % self.name
        print "  min", self.minValue
        print "  max", self.maxValue
        print "  mean", self.totalValue / float(self.numLines)
        print "  histo bins", self.histo.bins

        fig =  plt.figure()
        ax1 = fig.add_subplot(111)
        binIndices = arange(0, self.histo.numBins)
        plt.bar( binIndices, self.histo.bins )
        plt.xticks( binIndices, self.histo.binStarts, rotation = 'vertical' )
        plt.title('Distribution of Voltages')
        plt.xlabel('Voltage')
        plt.ylabel('Frequency')
        plt.show()
    
#datavalues = []


fileToProcess = sys.argv[1]
with open(fileToProcess) as f:
    calc1 = StatsAccumulator( "Voltage stats", 40, 219, 259)
    #calc2 = StatsAccumulator( "Real power - (rmsCurrent * rmsVoltage)")
    #calc3 = StatsAccumulator( "Real power - (rmsCurrent * 240)")
    #calc4 = StatsAccumulator( "Real power - (rmsPositiveCurrent * rmsVoltage) ")
    #calc5 = StatsAccumulator( "Real power - (rmsPositiveCurrent * 240) ")
    #calc6 = StatsAccumulator( "Real power - (rmsNegativeCurrent * rmsVoltage) ")
    #calc7 = StatsAccumulator( "Real power - (rmsNegativeCurrent * 240) ") 
    #calc8 = StatsAccumulator( "powerFactor" )

    for l in f:
        els = l.split(',')
        rmsVoltage = float(els[0])
        rmsCurrent = float(els[1])
        rmsPositiveCurrent = float(els[2])
        rmsNegativeCurrent = float(els[3])
        realPower = float(els[4])

        powerFactor = float(els[5])

        calc1.update(rmsVoltage)
        #calc2.update( realPower - (rmsCurrent*rmsVoltage) )
        #calc3.update( realPower - (rmsCurrent * 240) )
        #calc4.update( realPower - (rmsPositiveCurrent * rmsVoltage) )
        #calc5.update( realPower - (rmsPositiveCurrent * 240) )
        #calc6.update( realPower - (rmsNegativeCurrent * rmsVoltage) )
        #calc7.update( realPower - (rmsNegativeCurrent * 240) )
        #calc8.update( powerFactor )

    calc1.report()
    #calc2.report()
    #calc3.report()
    #calc4.report()
    #calc5.report()
    #calc6.report()
    #calc7.report()
    #calc8.report()
