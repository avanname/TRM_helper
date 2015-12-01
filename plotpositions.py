# This is a Python script that takes in binary output from TRACMASS,
# reads it, and plots the particle positions at the end of the run.

import pytraj
import pandas
import numpy as np
import matplotlib.pylab as plt
import scipy.stats
import subprocess


#~~~~~~~~REPLACE FILENAME HERE~~~~~~~#
outdatadir = '/Volumes/P4/workdir/ashley/TRM_output/'
filename = 'testcells_19598.100000.50_t00715372_run.bin'

#(CASENAME, PROJECTNAME) :: Initiates pytraj
tr = pytraj.Trm('rutgersNWA','rutgersNWA')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
referencefile = str(outdatadir + filename)

#Load the file(s) 
data1 = pandas.DataFrame(tr.readfile(referencefile))

#Adjust columns in the dataframes
data1 = data1.loc[:,['ntrac','x','y']]
data1 = data1.drop_duplicates(cols=['ntrac'], take_last=True)

#Change data into int
data1 = data1.astype(int)

#Group by size
group1 = data1.groupby(['x','y']).size()

#Reset Indicies
group1reset = group1.reset_index()
group1reset.columns = ['x','y','part']

print group1reset

#Pivot chart
group1pivot = group1reset.pivot('x','y')
Z1 = group1pivot.values
nans = np.isnan(Z1)
Z1[nans] = 0

#-------plotting------#

#Creats hexbin plot of ending particle positions
group1reset.plot(kind='hexbin', x='x', y='y', C='part',cmap='winter', gridsize=100)
plt.title('Ending Particle Positions') 
plt.savefig('Endingpartpos.png')

#----------------------#

