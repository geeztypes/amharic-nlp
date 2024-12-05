import json
import io


sentence = r'ፍልስፍና ከግሪኩ φιλοσοφία (ፊሎዞፊያ) የመጣ ሲሆን ትርጉሙም የጥበብ ፍቅር ነው። ስለዚህ የፍልስፍና ዕውቀት ሁለት ነገሮችን መነሻ ያደረጋል። አንደኛው፣ «ጥበብ አለ» የሚል ሲሆን፣ ሁለተኛው «ይህ ጥበብ ሊደረስበት ይቻላል» የሚል ነው።'
sentence_phonetic = ''

f = open('.\\resources\\geez_syllables.json', mode="r", encoding="utf-8")

# returns JSON object as 
# a dictionary
data = json.load(f)

for letter in sentence:
    # Iterating through the json
    # list
    for i in data['geez']:
        if i['syllable'] == letter and i['syllable_grouping'] != "punctuation":
            sentence = sentence.replace(letter, i['syllable_phonetic'].lower())



print(sentence)

# Closing file
f.close()