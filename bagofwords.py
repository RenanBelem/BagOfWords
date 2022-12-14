# -*- coding: utf-8 -*-
"""BagOfWords.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QEBmVxb8Q5o7tTEjgA88c2PFgSafxsY3
"""

#RENAN BELEM BIAVATI

#ENUNCIADO
#Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e
#imprimir esta matriz na tela. Para tanto:
#a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores,
#onde cada item será uma das palavras da sentença.
#b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores,
#onde cada item será um lexema.
#c) Este único corpus será usado para gerar o vocabulário.
#d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da
#técnica bag of Words em tod0 o corpus.

from bs4 import BeautifulSoup
import requests
import spacy

s1 = requests.get("https://www.linguamatics.com/what-text-mining-text-analytics-and-natural-language-processing")
s2 = requests.get("https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP")
s3 = requests.get("https://en.wikipedia.org/wiki/Natural_language_processing")
s4 = requests.get("https://monkeylearn.com/blog/natural-language-processing-techniques/")
s5 = requests.get("https://towardsdatascience.com/introduction-to-natural-language-processing-for-text-df845750fb63")

bs1 = BeautifulSoup(s1.text,"html.parser").find_all("p")[2].get_text()
bs2 = BeautifulSoup(s2.text,"html.parser").find_all("p")[2].get_text()
bs3 = BeautifulSoup(s3.text,"html.parser").find_all("p")[2].get_text()
bs4 = BeautifulSoup(s4.text,"html.parser").find_all("p")[2].get_text()
bs5 = BeautifulSoup(s5.text,"html.parser").find_all("p")[2].get_text()

var = spacy.load("en_core_web_sm")
def verifica(s):
  x = var(s)
  return [x.orth_ for x in x if not x.is_punct]

envio1 = verifica(bs1)
envio2 = verifica(bs2)
envio3 = verifica(bs3)
envio4 = verifica(bs4)
envio5 = verifica(bs5)
dicionario = (envio1 + envio2 + envio3 + envio4 + envio5)
vetorD = [dicionario]

def frequencia(envio, tudo):
  vetorF = []
  for palavra in tudo:
    freq = 0
    for frase in envio:
      if frase == palavra:
        freq += 1
    vetorF.append(freq)
  return vetorF

vetorD.append(frequencia(envio1, dicionario))
vetorD.append(frequencia(envio2, dicionario))
vetorD.append(frequencia(envio3, dicionario))
vetorD.append(frequencia(envio4, dicionario))
vetorD.append(frequencia(envio5, dicionario))

print("Matriz Termo Documento:")
print("\n           " ,dicionario)
print("Documento 1",vetorD[1])
print("Documento 2",vetorD[2])
print("Documento 3",vetorD[3])
print("Documento 4",vetorD[4])
print("Documento 5",vetorD[5])