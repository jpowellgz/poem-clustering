import numpy as np
import nltk
import csv
import matplotlib.pyplot as plt
import math
#from nltk.stem.snowball import SnowballStemmer

textFile = open('VOCAB.txt',encoding='utf-8')
rawText = textFile.read()	
#Obtain tokens for processing, and frequency distribution
vocabTokens = nltk.word_tokenize(rawText)
distTot = nltk.FreqDist(vocabTokens)
filterVocab =[w for w in distTot] #if w.isalpha()]
textFile.close()

#stemmer = SnowballStemmer("spanish")
nonSui = []
sui = []
docsByPoet = 50
docSize = 1
for k in range(1,7):
	for i in range(1,docsByPoet+1):
		number = "ns/"+str(k)+"/D"+str(i)+".txt"
		poem = open(number,"r")
		text = poem.read()
		tokens = nltk.word_tokenize(text)
		distribNS = nltk.FreqDist(tokens)
		nonSui.append(distribNS)
		poem.close()
for k in range(1,7):
	for i in range(1,docsByPoet+1):
		number = "s/"+str(k)+"/D"+str(i)+".txt"
		poem = open(number,"r")
		text = poem.read()
		tokens = nltk.word_tokenize(text)
		distribS = nltk.FreqDist(tokens)
		sui.append(distribS)
		poem.close()
#totalDocs = docsByPoet*12


metaphorSet = []
negativeSet = []

textFile = open('metaphorSet.txt',encoding = 'utf-8')
metaphorSet = textFile.read().splitlines()
textFile.close()

textFile = open('negativeSet.txt',encoding = 'utf-8')
negativeSet = textFile.read().splitlines()
textFile.close()
print("Tamano N1: ", len(negativeSet))
print("Tamano N2: ", len(metaphorSet))

sizeNeg= len(negativeSet)
sizeMet=len(metaphorSet)
numDocPoet = int(docsByPoet/docSize)
totalDocs = numDocPoet*12
halfDocs= int(totalDocs/2)
metFreq =np.zeros((sizeMet,totalDocs))
negFreq= np.zeros((sizeNeg,totalDocs))
typeFreq = np.zeros(totalDocs)
for docu in range(halfDocs):
	total = 0 
	typeTest = "me"
	for wr in nonSui[docu]:
		if(wr.startswith(typeTest)):
			total = total + nonSui[docu][wr]
	typeFreq[docu]= total/len(nonSui[docu])
	total = 0
	for wr in sui[docu]:
		if(wr.startswith(typeTest)):
			total = total + sui[docu][wr]
	typeFreq[docu+halfDocs] = total/len(sui[docu])
for wor in range(sizeNeg):
	for doc in range(halfDocs):
		currWordNeg = negativeSet[wor]
		sumFreqNNS= 0
		sumFreqNS = 0
		for subdoc in range(docSize):
			indDoc = doc*docSize+ subdoc
			sumFreqNNS=sumFreqNNS +nonSui[indDoc][currWordNeg]
			sumFreqNS = sumFreqNS+sui[indDoc][currWordNeg]
		negFreq[wor][doc] = sumFreqNNS
		negFreq[wor][doc+halfDocs] = sumFreqNS
for wor in range(sizeMet):
	for doc in range(halfDocs):
		currWordMet = metaphorSet[wor]
		sumFreqPNS =0
		sumFreqPS = 0
		for subdoc in range(docSize):
			indDoc = doc*docSize+ subdoc
			sumFreqPNS=sumFreqPNS+nonSui[indDoc][currWordMet]
			sumFreqPS = sumFreqPS+sui[indDoc][currWordMet]
		metFreq[wor][doc] = sumFreqPNS
		metFreq[wor][doc+halfDocs] = sumFreqPS
metFreqV= np.zeros(totalDocs)
negFreqV= np.zeros(totalDocs)
value = np.zeros(totalDocs)

for a in range(halfDocs):
	sumPNS = 0
	sumNNS = 0
	sumPS = 0
	sumNS = 0
	sumWordsPNS = 0
	sumWordsNNS = 0
	sumWordsPS = 0
	sumWordsNS = 0
	for b in range(sizeNeg):
		sumNNS = sumNNS + negFreq[b][a]
		sumNS = sumNS + negFreq[b][a+halfDocs]
	for c in range(sizeMet):
		sumPNS = sumPNS + metFreq[c][a]
		sumPS = sumPS + metFreq[c][a+halfDocs]
	for subd in range(docSize):
		r = a*docSize+subd
		sumWordsPNS = sumWordsPNS+(len(nonSui[r]))
		sumWordsNNS = sumWordsNNS+(len(nonSui[r]))
		sumWordsPS = sumWordsPS+(len(sui[r]))
		sumWordsNS = sumWordsNS+(len(sui[r]))
	metFreqV[a] = sumPNS/sumWordsPNS
	negFreqV[a] = sumNNS/sumWordsNNS
	metFreqV[a+halfDocs] = sumPS/sumWordsPS
	negFreqV[a+halfDocs] = sumNS/sumWordsNS
	# value[a] =metFreqV[a]
	# value[a+halfDocs] = metFreqV[a+halfDocs]
	value[a] = negFreqV[a]
	value[a+halfDocs] = negFreqV[a+halfDocs]
	# value[a] = typeFreq[a]
	# value[a+halfDocs] = typeFreq[a+halfDocs]
print(metFreqV.shape)
np.save("metFreq",metFreqV)
np.save("negFreq",negFreqV)
