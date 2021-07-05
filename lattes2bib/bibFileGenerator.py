from entryTypes import *
from utils import *


class BibFile():
    def __init__(self, bibType, publications, bibClass, outputDir):
        super(BibFile, self).__init__()
        self.type = bibType  # Publication type (article, book, etc)
        self.publications = publications  # List of publications
        self.bibType = bibClass  # Publication type class

        self.publicationsInfo = self.getInfo()  # Gets the info from each publication
        self.bibFormat = self.formatBib()  # Formats bib file

        self.outputDir = outputDir

    def getAuthors(self, pub):
        authors = []
        for i in pub:
            if 'NOME-PARA-CITACAO' in i.attrib.keys():  # Finds the 'NOME-PARA-CITACAO' attribute
                author = i.attrib['NOME-PARA-CITACAO']
                author = titleCase(author)  # Name formatation
                # Adds the author to the list of authors
                authors.append(author)

        authorsStr = ''
        # Generates a string with all the authors names
        for position, auth in enumerate(authors):
            if position == 0:
                authorsStr = authorsStr + auth
            else:
                authorsStr = authorsStr + ' and ' + auth

        return authorsStr

    def getInfo(self):
        # List of publications and its info (fields and cite key)
        publicationsInfo = []

        for pos, pub in enumerate(self.publications):
            publicationInfo = {'Publication': [], 'Field': {
                'Tag': [], 'Info': []}, 'CiteKey': {'Author': [], 'Year': [], 'TitleWord': []}}
            publicationInfo['Publication'].append(
                pub)  # Adiciona a publicação ao array

            authors = self.getAuthors(pub)
            publicationInfo['Field']['Tag'].append(
                'author')  # Adds the tag "author"
            publicationInfo['Field']['Info'].append(
                authors)  # Adds author info

            # Gets the last name of the first author
            firstAuthLastName = authors.split(',')
            firstAuthLastName = firstAuthLastName[0]
            publicationInfo['CiteKey']['Author'].append(firstAuthLastName.replace(
                ' ', ''))  # Adds the last name of the first author to the cite key

            for tag in self.bibType.tags:  # For each tag for this type of publication
                bibTag = tag[0]
                xmlKey = tag[1]  # Gets the xml key for this tag
                xmlIndex = tag[2]  # Gets the xml index for this tag

                if bibTag == 'year':
                    publicationInfo['CiteKey']['Year'].append(
                        pub[xmlIndex].attrib[xmlKey])  # Adds the year to the cite key
                elif bibTag == 'title':
                    title = pub[xmlIndex].attrib[xmlKey]  # Access the title
                    title = title.split(' ')

                    for word in title:
                        if checkException(word) == False:
                            # First word of the title that is not an exception (articles, prepositions, conjunctions) is added to the cite key
                            word = word.replace(':', '')  # Removes :
                            word = word.replace(',', '')  # Removes ,
                            publicationInfo['CiteKey']['TitleWord'].append(
                                word)
                            break

                if bibTag == 'pages':
                    try:
                        initPage = pub[xmlIndex[0]].attrib[xmlKey[0]]
                        finalPage = pub[xmlIndex[1]].attrib[xmlKey[1]]
                        # Merges initPage and finalPage
                        pages = f'{initPage}-{finalPage}'
                    except:
                        # If its the total number of pages instead of the initial and the final ones
                        pages = pub[xmlIndex].attrib[xmlKey]

                    if pages[-1] == '-':
                        pages = pages[:-1]
                    publicationInfo['Field']['Tag'].append(
                        bibTag)  # Adds the tag pages
                    publicationInfo['Field']['Info'].append(
                        pages)  # Adds the pages

                # If it's one of these tags the title case will be applied to it
                elif bibTag == 'journal' or bibTag == 'booktitle' or bibTag == 'title':
                    attrib = pub[xmlIndex].attrib[xmlKey]
                    attrib = titleCase(attrib)
                    publicationInfo['Field']['Tag'].append(
                        bibTag)  # Adds the tag
                    publicationInfo['Field']['Info'].append(
                        attrib)  # Adds the info

                else:  # In other cases
                    attrib = pub[xmlIndex].attrib[xmlKey]
                    publicationInfo['Field']['Tag'].append(
                        bibTag)  # Adds the tag
                    publicationInfo['Field']['Info'].append(
                        attrib)  # Adds the info

            # if str(publicationInfo['CiteKey']['Year'][0]) in ["2016", "2017", "2018", "2019", "2020", "2021"]: // Filter period
                # Adds the publicationInfo to a list of publicationsInfo (A list with all the publications and its info)
            publicationsInfo.append(publicationInfo)

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
            # Example @article{lastname0000word
            bibFormat = bibFormat + '@' + \
                self.type + '{' + self.citeKey + ',\n'

            # For each tag
            for pos, tag in enumerate(publicationInfo['Field']['Tag']):
                # Info that corresponds to the tag
                info = publicationInfo['Field']['Info'][pos]
                if pos == 0:
                    # If its the first tag it doesn't starts with a ',\n'
                    bibFormat = bibFormat + '  ' + tag + ' = {' + info + '}'

                elif info != '' and info != ' ' and info != '-':  # If the information is not empty
                    bibFormat = bibFormat + ',\n  ' + tag + \
                        ' = {' + info + '}'  # Example:  year = {1993},

            bibFormat = bibFormat + '\n}\n\n'  # Close the bibtex

        return bibFormat

    def save_bib(self):  # Salva o arquivo
        with open(f'{self.outputDir}/{self.bibType.fileName}.bib', 'w', encoding='UTF-8') as bibfile:
            bibfile.write(self.bibFormat)
