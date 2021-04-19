import os
import random
import subprocess

#Pasta do projeto
#/Users/felipe/Desktop/ftrajano/app-questoes/script
#/Users/felipe/Desktop/ftrajano/app-questoes/banco-questoes/ficha2
#/Users/felipe/Desktop/ftrajano/app-questoes/banco-questoes/ficha3
#/Users/felipe/Desktop/ftrajano/app-questoes/banco-questoes/ficha4


###############################################################################
#						GERAR LISTA DE CAMINHOS 
def caminho_questoes(pasta):
	return os.path.join(os.getcwd(),"../banco-questoes/calculo2/"+pasta)


def caminhos_questoes_array(pastas):
	pasta_caminhos = [caminho_questoes(pasta) for pasta in pastas]
	return pasta_caminhos


################################################################################
#						LISTAR OS ARQUIVOS DE UMA PASTA

# Lista os arquivos da pasta
def lista_questoes(pasta):
	lista = os.listdir(pasta)
	if('.DS_Store') in lista:
		lista.remove('.DS_Store')
	return lista

#gera uma lista aplicando a funcao acima numa lista de pastas
def lista_das_listas_questoes(lista):
	lista_das_questoes_por_pasta = [lista_questoes(pasta) for pasta in lista]
	return lista_das_questoes_por_pasta


############################################################################
#						EMBARALHA AS QUESTOES 


#Gerar uma lista com os enderecos relativos das questoes
def random_questions(lista,n):
	return [lista[i] for i in random.sample(range(len(lista)),n)]



##################################################################################
def adiciona_caminho_relativo(lista, rel_path):
	return [rel_path+item for item in lista]


# function to get the path of the desired folder
def get_folder(nome_pasta):
	path_questoes = os.path.join(os.getcwd(),"banco-questoes/"+folder_name)
	return path_questoes


#Funcao Principal
#recebe uma lista de pastas e uma lista de quantidade de questoes por pasta
#gera n provas com a quantidade de questoes estabelecidas por pasta.

#lista_de_arquivos = [lista_questoes(item) for item in lista_pastas]


#gerar lista de prova sorteando as questoes de cada pasta.
#[3,3,4]

def questoes_app(lista_para_embaralhar, questoes_por_pasta, quantidade_de_provas,lista_pastas):

	
	lista_para_embaralhar2 = [] 
	
	for k in range(len(lista_pastas)):
		lista_cam_relativo = adiciona_caminho_relativo(lista_para_embaralhar[k],"../banco-questoes/calculo2/"+lista_pastas[k]+'/')
		lista_para_embaralhar2.extend(lista_cam_relativo)
	
	provas = []
	for j in range(quantidade_de_provas):
		prova = []
		for i in range(len(questoes_por_pasta)):
			embaralhada = random_questions(lista_para_embaralhar2,questoes_por_pasta[i])
			print(len(embaralhada))
			prova.extend(embaralhada)
		provas.append(prova)
	return provas

def adiciona_chaves(lista):
	for i in range(len(lista)):
		lista[i] = '{'+lista[i]+'}'
	


def generate_template(n):
	question_template =r''' 
	%-----------------QUESTION-----------------------------------------
	\item \input{{{i}}}
	'''
	qt = ''
	for i in range(0,n):
		qt+=question_template.format(i=i)
	return qt

#recebe a lista de questoes ja sorteadas e devolve o template
# falta ainda substituir pelo endereco das questoes
def template(lista_prova):
	content1=r'''
	\documentclass[12pt]{{report}}

	%EndMSIPreambleData
	\providecommand{{\U}}[1]{{\protect\rule{{.1in}}{{.1in}}}}
	\pretolerance=10000
	\baselineskip=9.in
	\evensidemargin 0.0 in
	\oddsidemargin 0.0 in
	\parindent 24pt
	\textheight 8.5 in
	\textwidth 6.5 in
	\topmargin -0.5 in
	\renewcommand{{\baselinestretch}}{{1.18}} %% Packages
	\usepackage{{amssymb,amsthm,amsfonts,amsmath,pifont}}
	\usepackage{{enumerate}}
	\usepackage[brazil]{{babel}}
	\usepackage[utf8]{{inputenc}}
	\usepackage{{hyperref}}
	\usepackage{{dsfont}}
	\usepackage{{upgreek}}
	\usepackage{{graphicx}}
	\usepackage{{indentfirst}}%1ª linha do capitulo em paragrafo%
	\setcounter{{MaxMatrixCols}}{{30}}
	\usepackage{{color}}
	\usepackage{{relsize}}

	%\usepackage[applemac]{{inputenc}}
	%\usepackage[portuges,brazilian]{{babel}}
	%\usepackage[T1]{{fontenc}}

	\begin{{document}}
	\thispagestyle{{empty}}

	\begin{{figure}}[ht]
	\hspace{{0.5cm}}
	\begin{{minipage}}[b]{{0.11\linewidth}}
	\centering
	\includegraphics[width=1.5cm]{{logoufpe.jpg}}
	\end{{minipage}}
	\hspace{{0.5cm}}
	\begin{{minipage}}[b]{{0.75\linewidth}}
	\centering
	\large\textbf{{Universidade Federal de Pernambuco}}\\
	Centro Acad\^emico do Agreste	\\
	N\'ucleo de Forma\c{{c}}\~ao Docente\\
	Equa\c{{c}}\~oes Diferenciais
	\end{{minipage}}
	\end{{figure}}
	Professor: \textbf{{Felipe Trajano}}
	\vspace{{0.2cm}}

	Aluno: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nota: \_\_\_\_\_\_\_\_\_\_\_\_
	\vspace{{0.2cm}}
	\begin{{center}}
	\textbf{{Avalia\c{{c}}\~ao Final}}
	\end{{center}}

	OBS.: Apenas respostas justificadas ser\~ao consideradas.

	\vspace{{0.2cm}}
	\normalsize

	\begin{{enumerate}}
	'''

	content2 = generate_template(len(lista_prova))

	content3 = r'''
	\end{{enumerate}}
	\end{{document}}
	'''

	content = content1+content2+content3

	return content

def gerarProva(lista_de_provas):
	print(len(lista_de_provas))
	provas = []
	for prova in lista_de_provas:
		print('quantidade de questoes é: '+str(len(prova)))
		provas.append(template(prova).format(*prova))
	return provas



def gerar_prova(lista_de_provas_content):
	for i in range(len(lista_de_provas_content)):
		tex_file = 'teste{}.tex'.format(i) 
		with open(tex_file, 'w') as f:
			f.write(lista_de_provas_content[i])
			proc = subprocess.Popen(['pdflatex',tex_file])

nome_da_pastas = ['ficha2','ficha3','ficha4']
questoes_por_assunto=[3,3,4]
quantidade_provas = 36

def prova(nome_da_pastas, questoes_por_assunto,quantidade_de_provas):
	pastas_caminho = caminhos_questoes_array(nome_da_pastas)
	lista_das_questoes_por_pasta = lista_das_listas_questoes(pastas_caminho)
	provas_embaralhadas = questoes_app(lista_das_questoes_por_pasta,questoes_por_assunto,quantidade_de_provas,nome_da_pastas)
	for pasta in provas_embaralhadas:
		lista_com_chaves = adiciona_chaves(pasta)
	provas = gerarProva(provas_embaralhadas)
	gerar_prova(provas)

prova(nome_da_pastas, questoes_por_assunto, quantidade_provas)

#print(caminhos_questoes_array(nome_da_pastas))

#for item in caminhos_questoes_array(nome_da_pastas):
#	print(lista_questoes(item))
