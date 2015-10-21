# TRM_helper
TRM_helper is a set of codes that can help to more easily run TRM.

The following is a very basic overview on how to run TRM.

First, make sure you have all of the requirements (TRACMASS/requirements.txt)

You will deal mostly with these three things in the TRACMASS directory
- Makefile_tmpl
- projects directory
- dataloop.bash

MAKEFILE_TMPL
- change your project and case name (usually these are the same)
- make sure runfile == runtrm
- change your compiler & netcdflibs
Run the make

PROJECTS DIRECTORY
This stores codes for various grids. They should coincide with the project and casename in makefile_tmpl
- Makefile.prj :: this is a way to change general settings for your run (e.g. type of output)
- projectname_run.in :: leave this alone, the dataloop.bash file in the TRACMASS directory will allow you to edit this
- projectname_grid.in :: allows you to edit grid information, but should be already (mostly) correct based on project

DATALOOP.BASH
This is a script that allows you to enter information about each run of TRACMASS that you want to complete
--This script will edit the file casename2_run.in in the trm directory and then copy it over to the projects directory for the run (avoids damaging the raw code).
- Change the details under the user input section
- textfile == this allows you to specify multiple months/years that you would like to run. For example, if you type:
199807
199907
200007
With a startDay = 01 and daytrack=31, then TRM will run for the entire month of July in each of these years.

-IJ Cooridnates are used to specify where you would like to seed passive tracers. The default setting is to seed each cell with the same number of particles (particle number specified by startpart/endpart). You can change this setting in the casename2_run.in file

- CHANGE: The path to your casename_run.in file in the projects directory at line 74 (the cp command).
- You can also change the name of the out data file by editing the out_Data and out_Datafile variables 




