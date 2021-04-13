import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

bibtex = """@article{article,
  author  = {Peter Adams}, 
  title   = {The title of the work},
  journal = {The name of the journal},
  year    = {1993},
  number  = {2},
  pages   = {201-213},
  note    = {An optional note}, 
  volume  = {4}
}"""

# with open('bibtexTest.bib', 'w') as bibfile:
#     bibfile.write(bibtex)

with open('bibtex.bib') as bibtex_file:
	parser = BibTexParser(common_strings=False)
	parser.ignore_nonstandard_types = False
	parser.homogenise_fields = False
	bib_database = bibtexparser.load(bibtex_file, parser)

bib_database.entries[0]['title'] = 'titulo'
print(bib_database.entries)

writer = BibTexWriter()
with open('bibtexTest.bib', 'w') as bibfile:
    bibfile.write(writer.write(bib_database))
