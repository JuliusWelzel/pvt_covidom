# PVT task
Python based PVT task for the Covidom project by [Julius Welzel](j.welzel@neurologie.uni-kiel.de).

## Project description
This repo contains all software to run the PVT task as done for the covidom project in Kiel, December 2020. It contains one training block of 8 trails and one experimental block of 5 minutes.<br>

## Installation guide
1. clone this repo to locally
2. install python via [anaconda distribution](https://www.anaconda.com/products/individual)
3. run anaconda prompt as admin
4. install modules via pip (psychopy, numpy, pylsl)

If you encounter this error in Windows: "error: command 'swig.exe' failed: No such file or directory", you should install pywinhook. This can be done in the anaconda shell by typing:
```
conda install -c conda-forge pywinhook
```
Then you can re-run the failed command.

## Run PVT
1. run pvt_standalone.bat
2. open anaconda prompt and run "python pvt.py" in local directory
3. enter participant id in Lab recorder and start recording
4. end recording

## Run PVT from single batch
1. run pvt_all.bat
2. enter participant id in Lab recorder and start recording
3. end recording

## Author
Developed by Julius Welzel, University of Kiel, (j.welzel@neurologie.uni-kiel.de) <br>

## Project structure
* 02_scripts *(experimental script to run pvt in python and first MatLab script for analysis results)*
* 03_data *(contains raw and prep data)*
* 101_software *(toolboxes and additional functions)*

## Versioning
*Version 1.1.1//15.06.2022* - Minor bug fix in installation related to pywinhook
