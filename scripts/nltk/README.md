https://github.com/MarsPanther/Amharic-English-Machine-Translation-Corpus

https://www.researchgate.net/profile/Girma-Demeke/publication/237553785_Manual_Annotation_of_Amharic_News_Items_with_Part-of-Speech_Tags_and_its_Challenges/links/57045f2308ae74a08e246382/Manual-Annotation-of-Amharic-News-Items-with-Part-of-Speech-Tags-and-its-Challenges.pdf

CRF
MBT
CNN-BiLSTM-CRF

Therefore, there should be a way to automatically produce training data as the best solution.

However, using machine-labelled data merely does not guarantee to development of a competent model due to automated tagging errors.

morphologically complex languages, like Amharic

1. Find corpus of data in your language or create one
2. Create a tagged corpus from corpus data from #1
3. Rrain the NLTK tagger on that tagged corpus
