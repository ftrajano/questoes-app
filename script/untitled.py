import os
import random
import subprocess

path_questoes=os.path.join(os.getcwd(),"questoes/conjuntos")
lista=os.listdir(path_questoes)

questoes_sorteadas=[lista[i] for i in random.sample(range(len(lista)),5)]


content=r'''
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
\usepackage[latin1]{{inputenc}}
\usepackage{{hyperref}}
\usepackage{{dsfont}}
\usepackage{{upgreek}}
\usepackage{{graphicx}}
\usepackage{{indentfirst}}%1ª linha do capitulo em paragrafo%
\setcounter{{MaxMatrixCols}}{{30}}
\usepackage{{color}}

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

%-----------------PRIMEIRA QUESTÌO-----------------------------------------
\item 
\input{{{0}}}

%------------------SEGUNDA QUESTÌO------------------------------------------
\item 
\input{{{1}}}

%----------------TERCEIRA QUESTÌO--------------------------------------------
\item 
\input{{{2}}}

%-----------------QUINTA QUESTÌO-----------------------------------------------
\item 
\input{{{3}}}

%----------------QUARTA QUESTÌO---------------------------------------------
\item 
\input{{{4}}}

\end{{enumerate}}
\end{{document}}

'''.format(questoes_sorteadas[0],questoes_sorteadas[1],questoes_sorteadas[2],questoes_sorteadas[3],questoes_sorteadas[4])
with open('teste.tex', 'w') as f:
	f.write(content)

proc = subprocess.Popen(['pdflatex','teste.tex'])
