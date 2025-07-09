import spacy

# Texto em Ingles
nlp = spacy.load('en_core_web_sm')
doc = nlp('Hello, my name is Marcos')

print('\n\n-------- [ POS - Inglês ] ----------------------\n')
for token in doc:
    print(token.text,'-->', token.pos_)


print('\n\n---------- [ POS - Português ] --------------------\n')
# Texto em portugues
nlp = spacy.load('pt_core_news_sm')
doc = nlp('Olá, meu nome é Marcos')

for token in doc:
    print(token.text, '-->', token.pos_)


print('\n\n FIM \n\n')

