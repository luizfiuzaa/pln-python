import spacy

# Carregando o modelo da língua portuguesa
nlp = spacy.load("pt_core_news_sm")

# Processando o texto
doc = nlp("Paulo, A Fatec é uma faculdade localizada em Tatuí, estado de São Paulo  e California. Ela tem parceria com a Microsoft e Google e Bradesco.")
#doc = nlp("o campeonato mundial será em 2026")

# Iterando sobre as entidades nomeadas e imprimindo informações sobre elas
for ent in doc.ents:
    print(ent.text,'-->', ent.label_)
    print(str(spacy.explain(ent.label_)))
    print("\n ------------------------------------------ \n")

