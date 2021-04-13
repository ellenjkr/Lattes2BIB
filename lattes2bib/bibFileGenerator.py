from entryTypes import *
from utils import *

class BibFile():
	def __init__(self, bibType, publications, bibClass, outputDir):
		super(BibFile, self).__init__()
		self.type = bibType # Publication type (article, book, etc)
		self.publications = publications # List of publications
		self.bibType = bibClass # Publication type class

		self.publicationsInfo = self.getInfo() # Gets the info from each file
		self.bibFormat = self.formatBib() # Formats bib file

		self.outputDir = outputDir
		self.saveBib() # Saves the files


	def getAuthors(self, pub):
		authors = []
		for i in pub:
			if 'NOME-PARA-CITACAO' in i.attrib.keys(): # Finds the 'NOME-PARA-CITACAO' attribute 
				author = i.attrib['NOME-PARA-CITACAO'] 
				author = titleCase(author) # Name formatation
				authors.append(author) # Adds the author to the list of authors

		authorsStr = '' 
		for position, auth in enumerate(authors): # Generates a string with all the authors names
			if position == 0:
				authorsStr = authorsStr + auth
			else:
				authorsStr = authorsStr + ' and ' + auth

		return authorsStr


	def getInfo(self):
		publicationsInfo = [] # List of publications and its info (fields and cite key)
		
		for pos, pub in enumerate(self.publications):
			publicationInfo = {'Publication':[], 'Field':{'Tag':[], 'Info':[]}, 'CiteKey':{'Author':[], 'Year':[], 'TitleWord':[]}}
			publicationInfo['Publication'].append(pub) # Adiciona a publicação ao array

			authors = self.getAuthors(pub)
			publicationInfo['Field']['Tag'].append('author') # Adds the tag "author" 
			publicationInfo['Field']['Info'].append(authors) # Adds author info

			firstAuthLastName = authors.split(',') # Gets the last name of the first author
			firstAuthLastName = firstAuthLastName[0] 
			publicationInfo['CiteKey']['Author'].append(firstAuthLastName.replace(' ', '')) # Adds the last name of the first author to the cite key

			for tag in self.bibType.tags: # For each tag for this type of publication
				bibTag = tag[0]
				xmlKey = tag[1] # Gets the xml key for this tag
				xmlIndex = tag[2] # Gets the xml index for this tag

				if bibTag == 'year':
					publicationInfo['CiteKey']['Year'].append(pub[xmlIndex].attrib[xmlKey]) # Adds the year to the cite key
				elif bibTag == 'title': 
					title = pub[xmlIndex].attrib[xmlKey] # Access the title
					title = title.split(' ')

					for word in title:
						if checkException(word) == False: 
							# First word of the title that is not an exception (articles, prepositions, conjunctions) is added to the cite key
							word = word.replace(':', '') # Removes :
							word = word.replace(',', '') # Removes ,
							publicationInfo['CiteKey']['TitleWord'].append(word)
							break 

				if bibTag == 'pages':
					try:
						initPage = pub[xmlIndex[0]].attrib[xmlKey[0]]
						finalPage = pub[xmlIndex[1]].attrib[xmlKey[1]]
						pages = f'{initPage}-{finalPage}' # Merges initPage and finalPage
					except:
						pages = pub[xmlIndex].attrib[xmlKey] # If its the total number of pages instead of the initial and the final ones

					if pages[-1] == '-': pages = pages[:-1]
					publicationInfo['Field']['Tag'].append(bibTag) # Adds the tag pages
					publicationInfo['Field']['Info'].append(pages) # Adds the pages

				elif bibTag == 'journal' or bibTag == 'booktitle' or bibTag == 'title': # If it's one of these tags the title case will be applied to it
					attrib = pub[xmlIndex].attrib[xmlKey]
					attrib = titleCase(attrib)
					publicationInfo['Field']['Tag'].append(bibTag) # Adds the tag
					publicationInfo['Field']['Info'].append(attrib) # Adds the info 

				else: # In other cases
					attrib = pub[xmlIndex].attrib[xmlKey]
					publicationInfo['Field']['Tag'].append(bibTag) # Adds the tag
					publicationInfo['Field']['Info'].append(attrib) # Adds the info

			publicationsInfo.append(publicationInfo) # Adds the publicationInfo to a list of publicationsInfo (A list with all the publications and its info)

		return publicationsInfo

		
	def formatBib(self):
		bibFormat = ''
		for publicationInfo in self.publicationsInfo:
			citeKeyInfo = publicationInfo['CiteKey'] 
			'''
			cite key formatation: lastname0000word, 
			-> the last name of the first author
			-> publication year
			-> first word of the title that is not an exception
			'''
			self.citeKey = f"{citeKeyInfo['Author'][0].lower()}{citeKeyInfo['Year'][0].lower()}{citeKeyInfo['TitleWord'][0].lower()}" 
			bibFormat = bibFormat + '@' + self.type + '{' + self.citeKey + ',\n' # Example @article{lastname0000word

			for pos, tag in enumerate(publicationInfo['Field']['Tag']): # For each tag
				info = publicationInfo['Field']['Info'][pos] # Info that corresponds to the tag
				if pos == 0:
					bibFormat = bibFormat + '  ' + tag + ' = {' + info + '}' # If its the first tag it doesn't starts with a ',\n'

				elif info != '' and info != ' ' and info != '-': # If the information is not empty
					bibFormat = bibFormat + ',\n  ' + tag + ' = {' + info + '}' #Example:  year = {1993},

			bibFormat = bibFormat + '\n}\n\n' # Close the bibtex

		return bibFormat


	def saveBib(self): # Salva o arquivo
		with open(f'{self.outputDir}/{self.bibType.fileName}.bib', 'w', encoding='UTF-8') as bibfile:
			bibfile.write(self.bibFormat)