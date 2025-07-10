import spacy

# Carregar o modelo de idioma
nlp = spacy.load("en_core_web_sm")

# Processamento do texto
texto = "O spaCy é uma biblioteca de processamento de linguagem natural em Python. É útil para análise de texto."
doc = nlp(texto)

# Extraindo frases
for sent in doc.sents:
    print(sent.text)