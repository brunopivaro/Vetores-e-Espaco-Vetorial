# Importando os pacotes

import ast
import numpy as np
import pandas as pd
import sklearn
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pd.options.mode.chained_assignment = None

# Carregando os dados

df_filmes = pd.read_csv("Datasets/dataset_filmes.csv")
print(df_filmes.shape)
print(df_filmes.head())
print(df_filmes.columns)

df_elenco = pd.read_csv("Datasets/dataset_elenco.csv")
print(df_elenco.shape)
print(df_elenco.head())
print(df_elenco.columns)

# Organizando os dados

df = df_filmes.merge(df_elenco, on = "title") # Join na coluna "title"

print(df.shape)
print(df.head())
print(df.columns)

# Filtrando colunas
df = df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

print(df.shape)
print(df.head())
print(df.columns)

# Verificando valores nulos
print(df.isnull().sum())

# Excluindo linhas nulas
df.dropna(inplace = True)
print(df.isnull().sum())

# Verificando se há registros duplicados
print(df.duplicated().sum())

# Processando o texto com AST

def converter(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name']) # Vai iterar o dicionário que iremos passar e identificar a chave "Name" e retornar os valores dessa chave-valor
    return L

# Aplicando função na coluna Genres
df['genres'] = df['genres'].apply(converter) # Agora ao invés de me retornar o dicionário, ele me retorna apenas uma lista com os gêneros dos filmes
print(df['genres'])

# Aplicando função na coluna Keywords
df['keywords'] = df['keywords'].apply(converter) 
print(df['keywords'])

# Extraindo os 3 membros do elenco

def converter_3(obj):

    L = []
    counter = 0

    for i in ast.literal_eval(obj):

        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

# Aplicando função na coluna cast
df['cast'] = df['cast'].apply(converter_3) 
print(df['cast'])

# Extraindo diretor do filme

def extrair_diretor(obj):

    L = []

    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

# Aplicando função na coluna crew
df['crew'] = df['crew'].apply(extrair_diretor) 
print(df['crew'])

# Limpeza dos dados de texto

# Separando a string da coluna overview por espaços em branco
df['overview'] = df['overview'].apply(lambda x:x.split())
print(df['overview'])

# Removendo espaços por vazio
df['genres'] = df['genres'].apply(lambda x:[i.replace(" ", "") for i in x])
df['keywords'] = df['keywords'].apply(lambda x:[i.replace(" ", "") for i in x])
df['cast'] = df['cast'].apply(lambda x:[i.replace(" ", "") for i in x])
df['crew'] = df['crew'].apply(lambda x:[i.replace(" ", "") for i in x])

print(df.head())

# Reduzindo a dimensionalidade
df['tags'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['crew']

df_final = df[['movie_id', 'title', 'tags']]
print(df_final.head())

# Join das strings
df_final['tags'] = df_final['tags'].apply(lambda x: " ".join(x))
df_final['tags'] = df_final['tags'].apply(lambda x:x.lower())

print(df_final.head())

# Parse e Vetorização
# Aplicaremos o stemming para simplificar o contexto, pegar os radicais das palavras, reduzindo a quantidade das palavras e o processamento

parse_ps = PorterStemmer()

def stem(text):
    y = []

    for i in text.split():
        y.append(parse_ps.stem(i))
    return " ".join(y)

# Aplicando a função na coluna tags
df_final['tags'] = df_final['tags'].apply(stem)
print(df_final['tags'])

# Vetorizador: convertendo texto em representação numérica
cv = CountVectorizer(max_features = 5000, stop_words = 'english') # Limitamos a 5000 palavras porque senão seria algo enorme, é verificado cada palavra para cada tag, por isso limitamos a 5000
vector = cv.fit_transform(df_final['tags']).toarray()
print(len(cv.get_feature_names_out()))

# Calculando distância de vetores
similaridade = cosine_similarity(vector) # Calculando a distância dos vetores a partir da distância de cosseno

# Aplicando sistema de recomendação

def sistema_recomendacao(movie):

    index = df_final[df_final['title'] == movie].index[0] # Pegando o filme que o usuário digitou e pegando seu respectivo index

    distancia = sorted(list(enumerate(similaridade[index])), reverse = True, key = lambda x: x[1]) # A partir do filme retorna os filmes com maior aproximidade do digitado

    # Pegando os 5 filmes mais similares ao digitado
    for i in distancia[1:6]:
        print(df_final.iloc[i[0]].title)


print(sistema_recomendacao('Avengers: Age of Ultron'))
print(sistema_recomendacao('Iron Man 2'))