# Classes with each type of publication and their respective tags, keys and indexes from the xml resume

class Article():
	def __init__(self):
		super(Article, self).__init__()
		bibTags = ('title', 'journal', 'year', 'pages', 'volume', 'doi') # The fields(tags)
		xmlKeys = ('TITULO-DO-ARTIGO', 'TITULO-DO-PERIODICO-OU-REVISTA', 'ANO-DO-ARTIGO', ('PAGINA-INICIAL', 'PAGINA-FINAL'), 'VOLUME', 'DOI') # The keys (from the xml dictionary) corresponding to each bib tag
		indexes = (0, 1, 0, (1, 1), 1, 0) # The index where the dictionary will be found

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'artigos' # Name of the file that will be saved


class Book():
	def __init__(self):
		super(Book, self).__init__()
		bibTags = ('title', 'edition', 'address', 'publisher', 'year', 'volume', 'series', 'pages', 'isbn', 'doi')
		xmlKeys = ('TITULO-DO-LIVRO', 'NUMERO-DA-EDICAO-REVISAO', 'CIDADE-DA-EDITORA', 'NOME-DA-EDITORA', 'ANO', 'NUMERO-DE-VOLUMES', 'NUMERO-DA-SERIE', 'NUMERO-DE-PAGINAS', 'ISBN', 'DOI')
		indexes = (0, 1, 1, 1, 0, 1, 1, 1, 1, 0)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'livros'


class Chapter():
	def __init__(self):
		super(Chapter, self).__init__()
		bibTags = ('organization', 'title', 'booktitle', 'address', 'publisher', 'year', 'volume', 'edition', 'pages', 'isbn', 'doi')
		xmlKeys = ('ORGANIZADORES', 'TITULO-DO-CAPITULO-DO-LIVRO', 'TITULO-DO-LIVRO', 'CIDADE-DA-EDITORA', 'NOME-DA-EDITORA', 'ANO', 'NUMERO-DE-VOLUMES', 'NUMERO-DA-EDICAO-REVISAO', ('PAGINA-INICIAL', 'PAGINA-FINAL'), 'ISBN', 'DOI')
		indexes = (1, 0, 1, 1, 1, 0, 1, 1, (1, 1), 1, 0)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'capitulos'


class Text():
	def __init__(self):
		super(Text, self).__init__()
		bibTags = ('title', 'journal', 'address', 'volume', 'pages', 'year', 'doi')
		xmlKeys = ('TITULO-DO-TEXTO', 'TITULO-DO-JORNAL-OU-REVISTA', 'LOCAL-DE-PUBLICACAO', 'VOLUME', ('PAGINA-INICIAL', 'PAGINA-FINAL'), 'ANO-DO-TEXTO', 'DOI')
		indexes = (0, 1, 1, 1, (1, 1), 0, 0)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'textos'


class Event():
	def __init__(self):
		super(Event, self).__init__()
		bibTags = ('title', 'booktitle', 'address', 'publisher', 'year', 'volume', 'pages', 'doi')
		xmlKeys = ('TITULO-DO-TRABALHO', 'NOME-DO-EVENTO', 'CIDADE-DO-EVENTO', 'NOME-DA-EDITORA', 'ANO-DO-TRABALHO', 'VOLUME', ('PAGINA-INICIAL', 'PAGINA-FINAL'), 'DOI')
		indexes = (0, 1, 1, 1, 0, 1, (1, 1), 0)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'eventos'


class Conference():
	def __init__(self):
		super(Conference, self).__init__()
		bibTags = ('title', 'year', 'booktitle')
		xmlKeys = ('TITULO', 'ANO', 'NOME-DO-EVENTO')
		indexes = (0, 0, 1)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'apresentações'


class Other():
	def __init__(self):
		super(Other, self).__init__()
		bibTags = ('title', 'address', 'publisher', 'year', 'pages', 'doi')
		xmlKeys = ('TITULO', 'CIDADE-DA-EDITORA', 'EDITORA', 'ANO', 'NUMERO-DE-PAGINAS', 'DOI')
		indexes = (0, 1, 1, 0, 1, 0)

		self.tags = list(zip(bibTags, xmlKeys, indexes))
		self.fileName = 'outras'