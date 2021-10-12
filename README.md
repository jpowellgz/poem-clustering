# Clustering of suicidal and non-suicidal poems using K-means and Particle Swarm Optimization

*Suicide is considered a public health issue, and its early detection and treatment may contribute to its prevention. Automatic detection of suicidal ideation indicators within texts can be a useful tool to prevent it. In this work a corpus was compiled, which consists of poems written by twelve different poets, where six of them committed suicide. Two vector representations were experimented on, one with the total number of words and another with words related to negative emotional concepts. The vectors were clustered using two algorithms: K-Means and a K-Means with Particle Swarm Optimization hybrid. The efficiency of the vector representations and the used algorithms were compared, obtaining as result that, through the hybrid algorithm and the negative emotional concepts vocabulary, the groups of poets with suicidal ideation and without it could be distinguished with an accuracy of 0.98. Keywords: Clustering, Metaheuristics, K-Means, Particle Swarm Optimization, Suicidal Ideation Detection.doi: https://doi.org/10.36825/RITI.09.18.002*

Use as reference:  
González, J. E. P., Ruiz, M. C., & García, M. J. S. (2021). Agrupamiento de poemas de autores suicidas y no suicidas usando K-means y enjambre de partículas. Revista de Investigación en Tecnologías de la Información: RITI, 9(18), 14-23.

-ns and s folders contain poems arranged as non-suicidal and suicidal from 12 poets.  
-Extract.py obtains the complete vocabulary from the set of poems.  
-Frequency.py counts the frequency of specific words which are contained in the methaphorSet and negativeSet, inside the complete vocabulary.  
-Classify.py performs the K-means with particle swarm optimization clustering
  
# Agrupamiento de poemas de autores suicidas y no suicidas usando K-means y enjambre de partículas 
  
*El suicidio es considerado un problema de salud pública, y su detección y tratamiento de manera temprana pueden contribuir a prevenirlo. La detección automática de indicadores de ideación suicida en textos tiene posibilidad de ser una herramienta útil para su prevención. En este trabajo, se reunió un corpus formado por poemas de doce poetas distintos, de los cuales seis cometieron suicidio. Se experimentó con dos representaciones vectoriales, una por número total de palabras y otra por palabras relacionadas con conceptos emocionales negativos. Los vectores se agruparon utilizando dos algoritmos: K-means y un híbrido de K-means con Optimización por Enjambre de Partículas. Se comparó la eficiencia de las representaciones vectoriales y de los algoritmos usados y se obtuvo que, por medio del algoritmo híbrido y del vocabulario relacionado con conceptos emocionales negativos, los grupos de poetas con ideación suicidada y sin ella pudieron ser distinguidos con una exactitud de hasta 0.98.Palabras clave: Agrupamiento, Metaheurísticas, K-Means, Optimización por Enjambre de Partículas, Detección de Ideación Suicida.doi: https://doi.org/10.36825/RITI.09.18.002  *
  
Citar como:   
González, J. E. P., Ruiz, M. C., & García, M. J. S. (2021). Agrupamiento de poemas de autores suicidas y no suicidas usando K-means y enjambre de partículas. Revista de Investigación en Tecnologías de la Información: RITI, 9(18), 14-23.  


-ns and s folders contienen poemas de 12 autores, clasificados como suicidas o no suicidas
-Extract.py obtiene el conjunto completo de palabras de los poemas  
-Frequency.py cuenta la frecuencia de palabras específicas en el vocabulario completo, cuando están dentro de los conjuntos  methaphorSet y negativeSet.  
-Classify.py realiza el agrupamiento por K-means y PSO
