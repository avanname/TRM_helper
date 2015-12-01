import pytraj
import pandas
import numpy as np
import matplotlib.pylab as plt
import scipy.stats
import datetime


#~~~~~~~~REPLACE PATHS HERE~~~~~~~#
outdatadir = '/Volumes/P4/workdir/ashley/TRM_output/'
filename = '12003.1.300_t00731225_run.bin'
animdir = '/Volumes/P4/workdir/ashley/Plots/ParticlePositions/Animate/Animate/' #directory to store images and create animation
tr = pytraj.Trm('rutgersNWA','rutgersNWA')

#~~~~~~~~~RUN INFORMATION~~~~~~~~~~~#
start_date = '01/10/03'
timesteps = 300 #Number of days of the run
partnum = 49 #Number of particles seeded


#=============PLOTTING==============#

#Combine directory and filename
referencefile = str(outdatadir + filename)

#Initiate pytraj
tr = pytraj.Trm('rutgersNWA','rutgersNWA')


#Load the file(s) that you want to look at
data = pandas.DataFrame(tr.readfile(referencefile))


#Adjust columns in the dataframe and sort
dataraw = data.loc[:,['ntrac','x','y']]
datasort = dataraw
datasort['index1'] = datasort.index
datasort = datasort.sort(['ntrac'])

#----optional-----#
#To plot a boundary
iroms = np.arange(0,721,1)  #i-coords
jroms = np.array([int(line.rstrip('\n')) for line in open('bigbounds.txt')]) #j-coords
#----------------#

ax = plt.gca()

for j in range(0,len(datasort)+1,partnum):
	datasort = datasort.sort_index()
	dataplot = datasort[0:j]
	dataplot = dataplot.sort_index()
	ax.plot(iroms,jroms, color='brown') #<--TURN OFF IF NOT PLOTTING A BOUNDARY
	dataplot = datasort.sort_index()
	dataplot = dataplot[0+j:49+j]
  	start = dataplot.head(1)
  	end = dataplot.tail(1)
  	ax.plot(dataplot['x'], dataplot['y'], '.', color='black', markersize=0.1,  alpha=1, linewidth=.2,zorder=1)
	dataplot = datasort
	date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")
  	end_date = str(date_1 + datetime.timedelta(days=(float(j)/float(49))))
	plt.title(str(end_date[0:10]) + " : Tracks of " + str(partnum) + ' particles')
	plt.savefig(animdir+str("%07d" % (j,))+'_'+'tracks.png')


# Final step to create animation
# Go to animdir and run the following bash command (requires ImageMagick):
# convert -set delay 5 -colors 50 -dispose 1 -loop 0 -scale 100% *.png movie.gif
