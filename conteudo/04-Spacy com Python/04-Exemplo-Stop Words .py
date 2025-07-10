import spacy

# Carregar o modelo de idioma
nlp = spacy.load("pt_core_news_sm")

# Processamento do texto
texto = "O spaCy é uma biblioteca de processamento de linguagem natural em Python, ela bem é bem utilizada, mas existem outras."
doc = nlp(texto)

print("\n\n ----------------------------------------------------------\n\n")

# Remoção de Stop Words
tokens_sem_stop_words = [token.text for token in doc if not token.is_stop]
print("Texto sem stop words\n",tokens_sem_stop_words)