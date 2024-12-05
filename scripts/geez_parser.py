import json
import io


sentence = r'ተጻብኦታት ኬጋጥመና ኸሎ፡ ኣብ የሆዋን ኣብ ውድቡን ዘሎና ተኣማንነት ኪፍተን ይኽእል እዩ።'
sentence_phonetic = ''

f = open('geez_syllables.json', mode="r", encoding="utf-8")

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