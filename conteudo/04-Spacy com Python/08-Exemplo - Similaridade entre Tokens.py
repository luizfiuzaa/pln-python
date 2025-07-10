import spacy

# Carregar o modelo de idioma
nlp = spacy.load("pt_core_news_sm")

# ----------------------------------
# 1- Processamento dos textos
# ----------------------------------
texto1 = "gato"
texto2 = "gata"
token1 = nlp(texto1)[0]
token2 = nlp(texto2)[0]

# Similaridade
similaridade = token1.similarity(token2)
print("\n\n\n Similaridade entre '{}' e '{}': {:.2f}".format(texto1, texto2, similaridade))

# ----------------------------------
# 2- Processamento dos textos
# ----------------------------------
texto3 = "gato"
texto4 = "rato"
token3 = nlp(texto3)[0]
token4 = nlp(texto4)[0]

# Similaridade
similaridade2 = token3.similarity(token4)
print("\nSimilaridade entre '{}' e '{}': {:.2f}".format(texto3, texto4, similaridade2))
print("\n\n\n\n\n FIM \n\n\n\n")