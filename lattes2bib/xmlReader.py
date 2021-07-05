import xml.etree.ElementTree as ET
from bibFileGenerator import *

class Resume():
	def __init__(self, fileName, outputDir):
		super(Resume, self).__init__()
		self.outputDir = outputDir
		self.bib_files = []

		self.mytree = ET.parse(fileName)
		self.myroot = self.mytree.getroot()

		# Each type of work has its entry type and its fields (tags)
		# xml tag: [bib signature, class with the tags]
		self.entryTypes = {'TRABALHOS-EM-EVENTOS': ['inproceedings', Event()], 
						   'ARTIGOS-PUBLICADOS': ['article', Article()], 
						   'LIVROS-PUBLICADOS-OU-ORGANIZADOS': Book(), 
						   'CAPITULOS-DE-LIVROS-PUBLICADOS': Chapter(), 
		 				   'TEXTOS-EM-JORNAIS-OU-REVISTAS': ['article', Text()], 
		 				   'DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA': ['article', Other()]} 


	def get_bib_files(self): # Generates the bib files
		for category in self.myroot[1]: # -> Produção Bibliográfica
			if category.tag == 'LIVROS-E-CAPITULOS':
				for i in category: # Separates books from chapters
					if i.tag == 'LIVROS-PUBLICADOS-OU-ORGANIZADOS': 
						books = i
						bib = BibFile('book', books, self.entryTypes[i.tag], self.outputDir)
						self.bib_files.append(bib)
					else:
						chapters = i
						bib = BibFile('inbook', chapters, self.entryTypes[i.tag], self.outputDir)
						self.bib_files.append(bib)
			else:
				if category.tag in self.entryTypes.keys():
					pub = category # List of publications of a category
					pubType = self.entryTypes[category.tag] # Get the data of the category (its bib signature and its fields (tags))
					bib = BibFile(pubType[0], pub, pubType[1], self.outputDir) # Entry type, publications, fields, output directory
					self.bib_files.append(bib)
				else:
					print('Categoria não inclusa na implementação: ', category.tag)

		return self.bib_files

	def save_bib_files(self, bib_files):
		for bib in bib_files:
			bib.save_bib()

# ====================================================================
'''
conferences = []
cont = 0
for i in self.myroot[2]:
	if i.tag == 'DEMAIS-TIPOS-DE-PRODUCAO-TECNICA':
		for j in i:
			if j.tag == 'APRESENTACAO-DE-TRABALHO':
				conferences.append(i[cont])
				cont += 1

bib = BibFile('conference', 'apresentacao', conferences, Conference())
'''

# ====================================================================
