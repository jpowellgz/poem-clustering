import numpy as np
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
#from nltk.stem.snowball import SnowballStemmer
#from nltk.corpus import stopwords
#Opciones para obtener solo raices de las palabras
#Options to stem words

#define a file for the full vocabulary
#definir un archivo para el vocabulario

fullFile = open("VOCAB.txt","w",encoding='utf-8')
docsByPoet = 50
#stemmer = SnowballStemmer("spanish")
#stopwordVec = set(stopwords.words('spanish'))

#Extract words from every poem of every poet in ns and s
#Extraer palabras para cada poema de cada autor en s y ns

for k in range(1,7):
	for i in range(1,docsByPoet+1):
		number = "ns/"+str(k)+"/D"+str(i)+".txt"
		#number1 = "ns/"+str(k)+"/ND"+str(i)+".txt"
		poem = open(number,"r")
		#newpoem = open(number1,"w")
		text = poem.read()
		# tokens = nltk.word_tokenize(text.lower())
		# vect =[w for w in tokens if w.isalpha() and not w in stopwordVec]
		# for wo in vect:
			# wo = stemmer.stem(wo)
			# newpoem.write(wo+" ")
			# fullFile.write(wo+" ")
		fullFile.write(text.lower())
		fullFile.write("\n")
		#newpoem.close()
		poem.close()
for k in range(1,7):
	for i in range(1,docsByPoet + 1):
		number = "s/"+str(k)+"/D"+str(i)+".txt"
		#number1 = "s/"+str(k)+"/ND"+str(i)+".txt"
		poem = open(number,"r")
		#newpoem = open(number1,"w")
		text = poem.read()
		# tokens = nltk.word_tokenize(text.lower())
		# vect =[w for w in tokens if w.isalpha() and not w in stopwordVec]
		# for wo in vect:
			# wo = stemmer.stem(wo)
			# newpoem.write(wo+" ")
			# fullFile.write(wo+" ")
		fullFile.write(text.lower())
		fullFile.write("\n")
		#newpoem.close()
		poem.close()
fullFile.close()
