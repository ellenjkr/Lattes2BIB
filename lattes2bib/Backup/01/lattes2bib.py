import xml.etree.ElementTree as ET

def getAuthors(pub):
	authors = []
	for i in pub:
		if 'NOME-PARA-CITACAO' in i.attrib.keys():
			authors.append(i.attrib['NOME-PARA-CITACAO'])
	authorsStr = ''
	for position, auth in enumerate(authors):
		if position == 0:
			authorsStr = authorsStr + auth
		else:
			authorsStr = authorsStr + ' and ' + auth

	return authorsStr


mytree = ET.parse('curriculo.xml')
myroot = mytree.getroot()

bibFormat = """
  author  = {}, 
  title   = {},
  journal = {},
  year    = {},
  pages   = {},
  volume  = {}
"""
bibFormat2 = """
  author    = {}, 
  title     = {},
  edition   = {},
  address   = {},
  publisher = {}, 
  year      = {},
  volume    = {}, 
  series    = {},
  pages     = {},
  isbn      = {}
"""

bibFormat3 = """
  author    = {}, 
  organization = {},
  title     = {},
  booktitle = {},
  address   = {},
  publisher = {}, 
  year      = {},
  volume    = {},
  edition   = {},
  pages     = {},
  isbn      = {}
"""

bibFormat4 = """
  author   = {},
  title    = {},
  journal  = {},
  address = {},
  volume   = {},
  pages    = {},
  year     = {}
"""

bibFormat5 = """
  author            = {},
  title             = {},
  booktitle         = {},
  address           = {},
  note              = {},
  publisher         = {},
  year              = {},
  volume            = {},
  pages             = {}
"""

bibFormat6 = """
  author = {},
  title  = {},
  year   = {},
  booktitle  = {}
"""

bibFormat7 = """
  author = {},
  title = {},
  pubCity = {},
  publisher = {},
  year = {},
  pages = {}
"""

# =============================================================================
# Artigos completos publicados em periódicos

# artigos = myroot[1][1]
# bibtex = ''

# for pos, artigo in enumerate(artigos):
# 	authorsStr = getAuthors(artigo)
# 	title = artigo[0].attrib['TITULO-DO-ARTIGO']
# 	journal = artigo[1].attrib['TITULO-DO-PERIODICO-OU-REVISTA']
# 	year = artigo[0].attrib['ANO-DO-ARTIGO']
# 	initPage = artigo[1].attrib['PAGINA-INICIAL']
# 	finalPage = artigo[1].attrib['PAGINA-FINAL']
# 	pages = f'{initPage}-{finalPage}'
# 	volume = artigo[1].attrib['VOLUME']
# 	doi = artigo[0].attrib['DOI']

# 	if doi != '':
# 		final = bibFormat.format('{' + authorsStr + '}', '{' + title + '}', '{' + journal + '}', 
# 					'{' + year + '}', '{' + pages + '}', '{' + volume + '},')
# 		final = final + '  doi = {' + doi + '}' + '\n}\n\n'
# 	else:
# 		final = bibFormat.format('{' + authorsStr + '}', '{' + title + '}', '{' + journal + '}', 
# 			'{' + year + '}', '{' + pages + '}', '{' + volume + '}' + '\n}\n\n')

# 	bibtex = bibtex + """@article{article,""" + final

# with open(f'Resultados/artigos.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)


# =============================================================================
#Livros publicados/organizados ou edições

# livros = myroot[1][2][0]
# bibtex = ''

# for pos, livro in enumerate(livros):
# 	authorsStr = getAuthors(livro)
# 	title = livro[0].attrib['TITULO-DO-LIVRO']
# 	edition = livro[1].attrib['NUMERO-DA-EDICAO-REVISAO']
# 	address = livro[1].attrib['CIDADE-DA-EDITORA']
# 	publisher = livro[1].attrib['NOME-DA-EDITORA']
# 	year = livro[0].attrib['ANO']
# 	volume = livro[1].attrib['NUMERO-DE-VOLUMES']
# 	series = livro[1].attrib['NUMERO-DA-SERIE']
# 	pages = livro[1].attrib['NUMERO-DE-PAGINAS']
# 	isbn = livro[1].attrib['ISBN']
# 	doi = livro[0].attrib['DOI']

# 	if doi != '':
# 		final = bibFormat2.format('{' + authorsStr + '}', '{' + title + '}', '{' + edition + '}', 
# 			'{' + address + '}', '{' + publisher + '}', '{' + year + '}', '{' + volume + '}', 
# 			'{' + series + '}', '{' + pages + '}', '{' + isbn + '},')
# 		final = final + '  doi = {' + doi + '}' + '\n}\n\n'

# 	else:
# 		final = bibFormat2.format('{' + authorsStr + '}', '{' + title + '}', '{' + edition + '}', 
# 			'{' + address + '}', '{' + publisher + '}', '{' + year + '}', '{' + volume + '}', 
# 			'{' + series + '}', '{' + pages + '}', '{' + isbn + '}' + '\n}\n\n')

# 	bibtex = bibtex + """@book{book,""" + final

# with open(f'Resultados/livros.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)

# =============================================================================
# Capítulos de livros publicados

# capitulos = myroot[1][2][1]
# bibtex = ''

# for pos, capitulo in enumerate(capitulos):
# 	authorsStr = getAuthors(capitulo)
# 	organization = capitulo[1].attrib['ORGANIZADORES']
# 	title = capitulo[0].attrib['TITULO-DO-CAPITULO-DO-LIVRO']
# 	booktitle = capitulo[1].attrib['TITULO-DO-LIVRO']
# 	address = capitulo[1].attrib['CIDADE-DA-EDITORA']
# 	publisher = capitulo[1].attrib['NOME-DA-EDITORA']
# 	year = capitulo[0].attrib['ANO']
# 	volume = capitulo[1].attrib['NUMERO-DE-VOLUMES']
# 	edition = capitulo[1].attrib['NUMERO-DA-EDICAO-REVISAO']
# 	initPage = capitulo[1].attrib['PAGINA-INICIAL']
# 	finalPage = capitulo[1].attrib['PAGINA-FINAL']
# 	pages = f'{initPage}-{finalPage}'
# 	isbn = capitulo[1].attrib['ISBN']
# 	doi = capitulo[0].attrib['DOI']

# 	if doi != '':
# 		final = bibFormat3.format('{' + authorsStr + '}', '{' + organization + '}', '{' + title + '}', 
# 			'{' + booktitle + '}', '{' + address + '}', '{' + publisher + '}', '{' + year + '}', 
# 			'{' + volume + '}', '{' + edition + '}', '{' + pages + '}', '{' + isbn + '},')
# 		final = final + '  doi = {' + doi + '}' + '\n}\n\n'
# 	else: 
# 		final = bibFormat3.format('{' + authorsStr + '}', '{' + organization + '}', '{' + title + '}', 
# 			'{' + booktitle + '}', '{' + address + '}', '{' + publisher + '}', '{' + year + '}', 
# 			'{' + volume + '}', '{' + edition + '}', '{' + pages + '}', '{' + isbn + '}' + '\n}\n\n')

# 	bibtex = bibtex + """@inbook{inbook,""" + final

# with open(f'Resultados/capitulos.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)


# =============================================================================
# Textos em jornais de notícias/revistas

# textos = myroot[1][3]
# bibtex = ''

# for pos, texto in enumerate(textos):
# 	authorsStr = getAuthors(texto)
# 	title = texto[0].attrib['TITULO-DO-TEXTO']
# 	journal = texto[1].attrib['TITULO-DO-JORNAL-OU-REVISTA']
# 	address = texto[1].attrib['LOCAL-DE-PUBLICACAO']
# 	volume = texto[1].attrib['VOLUME']
# 	initPage = texto[1].attrib['PAGINA-INICIAL']
# 	finalPage = texto[1].attrib['PAGINA-FINAL']
# 	pages = f'{initPage}-{finalPage}'
# 	year = texto[0].attrib['ANO-DO-TEXTO']
# 	doi = texto[0].attrib['DOI']

# 	if doi != '':
# 		final = bibFormat4.format('{' + authorsStr + '}', '{' + title + '}', '{' + journal + '}', 
# 					'{' + address + '}', '{' + volume + '}', '{' + pages + '}', '{' + year + '},')
# 		final = final + '  doi = {' + doi + '}' + '\n}\n\n'
# 	else:
# 		final = bibFormat4.format('{' + authorsStr + '}', '{' + title + '}', '{' + journal + '}', 
# 			'{' + address + '}', '{' + volume + '}', '{' + pages + '}', '{' + year + '}' + '\n}\n\n')

# 	bibtex = bibtex + """@article{text,""" + final

# with open(f'Resultados/textos.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)


# =============================================================================
# Trabalhos completos publicados em anais de congressos 97
# + Resumos expandidos publicados em anais de congressos 3
# + Resumos publicados em anais de congressos 23

# pubAnais = myroot[1][0]
# bibtex = ''
# for pos, pub in enumerate(pubAnais):
# 	authorsStr = getAuthors(pub)
# 	title = pub[0].attrib['TITULO-DO-TRABALHO']
# 	booktitle = pub[1].attrib['NOME-DO-EVENTO']
# 	address = pub[1].attrib['CIDADE-DO-EVENTO']
# 	anais_proceedings = pub[1].attrib['TITULO-DOS-ANAIS-OU-PROCEEDINGS']
# 	publisher = pub[1].attrib['NOME-DA-EDITORA']
# 	year = pub[0].attrib['ANO-DO-TRABALHO']
# 	volume = pub[1].attrib['VOLUME']
# 	initPage = pub[1].attrib['PAGINA-INICIAL']
# 	finalPage = pub[1].attrib['PAGINA-FINAL']
# 	pages = f'{initPage}-{finalPage}'
# 	doi = pub[0].attrib['DOI']

# 	if doi != '':
# 		final = bibFormat5.format('{' + authorsStr + '}', '{' + title + '}', '{' + booktitle + '}', 
# 			'{' + address + '}', '{' + anais_proceedings + '}', '{' + publisher + '}', 
# 			'{' + year + '}', '{' + volume + '}', '{' + pages + '},')

# 		final = final + '  doi = {' + doi + '}' + '\n}\n\n'

# 	else:
# 		final = bibFormat5.format('{' + authorsStr + '}', '{' + title + '}', '{' + booktitle + '}', 
# 			'{' + address + '}', '{' + anais_proceedings + '}', '{' + publisher + '}', 
# 			'{' + year + '}', '{' + volume + '}', '{' + pages + '}' + '\n}\n\n')

# 	bibtex = bibtex + """@inproceedings{pubAnais,""" + final
	
# with open(f'Resultados/anais_de_congressos.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)


# =============================================================================
# Apresentações de Trabalho

# apresentacoes = []
# bibtex = ''

# for i in myroot[2]:
# 	if i.tag == 'DEMAIS-TIPOS-DE-PRODUCAO-TECNICA':
# 		for j in i:
# 			if j.tag == 'APRESENTACAO-DE-TRABALHO':
# 				apresentacoes.append(i)


# for pos, apresentacao in enumerate(apresentacoes):
# 	apresentacao = apresentacao[pos]
# 	authorsStr = getAuthors(apresentacao)
# 	title = apresentacao[0].attrib['TITULO']
# 	year = apresentacao[0].attrib['ANO']
# 	booktitle = apresentacao[1].attrib['NOME-DO-EVENTO']

# 	final = bibFormat6.format('{' + authorsStr + '}', '{' + title + '}', '{' + year + '}', '{' + booktitle + '}')

# 	bibtex = bibtex + """@conference{apresentacao,""" + final + '}\n\n'

# with open(f'Resultados/apresentações.bib', 'w', encoding='UTF-8') as bibfile:
# 	bibfile.write(bibtex)

# =============================================================================
# Outras Produções Bibliográficas

producoes = myroot[1][4]
bibtex = ''

for pos, producao in enumerate(producoes):
	authorsStr = getAuthors(producao)
	title = producao[0].attrib['TITULO']
	pubCity = producao[1].attrib['CIDADE-DA-EDITORA']
	publisher = producao[1].attrib['EDITORA']
	year = producao[0].attrib['ANO']
	pages = producao[1].attrib['NUMERO-DE-PAGINAS']
	doi = producao[0].attrib['DOI']

	if doi != '':
		final = bibFormat7.format('{' + authorsStr + '}', '{' + title + '}',  '{' + pubCity + '}', 
			'{' + publisher + '}', '{' + year + '}', '{' + pages + '},')
		final = final + '  doi = {' + doi + '}' + '\n}\n\n'

	else:
		final = bibFormat7.format('{' + authorsStr + '}', '{' + title + '}',  '{' + pubCity + '}', 
			'{' + publisher + '}', '{' + year + '}', '{' + pages + '}'+ '\n}\n\n')

	bibtex = bibtex + """@article{outras,""" + final

with open(f'Resultados/outras_produções_bibliográficas.bib', 'w', encoding='UTF-8') as bibfile:
	bibfile.write(bibtex)
