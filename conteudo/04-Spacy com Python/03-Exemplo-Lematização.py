import spacy

# Carregar o modelo de idioma
nlp = spacy.load("pt_core_news_sm")

# Processamento do texto
texto = "Eles estão estudando pouco, mas ontem estudaram muitos."
doc = nlp(texto)

# Lematização
for token in doc:
    # print(token.text, token.lemma_)
    print(f"{token.text:15} -> {token.lemma_}")