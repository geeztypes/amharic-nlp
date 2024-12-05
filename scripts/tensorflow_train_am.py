from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "ረሃቡ በምድሪቱ ላይ በርትቶ ነበር።",
    "ስለሆነም ከግብፅ ያመጡትን እህል በልተው ሲጨርሱ አባታቸው “ተመልሳችሁ ሂዱና ጥቂት እህል ግዙልን” አላቸው።",
    "በዚህ ጊዜ ይሁዳ እንዲህ አለው፦ “ሰውየው ‘ወንድማችሁን ይዛችሁት ካልመጣችሁ በምንም ዓይነት ዳግመኛ ፊቴን አታዩም’ በማለት በግልጽ አስጠንቅቆናል።",
    "ወንድማችንን ከእኛ ጋር የምትልከው ከሆነ ወደዚያ ወርደን እህል እንገዛልሃለን።"
]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

print(word_index)
print(sequences)