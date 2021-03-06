import re

def check_exception(word): # Checa se a palavra corresponde a uma exceção (artigo, preposição ou conjunção)
	exceptionsPort = ['o', 'os', 'a', 'as', 'um', 'uns', 'uma', 'umas', 'ao', 'aos', 'à', 'às', 'do', 'dos', 'da', 'das', 'dum', 'duns', 'duma', 'dumas', 'no', 'nos', 'na', 'nas', 'num', 'nuns', 'numa', 'numas', 'pelo', 'pelos', 'pela', 'pelas', 'ante', 'após', 'até', 'com', 'de', 'em', 'para', 'por', 'sem', 'sob', 'trás', 'e', 'nem', 'mas', 'ou', 'já', 'que', 'pois']
	
	exceptionsEng = ['and', 'but', 'or', 'so', 'the', 'a', 'an', 'of', 'in', 
	                 'on', 'to', 'for', 'at', 'as', 'with']

	exceptionsEsp = ['a', 'de', 'en', 'por', 'con', 'para', 'sin', 'y', 'ni', 'que', 'así', 'no', 'o', 'ya', 'el', 'él', 'la', 'lo', 'los', 'las', 'un', 'una', 'unos', 'unas']

	if word.lower() in exceptionsEng or word.lower() in exceptionsEsp or word.lower() in exceptionsPort:
		return True
	else:
		return False


def check_for_abbrev(word): # Checa se a palavra corresponde a alguma sigla conhecida
	abbrevs = ['IEEE', 'ACM', 'MDPI', 'VLSI', 'IFIP', 'UFSM', 'UFSC', 'UFRJ', 'USP', 'UNIVALI']
	if word.upper() in abbrevs:
		word = word.upper()

	return word


def check_for_roman_numerals(word): # Checa se a palavra é um número romano
	roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	cont = 0 
	
	for letter in word:
		if letter.upper() in roman:
			cont += 1 

	if cont == len(word): # Se todas as letras da palavra fizerem parte dos numerais romanos
		return word.upper()
	else:
		return word


def treat_abbrev(text): 
	for pos, word in enumerate(text):
		if word == '-': # Sentences separated by '-'
			if len(text[pos:]) <= 2: 
				cont = pos + 1
				while cont < len(text):
					text[cont] = text[cont].upper()
					cont += 1
			elif len(text[:pos]) <= 2:
				cont = 0
				while cont < pos:
					text[cont] = text[cont].upper()
					cont += 1

		if word != '' and word[0] == '(': # If the word starts with a parenthesis
			splitted = word.split('(')
			text[pos] = '(' + splitted[1].upper()

		text[pos] = check_for_abbrev(text[pos])
		text[pos] = check_for_roman_numerals(text[pos])

	return text


def title_case(text):

	lowercase_words = re.split(" ", text.lower())
	final_words = [lowercase_words[0].capitalize()]
	final_words += [word if check_exception(word) is True else word.capitalize() for word in lowercase_words[1:]]
	final_words = treat_abbrev(final_words)
	final_text = " ".join(final_words)

	return final_text

