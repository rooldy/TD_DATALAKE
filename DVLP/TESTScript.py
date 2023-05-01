import os, fnmatch
from shutil import copy
#myPathHtml = "C:\\TD_DATALAKE\\DATALAKE\\0_SOURCE_WEB\\"
myPathHtml = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\0_SOURCE_WEB\\"
myPathSoc = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\GLASSDOOR\\SOC"
myPathAVISOC = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\GLASSDOOR\\AVI"
myPathEMP = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\LINKEDIN\\EMP"

#myPathHtml = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\0_SOURCE_WEB"
#myPathSoc = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\GLASSDOOR\\SOC"
#myPathAVISOC = "C:\TD_DATALAKE\TD_DATALAKE\DATALAKE\1_LANDING_ZONE\GLASSDOOR\\AVI"
#myPathEMP = "C:\\TD_DATALAKE\\TD_DATALAKE\\DATALAKE\\1_LANDING_ZONE\\LINKEDIN\\EMP"

myListOfFileTmp = os.listdir(myPathHtml)

for myFileName in myListOfFileTmp:
    
    if fnmatch.fnmatch(myFileName, "*INFO-SOC*.html"):
        copy(myPathHtml + myFileName, myPathSoc + myFileName)
        print(f"Copying {myFileName} to {myPathSoc}")
        
    elif fnmatch.fnmatch(myFileName, "*AVIS-SOC*.html"):
        copy(myPathHtml + myFileName, myPathAVISOC + myFileName)
        print(f"Copying {myFileName} to {myPathAVISOC}")
        
    elif fnmatch.fnmatch(myFileName, "*INFO-EMP*.html"):
        copy(myPathHtml + myFileName, myPathEMP + myFileName)
        print(f"Copying {myFileName} to {myPathEMP}")