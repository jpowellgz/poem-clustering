# Clustering of suicidal and non-suicidal poems using K-means and Particle Swarm Optimization  / Agrupamiento de poemas de autores suicidas y no suicidas usando K-means y enjambre de partículas   

*Suicide is considered a public health issue, and its early detection and treatment may contribute to its prevention. Automatic detection of suicidal ideation indicators within texts can be a useful tool to prevent it. In this work a corpus was compiled, which consists of poems written by twelve different poets, where six of them committed suicide. Two vector representations were experimented on, one with the total number of words and another with words related to negative emotional concepts. The vectors were clustered using two algorithms: K-Means and a K-Means with Particle Swarm Optimization hybrid. The efficiency of the vector representations and the used algorithms were compared, obtaining as result that, through the hybrid algorithm and the negative emotional concepts vocabulary, the groups of poets with suicidal ideation and without it could be distinguished with an accuracy of 0.98. Keywords: Clustering, Metaheuristics, K-Means, Particle Swarm Optimization, Suicidal Ideation Detection.doi: https://doi.org/10.36825/RITI.09.18.002*

Use as reference:  
González, J. E. P., Ruiz, M. C., & García, M. J. S. (2021). Agrupamiento de poemas de autores suicidas y no suicidas usando K-means y enjambre de partículas. Revista de Investigación en Tecnologías de la Información: RITI, 9(18), 14-23.

-ns and s folders contain poems arranged as non-suicidal and suicidal from 12 poets.  
-Extract.py obtains the complete vocabulary from the set of poems.  
-Frequency.py counts the frequency of specific words which are contained in the methaphorSet and negativeSet, inside the complete vocabulary.  
-Classify.py performs the K-means with particle swarm optimization clustering
