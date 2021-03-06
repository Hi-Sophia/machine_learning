import numpy as np
import re
import math

documents = []
# 要去除的标点符号的正则表达式
punctuation_regex = '[,.;"]+'

# 停用词
stopwords = ['a', 'an', 'after', 'also', 'and', 'as', 'be', 'being', 'but', 'by', 'd', 'for', 'from', 'he', 'her',
             'his', 'in', 'is', 'more', 'of', 'often', 'the', 'to', 'who', 'with', 'people', '']

with open("textSVD.txt", "r") as f:
    for line in f:
        documents.append(line.strip("\n"))

doc_set_word = {}  # 除去去标点符号，停用词，每个文档中的单词
doc_list = []  # 文档集中的所有单词
docId = 0;  # 文档编号

for doc in documents:
    doc_word_list = []
    doc_words = doc.split(" ")
    for word in doc_words:
        word = re.sub(punctuation_regex, '', word.lower())
        if word in stopwords:
            continue
        doc_word_list.append(word)

    doc_set_word[docId] = doc_word_list
    doc_list.extend(doc_word_list)
    docId += 1

print(doc_set_word)
print(len(doc_list))


def computeTF(doc_set_word):
    tfdict = {}
    for key, doc in doc_set_word.items():
        doc_len = len(doc) #文档总词数
        word_count = dict.fromkeys(set(doc), 0)
        # 统计每个词在文档中出现的次数
        for word in doc:
            word_count[word] += 1

        print("doc：{} word count：{}".format(key, word_count))

        for word, count in word_count.items():
            word_count[word] = float(count / doc_len)

        tfdict[key] = word_count
    return tfdict


def computeIDF(doc_set_word, doc_list):
    idfdict = dict.fromkeys(set(doc_list), 0)
    docs_total = len(doc_set_word)  # 语料库中的文档总数

    #统计包含每个词的文档数
    for key, doc in doc_set_word.items():
        for word in set(doc):
            idfdict[word] += 1

    for word, word_doc_count in idfdict.items():
        idfdict[word] = math.log10(docs_total / (word_doc_count + 1))

    return idfdict


def computeTFIDF(tf, idfs):
    tfidf = {}
    for docId, doc in tf.items():
        doc_tfidf = {}
        for word, tfval in doc.items():
            doc_tfidf[word] = tfval * idfs[word]
        tfidf[docId] = doc_tfidf
    return tfidf


tf = computeTF(doc_set_word)
print("tf")
print(tf)

idfs = computeIDF(doc_set_word, doc_list)
print("idfs")
print(idfs)

tfidfs = computeTFIDF(tf, idfs)
print("tf-idfs")
print(tfidfs)
