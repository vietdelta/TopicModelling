# -*- coding: utf-8 -*-
import os
import demoji
import re
from pyvi import ViTokenizer, ViPosTagger
from pyvi import ViUtils


import pandas as pd
import numpy
def nomolize(txt):
    line = u"""%s""" % txt
    line = demoji.replace(line)
    line = re.sub(r'[a-zA-Z0-9_\.]+@[a-zA-Z]+\.[a-zA-Z]+(\.[a-zA-Z]+)*', '', line) # remove email
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    line = emoji_pattern.sub(r'', line)
    line = re.sub(r'[http|https:\/\/]*[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/=]*)', '', line) #remove url
    line = re.sub(r'\#', ' ', line) # remove ".""
    line = re.sub(r'\d', ' ', line) # remove number like 2488
    line = re.sub(r'\.', ' ', line) # remove ".""
    line = re.sub(r'\"', ' ', line) # remove ".""
    line = re.sub(r'\|', ' ', line) # remove ".""
    line = re.sub(r'\?', ' ', line) # remove ".""
    line = re.sub(r'\!', ' ', line) # remove ".""
    line = re.sub(r'\(', ' ', line) # remove ".""
    line = re.sub(r'\)', ' ', line) # remove ".""
    line = re.sub(r'\]', ' ', line) # remove ".""
    line = re.sub(r'\[', ' ', line) # remove ".""
    line = re.sub(r'\:', ' ', line) # remove ".""
    line = re.sub(r'\,', ' ', line) # remove ".""
    line = re.sub(r'\;', ' ', line) # remove ".""
    

    line = re.sub(r'\–+|\/+', ' ', line) # remove chacracter like - or / 
    line = re.sub(r'\=+|\*+|\++|\-+', ' ', line) #remove = * + -*=
    line = re.sub(r'\s{2,}|\n{1,}', ' ', line) 
    

    return line

def is_non_zero_file(fpath):  
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

def remove_stop_words(line,stop_words,stop_words_no_accent):
    words = line.split()
    mid = 0
    line = ""
    for count,word in enumerate(words):
        word_no_accent = ViUtils.remove_accents(u""+word)
        left = 0
        right = len(stop_words)-1
        while(int((right-left)/2)>0):
            mid = int((right+left)/2)
            # print(word_no_accent,stop_words_no_accent[mid],(word_no_accent>stop_words_no_accent[mid]),left,right)
            if(word_no_accent>stop_words_no_accent[mid]):
                left = mid
            elif(word_no_accent<stop_words_no_accent[mid]):
                right = mid
            elif((word_no_accent==stop_words_no_accent[mid])):
                break
        if(word_no_accent != stop_words_no_accent[mid]):
            # print(word,stop_words[mid])
            line = line+word+" "
        else:
            if(mid>=3 and mid<=(len(stop_words)-4)):
                check = 0
                for i in range(mid-3,mid+3):
                    if(word==stop_words[i]):
                        check = 1
                        break
                if(check == 0):
                    line = line+word+" "
            elif(mid <=3):
                check = 0
                for i in range(0,mid+3):
                    if(word==stop_words[i]):
                        check = 1
                        break
                if(check == 0):
                    line = line+word+" "
            elif(mid >= (len(stop_words)-4)):
                check = 0
                for i in range(mid - 5,mid):
                    if(word==stop_words[i]):
                        check = 1
                        break
                if(check == 0):
                    line = line+word+" "
        # else:
        #     print(word)
    return line
def pre_comments(comments):
    comments_done = []
    for comment in comments:
        comment = str(comment)
        if("K" in comment):
            if("," in comment):
                comment = comment + "00"
            else:
                comment = comment + "000"
        comment = re.sub("[^0-9]", "", comment)
        if(comment==""):
            comment = "0"
        comments_done.append(comment)
    return comments_done

data_folder = "/home/vietphan/Downloads/fbcrawl/Data-Celeb-Nov/"
stop_words = []
stop_words_file = "/home/vietphan/Downloads/fbcrawl/stopwords.txt"
stop_words_no_accent = []
with open(stop_words_file, 'r') as f:
    print("Reading stop words")
    line = f.readline()
    while line:
        line = ViTokenizer.tokenize(u""+line)
        stop_words.append(line)
        stop_words_no_accent.append(ViUtils.remove_accents(u""+line))
        line = f.readline()


# print(stop_words)
count = 0
filename = data_folder+"model/"+"corpus.txt"
rating_file = data_folder+"model/"+"rating.txt"
source_file = data_folder+"model/"+"source.txt"
with open(filename, 'w') as f:
    with open(rating_file, 'w') as f2:
        with open(source_file, 'w') as f3:
            while(count<=2):
                print("Processing "+str(count))
                if is_non_zero_file(data_folder+str(count)+".csv"):
                    data = pd.read_csv(data_folder+str(count)+".csv",usecols=['text'])
                    reactions = pd.read_csv(data_folder+str(count)+".csv",usecols=['reactions'])
                    comments = pd.read_csv(data_folder+str(count)+".csv",usecols=['comments'])
                    source = pd.read_csv(data_folder+str(count)+".csv",usecols=['source'])
                    data = list(data.values.flatten())
                    reactions = list(reactions.values.flatten())
                    comments = list(comments.values.flatten())
                    source = list(source.values.flatten())
                    for sou in source:
                        sou = str(sou)
                        if (sou != "" and sou != "nan"):
                            source = sou
                            break
                    reactions_done = pre_comments(reactions)
                    comments_done = pre_comments(comments)
            # print(data)
                    source = str(source)
                    print(source)
                    # f.write("*doc"+str(count)+":"+str(source)+"\n")
                    # f2.write("*doc"+str(count)+":"+str(source)+"\n")
                    
                    for i, line in enumerate(data):
                        line = nomolize(line)
                        line = ViTokenizer.tokenize(u""+line)
                        # print("Normalizing...")
                        line = line.lower()
                        line = remove_stop_words(line,stop_words,stop_words_no_accent)
                        
                        # print(line+"\n")
                        if (len(line)>=20):
                            f.write(line)
                            f.write("\n")
                            # print(comments_done[i],reactions_done[i])                        
                            f2.write(str(numpy.int64(reactions_done[i])+3*numpy.int64(comments_done[i])))
                            f2.write("\n")
                    f3.write(source)
                    f3.write("\n")
                count = count + 1    
    
