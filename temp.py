from pyvi import ViTokenizer, ViPosTagger
from pyvi import ViUtils
import nltk
from nltk.corpus import stopwords
stop_words = [] 
stop_words_file = "/home/vietphan/Downloads/fbcrawl/vietnamese-stopwords.txt"
stop_words_no_accent = []
with open(stop_words_file, 'r') as f:
    print("Reading stop words")
    line = f.readline()
    while line:
        line = ViTokenizer.tokenize(u""+line)
        stop_words.append(line)
        line = f.readline()

stop_words_english = set(stopwords.words('english'))
stop_words_english = list(stop_words_english)
for word in stop_words_english:
    stop_words.append(u""+word)

filename = "/home/vietphan/Downloads/fbcrawl/stopwords.txt"
with open(filename, 'w') as f:
    for line in stop_words:
            f.write(line)
            f.write("\n")