import spacy


print('\n\n---------- [ text  ] --------------------\n')
# Texto em portugues
nlp = spacy.load('pt_core_news_sm')
doc = nlp('Olá, meu nome é Marcos')

for token in doc:
    print(token.text)


print('\n\n FIM \n\n')

