import os
import random
import subprocess

path_questoes=os.path.join(os.getcwd(),"../banco-questoes/calculo2/ficha4")
rel_path = "/../banco-questoes/calculo2/ficha4/"


# Dados: o script está na pasta x
# Preciso pegar o caminho de onde estou ate o endereco das questo

def rel_path(folder_name):
	return "/banco-questoes/calculo2/"+folder_name

# list of files from the path_questoes
def list_files(folder_name):
	path_questions = os.join(os.getcwd)
	lista=os.listdir(path_questoes)

def questions_list(folder_name):
	path_questoes


#questoes_sorteadas=[rel_path+lista[i] for i in random.sample(range(len(lista)),5)]

# function to get the path of the desired folder
def get_folder(nome_pasta):
	path_questoes = os.path.join(os.getcwd(),"banco-questoes/"+folder_name)
	return path_questoes


#randomly choose n questions from a list and return another list
def sorted_questions(list_of_questions , n):
	return [lista[i] for i in random.sample(range(len()))]
