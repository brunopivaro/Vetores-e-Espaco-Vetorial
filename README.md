# Vetores, Espaço Vetorial e Sistema de Recomendação de Filmes

Este repositório contém anotações teóricas sobre **Vetores e Espaço Vetorial aplicados a Data Science** e o desenvolvimento prático de um **Sistema de Recomendação de Filmes baseado em Similaridade de Cosseno**.

---

## 📚 Conteúdo Teórico

### Vetores e Espaço Vetorial em Data Science
Anotações e conceitos fundamentais sobre:
- Representação vetorial de dados (embeddings e matrizes de termos).
- Espaço vetorial e dimensões.
- Métricas de distância e angularidade (Distância de Cosseno, Distância Euclidiana).

---

## 🎬 Projeto 01: Sistema de Recomendação de Filmes

### 📌 Visão Geral
O objetivo deste projeto é construir um motor de recomendação no qual o usuário informa o nome de um filme e o sistema retorna os **5 filmes mais semelhantes**.

### 🛠️ Etapas do Projeto & Pipeline de Dados

1. **Carga e Fusão dos Datasets:**
   - Integração das bases de dados de **Filmes** e **Elenco/Equipe**.

2. **Tratamento e Limpeza de Dados:**
   - Remoção de valores nulos e duplicados.
   - Parsing de strings estruturadas utilizando o módulo `ast` (`ast.literal_eval`) para extrair palavras-chave, gêneros, elenco e diretores.

3. **Processamento de Linguagem Natural (PLN):**
   - **Stemming:** Aplicação de stemming para reduzir as palavras ao seu radical, simplificando o contexto textual e otimizando o processamento computacional.

4. **Vetorização e Cálculo de Similaridade:**
   - **Vetorização:** Conversão dos textos processados em vetores numéricos (ex: *CountVectorizer* / *TF-IDF*).
   - **Distância de Cosseno:** Cálculo do ângulo entre os vetores no espaço vetorial para medir a similaridade entre os filmes e ranquear os 5 mais próximos.