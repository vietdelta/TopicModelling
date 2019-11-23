# -*- coding: utf-8 -*-
import os
from sklearn.feature_extraction.text import CountVectorizer
import lda
import numpy as np
import pickle
filename = "/home/vietphan/Downloads/fbcrawl/corpus.txt"
corpus = []
page_id = []
doc_count = 0
with open(filename, 'r') as f:
    line = f.readline()
    while(line):
        if(line[0]=="*"):
            page_id.append(doc_count)
        else:
            corpus.append(line)
            doc_count = doc_count +1
        line = f.readline()
# print(corpus)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
vocab = vectorizer.get_feature_names()
# print(vectorizer.get_feature_names())

model = lda.LDA(n_topics=20, n_iter=2500, random_state=1)
model.fit(X)
print("Saving model....")
model_filename = 'finalized_model.sav'
pickle.dump(model, open(model_filename, 'wb'))
print("Model saved")


