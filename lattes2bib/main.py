import glob
import os
import re 

from errno import EEXIST
from os import makedirs
from os import path
from xmlReader import XmlFile

def mkdir_p(pathName): # Creates a directory (mkdir -p on cmd)
	try:
		makedirs(pathName)
	except OSError as exc:
		if exc.errno == EEXIST and path.isdir(pathName):
			pass
		else:
			raise exc


if __name__ == '__main__':
	filepath = 'Resumes'

	for fileAddress in glob.glob(os.path.join(filepath, '*.xml')): # For each resume on the path
		inputDir = fileAddress # input directory = Resumes/filename.xml

		fileName = re.findall(r'\\(.*).xml', fileAddress) # Resumes/fileName.xml -> fileName
		outputDir = f'Results/{fileName[0]}' # .bib files will be saved to a folder that has the name of the resume, on the folder "Results"
		mkdir_p(outputDir) # Creates the folder that will hold the .bib files

		works = XmlFile(inputDir, outputDir) # Reads xml file
		works.getWorks() # Get the works from the xml file