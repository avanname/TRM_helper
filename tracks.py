import pytraj
import pandas
import numpy as np
import matplotlib.pylab as plt
import scipy.stats
import subprocess

tr = pytraj.Trm('rutgersNWA','rutgersNWA')

#~~~~~~~~REPLACE FILENAME HERE~~~~~~~#
outdatadir = '/Volumes/P4/workdir/ashley/TRM_output/'
filename = '12003.100.250_t00731225_run.bin'

#~~~~~~~~~~~Run info ~~~~~~~~~~~~~~~~#
timesteps = 250
parts_seeded = 4900
outputdir = '/Volumes/P4/workdir/ashley/Plots/ParticlePositions/'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Initiate pytraj
tr = pytraj.Trm('rutgersNWA','rutgersNWA')
referencefile = str(outdatadir + filename)

#Load the file(s) that you want to look at
data = pandas.DataFrame(tr.readfile(referencefile))

#Adjust columns in the dataframe
dataraw = data.loc[:,['ntrac','x','y']]


ax = plt.gca()
datasort = dataraw.sort(['ntrac'])

#-----optional: plots boundary------#
iroms = np.arange(0,721,1)
jroms = np.array([int(line.rstrip('\n')) for line in open('bigbounds.txt')])
#-----------------------------------#

for j in range(timesteps,len(datasort)+1,timesteps):
      slicer = j-timesteps
      dataplot = datasort[slicer:j]
	    print dataplot
	    dataplot = dataplot.sort_index()
	    print dataplot
	    start = dataplot.head(1)
	    end = dataplot.tail(1)
	    ax.plot(dataplot['x'], dataplot['y'], '-', color='grey', alpha=0.3, linewidth=.2,zorder=1)
	    ax.plot(start['x'], start['y'], '.', color='r',zorder=2)
	    ax.plot(end['x'], end['y'], '.', color='g',zorder=3)
	    ax.plot(iroms,jroms) # <-- TURN OFF IF NOT PLOTTING BOUNDARY
plt.savefig(str(outputdir) + str(filename) + 'tracks.png')



