from entry_types_classes import *
from utils import *


class BibFile():
    def __init__(self, bib_type_class, publications, bib_class, outputDir, period):
        super(BibFile, self).__init__()
        self.type = bib_type_class  # Publication type (article, book, etc)
        self.publications = publications  # List of publications
        self.bib_type_class = bib_class  # Publication type class
        self.outputDir = outputDir
        self.period = period

        self.publications_info = self.get_publications_info()  # Gets the info from each publication
        self.bib_format = self.formatBib()  # Formats bib file


    def get_authors_list(self, pub):
        authors = []
        for i in pub:
            if 'NOME-PARA-CITACAO' in i.attrib.keys():  # Finds the 'NOME-PARA-CITACAO' attribute
                author = i.attrib['NOME-PARA-CITACAO']
                author = title_case(author)  # Name formatation
                # Adds the author to the list of authors
                authors.append(author)

        return authors

    def authors_to_string(self, authors):
        authorsStr = ''
        # Generates a string with all the authors names
        for position, auth in enumerate(authors):
            if position == 0:
                authorsStr = authorsStr + auth
            else:
                authorsStr = authorsStr + ' and ' + auth

        return authorsStr

    def add_basic_info(self, publication_info, pub):
        publication_info['Publication'].append(pub)  # Add publication to the array

        authors_list = self.get_authors_list(pub)
        authors = self.authors_to_string(authors_list) # Get authors

        publication_info['Field']['Tag'].append('author')  # Adds the tag "author"
        publication_info['Field']['Info'].append(authors)  # Adds author info

        # Gets the last name of the first author
        first_auth_last_name = authors_list[0].split(',')[0]
        publication_info['CiteKey']['Author'].append(first_auth_last_name.strip())

        return publication_info

    def get_title_word(self, title): # Get the title first word that is not an exception
        title = title.split(' ')
        word = title[0]

        for word in title:
            if check_exception(word) is False:
                # First word of the title that is not an exception (articles, prepositions, conjunctions) is added to the cite key
                word = word.replace(':', '')  # Removes :
                word = word.replace(',', '')  # Removes ,
                
                break

        return word

    def get_pages(self, pub, xml_index, xml_key):
        try:
            initPage = pub[xml_index[0]].attrib[xml_key[0]]
            finalPage = pub[xml_index[1]].attrib[xml_key[1]]
            # Merges initPage and finalPage
            pages = f'{initPage}-{finalPage}'
        except:
            # If its the total number of pages instead of the initial and the final ones
            pages = pub[xml_index].attrib[xml_key]

        if pages[-1] == '-':
            pages = pages[:-1]

        return pages

    def add_bibtype_info(self, publication_info, pub):
        for tag in self.bib_type_class.tags:  # For each tag for this type of publication
            bib_tag = tag[0]
            xml_key = tag[1]  # Gets the xml key for this tag
            xml_index = tag[2]  # Gets the xml index for this tag

            if bib_tag == 'year':
                publication_info['CiteKey']['Year'].append(pub[xml_index].attrib[xml_key])  # Adds the year to the cite key
            elif bib_tag == 'title':
                title = pub[xml_index].attrib[xml_key]  # Access the title
                word = self.get_title_word(title)
                publication_info['CiteKey']['TitleWord'].append(word)

            if bib_tag == 'pages':
                pages = self.get_pages(pub, xml_index, xml_key)
                publication_info['Field']['Tag'].append(bib_tag)  # Adds the tag pages
                publication_info['Field']['Info'].append(pages)  # Adds the pages

            # If it's one of these tags the title case will be applied to it
            elif bib_tag == 'journal' or bib_tag == 'booktitle' or bib_tag == 'title':
                attrib = pub[xml_index].attrib[xml_key]
                attrib = title_case(attrib)
                publication_info['Field']['Tag'].append(bib_tag)  # Adds the tag
                publication_info['Field']['Info'].append(attrib)  # Adds the info

            else:  # In other cases
                attrib = pub[xml_index].attrib[xml_key]
                publication_info['Field']['Tag'].append(bib_tag)  # Adds the tag
                publication_info['Field']['Info'].append(attrib)  # Adds the info

        return publication_info

    def get_publications_info(self):
        # List of publications and its info (fields and cite key)
        publications_info = []

        for pos, pub in enumerate(self.publications):
            publication_info = {'Publication': [], 'Field': {'Tag': [], 'Info': []}, 'CiteKey': {'Author': [], 'Year': [], 'TitleWord': []}}

            publication_info = self.add_basic_info(publication_info, pub)
            publication_info = self.add_bibtype_info(publication_info, pub) # Get info from each tag of the publication type
    
            if self.period != None:
                if str(publication_info['CiteKey']['Year'][0]) in ["2016", "2017", "2018", "2019", "2020", "2021"]:
                    # Adds the publication_info to a list of publications_info (A list with all the publications and its info)
                    publications_info.append(publication_info)
            else:
                # Adds the publication_info to a list of publications_info (A list with all the publications and its info)
                publications_info.append(publication_info)

        return publications_info

    def formatBib(self):
        bib_format = ''
        for publication_info in self.publications_info:
            citeKeyInfo = publication_info['CiteKey']
            '''
			cite key formatation: lastname0000word, 
			-> the last name of the first author
			-> publication year
			-> first word of the title that is not an exception
			'''
            self.citeKey = f"{citeKeyInfo['Author'][0].lower()}{citeKeyInfo['Year'][0].lower()}{citeKeyInfo['TitleWord'][0].lower()}"
            # Example @article{lastname0000word
            bib_format = bib_format + '@' + \
                self.type + '{' + self.citeKey + ',\n'

            # For each tag
            for pos, tag in enumerate(publication_info['Field']['Tag']):
                # Info that corresponds to the tag
                info = publication_info['Field']['Info'][pos]
                if pos == 0:
                    # If its the first tag it doesn't starts with a ',\n'
                    bib_format = bib_format + '  ' + tag + ' = {' + info + '}'

                elif info != '' and info != ' ' and info != '-':  # If the information is not empty
                    bib_format = bib_format + ',\n  ' + tag + \
                        ' = {' + info + '}'  # Example:  year = {1993},

            bib_format = bib_format + '\n}\n\n'  # Close the bibtex

        return bib_format

    def save_bib(self):  # Salva o arquivo
        with open(f'{self.outputDir}/{self.bib_type_class.fileName}.bib', 'w', encoding='UTF-8') as bibfile:
            bibfile.write(self.bib_format)
