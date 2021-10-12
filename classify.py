import numpy as np
import nltk
import math
import matplotlib.pyplot as plt
import csv
import random
from sklearn.cluster import KMeans

def distance(p1, p2):
	dim = len(p1)
	dist = 0.0
	for a in range(dim):
		dif = math.pow((p1[a]-p2[a]),2)
		dist = dist + dif
	dist = math.sqrt(dist)
	return dist

def swarm(matrix,numCent,iterations,numPart,centr):
	dimension = len(matrix[0])
	inertia = 0.1
	acc1 = 0.1
	acc2 = 0.1
	numVec = len(matrix)
	centroids = np.zeros((numPart,numCent,dimension))
	label = np.zeros((numPart,numVec))
	distPoint = np.zeros((numPart,numVec))
	fitFunVec = np.zeros(numPart)
	bestLabel =np.zeros(numVec)
	gBest = np.zeros((numCent,dimension))
	gBestDist = 10000
	partVel = np.zeros((numPart,numCent,dimension))
	partBest = np.zeros((numPart,numCent,dimension))
	partBestDist = np.zeros(numPart)
	for pa in range(numPart):
		partBestDist[pa] = 10000
		for a in range(numCent):
			for b in range(dimension):
				centroids[pa][a][b] =0.001*random.random()
	centroids[0] = centr
	for t in range(iterations):
		for part in range(numPart):
			for vec in range(numVec):
				minDist = 1000
				for cent in range(numCent):
					distVec = distance(centroids[part][cent],matrix[vec])
					if(distVec<minDist):
						label[part][vec] = cent
						distPoint[part][vec] = distVec
						minDist = distVec
			#calculate fitness
			fitFun = 0
			for c in range(numCent):
				sum = 0
				num = 0
				for v in range(numVec):
					if(label[part][v] ==c):
						sum = sum + distPoint[part][v]
						num = num + 1
				if(num>0):
					fitFun = fitFun + sum/num
			fitFunVec[part] = fitFun/numCent
			if(fitFunVec[part] < partBestDist[part]):
				for nc in range(numCent):
					for d in range(dimension):
						partBest[part][nc][d] = centroids[part][nc][d]
					partBestDist[part] = fitFunVec[part]
			if(fitFunVec[part]<gBestDist):
				for nc in range(numCent):
					for d in range(dimension):
						gBest[nc][d] = centroids[part][nc][d]
				for lab in range(numVec):
					bestLabel[lab] = label[part][lab]
				gBestDist = fitFunVec[part]
		#print(partBestDist)
		#update positions
		for par in range(numPart):
			for cen in range(numCent):
				for dim in range(dimension):
					act = centroids[par][cen][dim]
					vel0 = inertia*partVel[par][cen][dim]
					vel1 = acc1*(-centroids[par][cen][dim] + partBest[par][cen][dim])
					vel2 = acc2*(-centroids[par][cen][dim] + gBest[cen][dim])
					partVel[par][cen][dim] = vel0 + vel1 + vel2
					#print(partVel[par][cen][dim])
					centroids[par][cen][dim] = act + partVel[par][cen][dim]
		#print("it ",t)
	#print(centroids)
	#print("Best: ",gBestDist)
	return(gBest,bestLabel)

metFreqV = np.load("metFreq.npy")
negFreqV = np.load("negFreq.npy")

totalDocs = len(metFreqV)
halfDocs = int(totalDocs/2)
plt.xlabel("N1")
plt.ylabel("N2")
plt.xticks(rotation="vertical")
#print(metFreqV)
#print(negFreqV)
# yvalues = []
# xvalues = []
# colors = []

freqMat =np.zeros((totalDocs,2))
for nod in range(halfDocs):
	# yvalues.append(value[nod])
	# xvalues.append("NS-"+str(nod))
	# colors.append("blue")
# for nod in range(halfDocs,totalDocs):
	# yvalues.append(value[nod])
	# xvalues.append("SU-"+str(nod))
	# colors.append("red")
	plt.plot(metFreqV[nod],negFreqV[nod],'bo')
	plt.plot(metFreqV[nod+halfDocs],negFreqV[nod+halfDocs],'ro')
	freqMat[nod][0]= metFreqV[nod]
	freqMat[nod][1] = negFreqV[nod]
# plt.bar(range(0,totalDocs),height=yvalues,tick_label=xvalues, color = colors)

#kmeans
plt.figure(2)
kmeans = KMeans(n_clusters=2)
kmeans.fit(freqMat)
labels = kmeans.labels_
realLabels = []
nonSuiLab0 =0
nonSuiLab1 = 0
suiLab0 =0
suiLab1 = 0
for s in range(halfDocs):
	if(labels[s] == 0):
		nonSuiLab0 = nonSuiLab0 + 1
		plt.plot(metFreqV[s],negFreqV[s],'g+')
	else:
		nonSuiLab1 = nonSuiLab1 +1
		plt.plot(metFreqV[s],negFreqV[s],'r+')
	if(labels[s+halfDocs] == 0):
		suiLab0 = suiLab0 + 1
		plt.plot(metFreqV[s+halfDocs],negFreqV[s+halfDocs],'gx')
	else:
		suiLab1 = suiLab1 +1
		plt.plot(metFreqV[s+halfDocs],negFreqV[s+halfDocs],'rx')
arr = kmeans.cluster_centers_
for r in range(2):
	plt.plot(arr[r][0],arr[r][1],'o')

print("---------------K Means----------------")
print("Centroids: ",arr)
print("Non Suicidal in group A: ",nonSuiLab0)
print("Non Suicidal in group B: ",nonSuiLab1)
print("Suicidal in group A:",suiLab0)
print("Non Suicidal in group B:",suiLab1)

#Particle swarm
plt.figure(3)
centSwarm,labelSwarm = swarm(freqMat,2,100,3,arr)
nonSuiLab0Sw =0
nonSuiLab1Sw = 0
suiLab0Sw =0
suiLab1Sw = 0
for s1 in range(halfDocs):
	if(labelSwarm[s1] == 0.0):
		nonSuiLab0Sw = nonSuiLab0Sw + 1
		plt.plot(metFreqV[s1],negFreqV[s1],'g+')
	else:
		nonSuiLab1Sw = nonSuiLab1Sw +1
		plt.plot(metFreqV[s1],negFreqV[s1],'r+')
	if(labelSwarm[s1+halfDocs] == 0.0):
		suiLab0Sw = suiLab0Sw + 1
		plt.plot(metFreqV[s1+halfDocs],negFreqV[s1+halfDocs],'gx')
	else:
		suiLab1Sw = suiLab1Sw +1
		plt.plot(metFreqV[s1+halfDocs],negFreqV[s1+halfDocs],'rx')
		
print("-------------Particle Swarm----------------")
print("Swarm centroids",centSwarm)
print("Non Suicidal in group A: ",nonSuiLab0Sw)
print("Non Suicidal in group B:",nonSuiLab1Sw)
print("Suicidal in group A:",suiLab0Sw)
print("Suicidal in group B:",suiLab1Sw)

plt.show()
