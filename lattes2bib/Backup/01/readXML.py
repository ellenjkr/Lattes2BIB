import xml.etree.ElementTree as ET

mytree = ET.parse('curriculo.xml')
myroot = mytree.getroot()


# print(myroot[1][0].tag) # TRABALHOS-EM-EVENTOS

# print(myroot[1][1].tag) # ARTIGOS-PUBLICADOS
# print(myroot[1][1][0][0].attrib)

# print(myroot[1][1].tag) # Artigos Publicados # Até [1][4]

# print(myroot[1][2].tag) # Livros e Capitulos
# print(myroot[1][2][0].tag) # Livros Publicados ou Organizados
# print(myroot[1][2][1].tag) # CAPITULOS-DE-LIVROS-PUBLICADOS

# print(myroot[1][3].tag) # Textos em jornais ou revistas

# print(myroot[1][4].tag) # DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA

# print(myroot[2].tag) # Produção Técnica
# print(myroot[3].tag) # Outra Produção
# print(myroot[4].tag) # Dados Complementares


qtd = 0
for i in myroot[1][1]:
	#print(i[0].attrib['TITULO-DO-ARTIGO'])
	qtd += 1
print(f'Artigos completos publicados em periódicos: {qtd}')


qtd2 = 0
for i in myroot[1][2][0]:
	#print(i[0].attrib['TITULO-DO-LIVRO'])
	qtd2 += 1
print(f'Livros publicados/organizados ou edições: {qtd2}')


qtd3 = 0
for i in myroot[1][2][1]:
	#print(i[0].attrib['TITULO-DO-CAPITULO-DO-LIVRO'])
	qtd3 += 1
print(f'Capítulos de livros publicados: {qtd3}')


qtd4 = 0
for i in myroot[1][3]:
	# print(i[0].attrib['TITULO-DO-TEXTO'])
	qtd4 += 1
print(f'Textos em jornais de notícias/revistas: {qtd4}')


'''
Trabalhos completos publicados em anais de congressos 97
+ Resumos expandidos publicados em anais de congressos 3
+ Resumos publicados em anais de congressos 23
= 123
'''
qtd5 = 0
for i in myroot[1][0]:
	# print(i[0].attrib['TITULO-DO-TRABALHO']) # 97 + 3 + 23
	qtd5 += 1
print(f'Publicados em anais de congressos: {qtd5}')


# ==========================================================
# VER 

qtd6 = 0
for i in myroot[2]:
	if i.tag == 'DEMAIS-TIPOS-DE-PRODUCAO-TECNICA':
		for j in i:
			if j.tag == 'APRESENTACAO-DE-TRABALHO':
				qtd6 += 1
print(f'Apresentações de Trabalho: {qtd6}')

# ==========================================================


qtd7 = 0
for i in myroot[1][4]:
	# print(i[0].attrib['TITULO'])
	qtd7 += 1
print(f'Outras produções bibliográficas: {qtd7}')


# =========================================================================================

'''
FALTOU

Assessoria e consultoria
1.
ZEFERINO, Cesar Albenes. Consultor externo do processo de análise de projetos de pesquisa para a Pró-Reitoria de Pesquisa e Pós-Graduação da Universidade Regional de Blumenau nos programas PIBIC/CNPq e PIBIC/FURB. 2005.

2.
ZEFERINO, Cesar Albenes. Membro do Comitê de Avaliação de propostas para Projeto do Sistema Brasileiro de TV Digital (MC/MCT/FINEP/FUNTEL). 2004.

'''
teste = 0
qtd8 = 0
for i in myroot[2]:
	teste+=1
	if i.tag == 'SOFTWARE':
		qtd8 += 1
print(teste)
qtd9 = 0
for i in myroot[2]:
	if i.tag == 'PRODUTO-TECNOLOGICO':
		qtd9 += 1

# qtd10 = 0
# for i in myroot[2]:
# 	if i.tag == 'TRABALHO-TECNICO': VER
# 		qtd10 += 1

'''
FALTOU

Entrevistas, mesas redondas, programas e comentários na mídia
1.
ZEFERINO, Cesar Albenes; SPANN, James ; MATTEI, Andre Luiz Pierri . Impacto do ensino de engenharia e de ciências na indústria e no desenvolvimento econômico,. 2017. (Programa de rádio ou TV/Mesa redonda). 
'''

qtd11 = 0
for i in myroot[2]:
	if i.tag == 'DEMAIS-TIPOS-DE-PRODUCAO-TECNICA':
		for j in i:
			if j.tag == 'CURSO-DE-CURTA-DURACAO-MINISTRADO': # Veio um a menos
				qtd11 += 1






print(qtd8)
print(qtd9)
#print(qtd10)
print(qtd11)


'''
apresentacoes = []

for i in myroot[2]:
	if i.tag == 'DEMAIS-TIPOS-DE-PRODUCAO-TECNICA':
		for j in i:
			if j.tag == 'APRESENTACAO-DE-TRABALHO':
				apresentacoes.append(i)

for pos, apresentacao in enumerate(apresentacoes):
	if pos == 0:
		print(apresentacao[144][0].attrib)
	apresentacao = apresentacao[0]
'''