import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ['The man who hunts ducks out on weekends.', 
    'The cotton clothing is made of grows in Mississippi.',
    'The horse raced past the barn fell.',
    'The man who whistles tunes pianos.',
    'The old man the boat.',
    'The complex houses married and single soldiers and their families.']


for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(i, i.label_,i.label) for i in doc.ents])

entity_gpe = spacy.explain("GPE")
print(f"GPE:{entity_gpe}")

# My program could only recognise one entity which is probably due to the use 
# of more common nouns than proper nouns in my chosen sentences.

# The meaning of the entity recognised made sense as 'Mississipi' is a state
# which is also shown by the GPE recognition.
