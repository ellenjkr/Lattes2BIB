from xmlReader import XmlFile
import glob
import sys
from errno import EEXIST
import os
from os import makedirs,path
import re 

def mkdir_p(pathName): # Creates a directory (mkdir -p on cmd)
    try:
        makedirs(pathName)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(pathName):
            pass
        else:
        	raise

if __name__ == '__main__':
	filepath = 'Resumes' 
	for fileAddress in glob.glob(os.path.join(filepath, '*.xml')): # For each resume on the path
		inputDir = fileAddress # inputDir = Resumes/filename.xml

		fileName = re.findall(r'\\(.*).xml', fileAddress) # Resumes/fileName.xml -> fileName
		outputDir = f'Results/{fileName[0]}' # .bib you'll be saved on a folder that has the name of the resyne, on the folder "Results"
		mkdir_p(outputDir) # Creates the folder that has the name of the resume

		works = XmlFile(inputDir, outputDir) # Reads xml file
		works.getWorks() # Get the works from the xml file