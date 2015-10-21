#!/bin/bash

# This script can be used to change certain input parameters in a TRACMASS run.
# It will automatically edit the runfile based on your inputs below.

# You can add aditional variables -
# Contact Ashley Van Name (a.vanname@rutgers.edu) with any questions.

# ===================USER INPUT=====================#

# Directory with raw data files
IN_DIR=/Volumes/P3/ROMS/NWA/NWA-DK.HCob38R

#Directory where run should be stored
OUT_DIR=/Volumes/P4/workdir/ashley/TRM_output/

#Enter the name of the text file with YYYYMM on each line
textfile='yearmonth.txt'
startDay=16

# Number of particles, starting/ending
startpart=50000 
endpart=100000
interval=50000

#Number of days to release particles
dayrelease=1

#Number of days to track particles
#Number of timesteps
daytrack=50


#I-J Grid Coords
ist1=580 #237=site1
ist2=582 #237
jst1=183 #140
jst2=185 #140
#===================================================#

for part in $( seq $startpart $interval $endpart) ; do
       PartQuant=$part
	while read line; do
		year=${line:0:4}
		startYear=$year'/'
		startMon=${line:4:6}
		month=$startMon
		inDataDir=$IN_DIR/$year/
		if [[ ${startMon:0:1} -eq 0 ]]; then
		month=${month:1}
		month=$month
		fi
		done
       out_Data=TRM_$year
       outDataFile=$out_Data$month.$part.$daytrack
       caseName=$outDataFile
       intspin=$dayrelease
       intrun=$daytrack

# This edits the local runfile for each specified variable
cat rutgers_run.in|while read a ; do echo ${a//month/$startMon,} ; done > run.in.t
cat run.in.t|while read a ; do echo ${a//year/$startYear} ; done > run.in.t1
cat run.in.t1|while read a ; do echo ${a//indatadirectory/$inDataDir} ; done > run.in.t2
cat run.in.t2|while read a ; do echo ${a//outdatafilename/$outDataFile} ; done > run.in.t3
cat run.in.t3|while read a; do echo ${a//partpercell/$PartQuant} ; done > run.in.t4
cat run.in.t4|while read a; do echo ${a//dayrelease/$intspin} ; done > run.in.t5
cat run.in.t5|while read a; do echo ${a//lat1/$ist1} ; done > run.in.t6
cat run.in.t6|while read a; do echo ${a//lat2/$ist2} ; done > run.in.t7
cat run.in.t7|while read a; do echo ${a//lon1/$jst1} ; done > run.in.t8
cat run.in.t8|while read a; do echo ${a//lon2/$jst2} ; done > run.in.t9
cat run.in.t9|while read a; do echo ${a//daytotrack/$startDay,} ; done > run.in.t10
cat run.in.t10|while read a; do echo ${a//daytrack/$intrun}  ; done > rutgers_run_$month+$year.in        
#Copies final local runfile to project runfile
cp rutgers_run_$month+$year.in /Users/ashley/TRACMASS2/projects/rutgersNWA/rutgersNWA_run.in

#Run TRACMASS
./runtrm
done<$textfile

#Remove junk files
rm run.in.*
rm rutgers_run_*
