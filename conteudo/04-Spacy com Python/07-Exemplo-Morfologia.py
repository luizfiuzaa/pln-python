import spacy

# Carregando o modelo da língua portuguesa
nlp = spacy.load("pt_core_news_sm")

# Processando o texto
doc = nlp("Elas compraram laranjas. Eu vou comprar banana. Colocarei no carro.")

# Extraindo frases
print("\n classificação morfológica \n")
for token in doc:
    print(token.text, " --> ", token.morph)
    print("--------------------------------------")
    if token.morph.get("Gender") == ['Masc']:
        print("  Masculino \n")


