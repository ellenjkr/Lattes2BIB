class Article():
	def __init__(self):
		super(Article, self).__init__()
		self.bibTags = ['title', 'journal', 'year', 'pages', 'volume', 'doi'] # The fields(tags)
		self.xmlKeys = ['TITULO-DO-ARTIGO', 'TITULO-DO-PERIODICO-OU-REVISTA', 
		'ANO-DO-ARTIGO', ['PAGINA-INICIAL', 'PAGINA-FINAL'], 'VOLUME', 'DOI'] # The keys (from the xml dictionary) that contains each tag
		self.indexes = [0, 1, 0, [1, 1], 1, 0] # The index where the dictionary will be found
		self.fileName = 'artigos' # Name of the file that will be saved


class Book():
	def __init__(self):
		super(Book, self).__init__()
		self.bibTags = ['title', 'edition', 'address', 'publisher', 'year', 'volume', 'series', 'pages', 'isbn', 'doi']
		self.xmlKeys = ['TITULO-DO-LIVRO', 'NUMERO-DA-EDICAO-REVISAO', 'CIDADE-DA-EDITORA', 'NOME-DA-EDITORA',
						'ANO', 'NUMERO-DE-VOLUMES', 'NUMERO-DA-SERIE', 'NUMERO-DE-PAGINAS', 'ISBN', 'DOI']
		self.indexes = [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
		self.fileName = 'livros'


class Chapter():
	def __init__(self):
		super(Chapter, self).__init__()
		self.bibTags = ['organization', 'title', 'booktitle', 'address', 'publisher', 'year', 'volume', 'edition', 
						'pages', 'isbn', 'doi']
		self.xmlKeys = ['ORGANIZADORES', 'TITULO-DO-CAPITULO-DO-LIVRO', 'TITULO-DO-LIVRO', 'CIDADE-DA-EDITORA', 
						'NOME-DA-EDITORA', 'ANO', 'NUMERO-DE-VOLUMES', 'NUMERO-DA-EDICAO-REVISAO', ['PAGINA-INICIAL', 
						'PAGINA-FINAL'], 'ISBN', 'DOI']
		self.indexes = [1, 0, 1, 1, 1, 0, 1, 1, [1, 1], 1, 0]
		self.fileName = 'capitulos'


class Text():
	def __init__(self):
		super(Text, self).__init__()
		self.bibTags = ['title', 'journal', 'address', 'volume', 'pages', 'year', 'doi']
		self.xmlKeys = ['TITULO-DO-TEXTO', 'TITULO-DO-JORNAL-OU-REVISTA', 'LOCAL-DE-PUBLICACAO',
						'VOLUME', ['PAGINA-INICIAL', 'PAGINA-FINAL'], 'ANO-DO-TEXTO', 'DOI']
		self.indexes = [0, 1, 1, 1, [1, 1], 0, 0]
		self.fileName = 'textos'


class Event():
	def __init__(self):
		super(Event, self).__init__()
		self.bibTags = ['title', 'booktitle', 'address', 'publisher', 'year', 'volume', 'pages', 'doi']
		self.xmlKeys = ['TITULO-DO-TRABALHO', 'NOME-DO-EVENTO', 'CIDADE-DO-EVENTO', 
						'NOME-DA-EDITORA', 'ANO-DO-TRABALHO', 'VOLUME', ['PAGINA-INICIAL', 'PAGINA-FINAL'], 'DOI']
		self.indexes = [0, 1, 1, 1, 0, 1, [1, 1], 0]
		self.fileName = 'eventos'


class Conference():
	def __init__(self):
		super(Conference, self).__init__()
		self.bibTags = ['title', 'year', 'booktitle']
		self.xmlKeys = ['TITULO', 'ANO', 'NOME-DO-EVENTO']
		self.indexes = [0, 0, 1]
		self.fileName = 'apresentações'


class Other():
	def __init__(self):
		super(Other, self).__init__()
		self.bibTags = ['title', 'address', 'publisher', 'year', 'pages', 'doi']
		self.xmlKeys = ['TITULO', 'CIDADE-DA-EDITORA', 'EDITORA', 'ANO', 'NUMERO-DE-PAGINAS', 'DOI']
		self.indexes = [0, 1, 1, 0, 1, 0]
		self.fileName = 'outras'