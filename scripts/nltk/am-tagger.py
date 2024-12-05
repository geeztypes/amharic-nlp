import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#from nltk.tokenize import sent_tokenize


import nltk.data 
  
#nltk.data.load('./corpora/am-bible/amharic.txt', format ='raw')

from nltk.tokenize import sent_tokenize, word_tokenize
txt1 = """የቶኪዮ ግንብ 333 ሜትር ከፍታ አለው።"""
am_st = sent_tokenize(txt1)
am_wt = word_tokenize(sent_tokenize(txt1)[0])
raw_wt = word_tokenize(txt1)

post_tag = nltk.pos_tag(am_wt)
print(post_tag)

# CC = a coordinating conjunction; RB = adverbs; IN = preposition; 
# NN = noun; JJ = adjective.