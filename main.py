import os
import spacy

def tokenization(text):
  file.write("=== TOKENIZAÇÃO ===\n")
  for token in nlp(text):
    file.write(token.text + " ")
  file.write("\n")

def pos_tagging(text):
  file.write("=== POS (Part-of-Speech Tagging) ===\n")
  for token in nlp(text):
    file.write(f'{token.text:15} -> {token.pos_}\n')
  file.write("\n")

def lemmatization(text):
  file.write("=== LEMMATIZAÇÃO ===\n")
  for token in nlp(text):
    file.write(f"{token.text:15} -> {token.lemma_}\n")
  file.write("\n")

def stop_words(text):
  file.write("=== STOP WORDS ===\n")
  stop_words = [token.text for token in nlp(text) if token.is_stop]
  for word in stop_words:
    file.write(word + " ")
  file.write("\n")

def ner(text):
  file.write("=== ENTIDADES NOMEADAS (NER) ===\n")
  for ent in nlp(text).ents:
    file.write(f"{ent.text:15} -> {ent.label_}\n")
  file.write("\n")

def sentence_segmentation(text):
  file.write("=== SEGMENTAÇÃO DE SENTENÇAS ===\n")
  for sent in nlp(text).sents:
    file.write(sent.text)
  file.write("\n")

def morphology(text):
  file.write("=== MORFOLOGIA ===\n")
  for token in nlp(text):
    file.write(f"{token.text:15} -> {token.morph}\n")
  file.write("\n")

def similarity(text):
    file.write("=== SIMILARIDADE ENTRE TOKENS ===\n")
    doc = nlp(text)
    tokens = [token.text for token in doc]
    print("Tokens disponíveis:", tokens)
    while True:
        palavra1 = input("Digite a primeira palavra do texto para comparar ('sair' para encerrar): ")
        if palavra1.lower() == 'sair':
            break
        palavra2 = input("Digite a segunda palavra do texto para comparar ('sair' para encerrar): ")
        if palavra2.lower() == 'sair':
            break

        token1 = None
        token2 = None
        for token in doc:
            if token.text == palavra1:
                token1 = token
            if token.text == palavra2:
                token2 = token

        if not token1 or not token2:
            print("Uma ou ambas as palavras não foram encontradas no texto.")
            continue
        
        file.write(f"Palavras Comparadas '{token1.text}' e '{token2.text}'\n")
        file.write(f"Similaridade: {token1.similarity(token2):.4f}\n")
        file.write("\n")
        break
      

data = ""
nlp = spacy.load('pt_core_news_sm')
with open('./input/input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    data = text
    
pln_funcs = [
  tokenization,
  pos_tagging,
  lemmatization,
  stop_words,
  ner,
  sentence_segmentation,
  morphology, 
  similarity,
]

os.makedirs('./output', exist_ok=True)
with open('./output/output.txt', 'w', encoding='utf-8') as file:
    for func in pln_funcs:
      func(data)
      file.write("\n")


