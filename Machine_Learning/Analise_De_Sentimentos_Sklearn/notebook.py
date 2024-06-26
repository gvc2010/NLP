
# Importação de bibliotecas


import os
import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

"""**Redução da granularidade dos sentimentos:**"""

# Carregue o corpus
corpus_textos = []
corpus_rotulos = []

with open("analise-sentimentos-2000-noticias.txt", "r", encoding="utf-8-sig") as f:
    for linha in f:
        rotulo, texto = linha.strip().split(";;")
        rotulo = mapeamento_emocoes.get(rotulo.lower(), None)  # Verifica se o rótulo está presente no dicionário
        if rotulo is not None:  # Se o rótulo estiver presente, adiciona ao corpus
            corpus_textos.append(texto)
            corpus_rotulos.append(rotulo)

"""**Configuração dos parâmetros de extração de atributos:**"""

# Vetorização dos textos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus_textos)

# Divisão dos dados em conjuntos de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, corpus_rotulos, test_size=0.2, random_state=42)

# Treinamento do modelo SVM
svm = SVC(kernel='linear')
svm.fit(X_treino, y_treino)

# Avaliação do modelo
previsoes = svm.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)
print("Perfeição do modelo SVM:", acuracia)

"""**Vetorização dos textos usando CountVectorizer**:"""

# Vetorização dos textos usando CountVectorizer com n-grams
vectorizer = CountVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(corpus_textos)



#Utilizando outro classificador de texto:

from sklearn.naive_bayes import MultinomialNB

# Treinamento do modelo Naive Bayes Multinomial
nb_classifier = MultinomialNB()
nb_classifier.fit(X_treino, y_treino)

# Avaliação do modelo
previsoes_nb = nb_classifier.predict(X_teste)
acuracia_nb = accuracy_score(y_teste, previsoes_nb)
print("Perfeição do modelo Naive Bayes:", acuracia_nb)
