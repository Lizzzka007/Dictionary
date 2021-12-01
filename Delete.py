import json
import random
import pandas as pd

Filename = "中級から学ぶ日本語.txt"

def func(filename):
	with open(filename,"r", encoding = 'utf8') as read_file: 
		data = json.load(read_file)

	read_file.close()

	words = []
	for row in data:
		lst = []
		lst.append(row['WORD'])
		lst.append(row['READING'])
		lst.append(row['TRANSLATION'])
		words.append(lst.copy())

	print(words)	

	return words

def CreateTextThemes(filename):
	words = func(filename)
	AllDict = {}
	TextNumber = 15
	TextWords = []
	for i in range(50, 81):
		TextWords.append(words[i])

	# Final_dict1 = {TextNumber: TextWords.copy()}
	AllDict[TextNumber] = TextWords.copy()
	
	TextNumber = 16
	TextWords = []
	for i in range(88, 113):
		TextWords.append(words[i])

	AllDict[TextNumber] = TextWords.copy()

	with open(Filename, "a", encoding = "utf-8") as file:
		json.dump(AllDict, file)



if __name__ == '__main__':
	CreateTextThemes("words.json")