import spacy 
from spacy import displacy
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_sm")

def subtree_matcher(doc):
  subjpass = 0

  for i,tok in enumerate(doc):
    # find dependency tag that contains the text "subjpass"    
    if tok.dep_.find("subjpass") == True:
      subjpass = 1

  x = ''
  y = ''

  # if subjpass == 1 then sentence is passive
  if subjpass == 1:
    for i,tok in enumerate(doc):
      if tok.dep_.find("subjpass") == True:
        y = tok.text

      if tok.dep_.endswith("obj") == True:
        x = tok.text
  
  # if subjpass == 0 then sentence is not passive
  else:
    for i,tok in enumerate(doc):
      if tok.dep_.endswith("subj") == True:
        x = tok.text

      if tok.dep_.endswith("obj") == True:
        y = tok.text

  return x,y

def match_this(doc):
    p1 = [{'POS':'PROPN'},
          {"POS": "ADJ", "OP": "?"},
          {"POS": "ADV", "OP": "?"},
          {"POS": "AUX", "OP": "?"},
          {'POS': 'VERB'}, 
          {'POS': 'PROPN'}]
    p2 = [{'POS':'PROPN'}, 
          {"POS": "ADJ", "OP": "?"},
          {"POS": "ADV", "OP": "?"},
          {"POS": "AUX", "OP": "?"},
          {'POS': 'VERB'}, 
          {'POS': 'NOUN'}]
    p3 = [{'POS':'PROPN'}, 
          {"LOWER": "is"},
          {"LOWER": "about"},
          {"LOWER": "to"},
          {'POS': 'VERB'}, 
          {'POS': 'NOUN'}]
    p4 = [{'POS':'NOUN'}, 
          {"LOWER": "is"},
          {"LOWER": "about"},
          {"LOWER": "to"},
          {'POS': 'VERB'}, 
          {'POS': 'PROPN'}]
    # Matcher class object 
    matcher = Matcher(nlp.vocab) 
    matcher.add("matching_1", [p1, p2, p3, p4]) 

    matches = matcher(doc) 
    if (len(matches) > 0):
        span = doc[matches[0][1]:matches[0][2]] 
        print(span.text)

def proccess_sentence(sentence):
    doc = nlp(sentence) 
    # displacy.serve(doc, style='ent')
    # displacy.serve(doc, style='dep')
    # print(subtree_matcher(doc))
    match_this(doc)
    for tok in doc: 
        print(tok.text, "-->",tok.dep_,"-->", tok.pos_)