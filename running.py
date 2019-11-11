import os
from sklearn.feature_extraction.text import CountVectorizer
import lda
import numpy as np
import pickle
import seaborn as sns

from matplotlib import pyplot as plt 

filename = "/home/vietphan/Downloads/fbcrawl/corpus.txt"
rating_file = "/home/vietphan/Downloads/fbcrawl/rating.txt"

corpus = []
page_id = []
doc_count = 0
rating = []
with open(filename, 'r') as f:
    line = f.readline()
    while(line):
        if(line[0]!="*"):
            corpus.append(line)
            # doc_count = doc_count +1
        line = f.readline()
with open(rating_file, 'r') as f2:
    line = f2.readline()
    while(line):
        if(line[0]=="*"):
            page_id.append(doc_count-len(page_id))
        else:
            rating.append(np.int64(line))
            doc_count = doc_count +1
        line = f2.readline()
print(page_id)
for i in range(len(page_id)-1):
    sum = 0
    for j in range(page_id[i],page_id[i+1]):
        sum = sum + rating[j]
        # print(j)
    for j in range(page_id[i],page_id[i+1]):
        rating[j] = rating[j]/sum

sum = 0
for j in range(page_id[-1],len(rating)):
    sum = sum + rating[j]
for j in range(page_id[-1],len(rating)):
    rating[j] = rating[j]/sum
print(rating)
# print(corpus)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
vocab = vectorizer.get_feature_names()
# print(vectorizer.get_feature_names())
# print(X.toarray())

model_filename = '/home/vietphan/Downloads/fbcrawl/finalized_model.sav'
model = pickle.load(open(model_filename, 'rb'))

page_vector = []
topic_word = model.topic_word_
doc_topic = model.doc_topic_
for i in range(len(page_id)-1):
    vector_temp = np.zeros((1, 20))
    for j in range(page_id[i],page_id[i+1]):
        vector_temp = vector_temp + rating[j]*doc_topic[j]
    page_vector.append(vector_temp)

vector_temp = np.zeros((1, 20))
for j in range(page_id[-1],len(rating)):
    vector_temp = vector_temp + rating[j]*doc_topic[j]
page_vector.append(vector_temp)

# print(page_vector)
sns.distplot(page_vector[5])


# print(type(topic_word))
# n_top_words = 10
# for i, topic_dist in enumerate(topic_word):
#     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
#     print('Topic {}: {}'.format(i, ' '.join(topic_words)))


# # for i in range(10):
# # 	print('Doc "{}"- Topic {}'.format(corpus[i], doc_topic[i].argmax()))
# # 	#print(doc_topic[i].argmax())
# for i, line in enumerate(corpus):
#     if(doc_topic[i].argmax()==7 and len(corpus[i])>=200):
#         print('Doc "{}"'.format(corpus[i]))
    