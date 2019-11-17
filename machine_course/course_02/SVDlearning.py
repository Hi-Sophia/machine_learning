import numpy as np
import re
import math

# df = np.mat(np.array([[1, 1], [1, 7]]))
# U,sigma,VT = np.linalg.svd(df)
#
# print(U)
# print(sigma)
# print(VT)


documents = []
# 要去除的标点符号的正则表达式
punctuation_regex = '[,.;"]+'

# 停用词
stopwords = ['a', 'an', 'after', 'also', 'and', 'as', 'be', 'being', 'but', 'by', 'd', 'for', 'from', 'he', 'her',
             'his', 'in', 'is', 'more', 'of', 'often', 'the', 'to', 'who', 'with', 'people']

with open("/Users/wujuhong/PycharmProjects/code/machine_learning/machine_course/course_02/textSVD.txt", "r") as f:
    for line in f:
        documents.append(line)

docs_total = len(documents)

doc_word_num = {}  # 单个文档中的单词总数
doc_total_word = {}  # 统计单个文档中每个单词出现的次数
doc_coll_word = set()  # 文档集中的所有单词
docId = 0;  # 文档编号

for doc in documents:
    total_word = 0
    dictionary = {}
    doc_words = doc.split(" ")
    for word in doc_words:
        word = re.sub(punctuation_regex, '', word.lower())
        if word in stopwords:
            continue
        total_word += 1
        doc_coll_word.add(word)
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    doc_total_word[docId] = total_word
    doc_word_num[docId] = dictionary
    docId += 1
print(doc_total_word)
print(doc_word_num)
print(doc_coll_word)

TF = {}


def computeTF(doc_total_word, doc_word_num):
    for key, value_dic in doc_word_num.items():
        dic = {}
        total = doc_total_word[key]
        for word, num in value_dic.items():
            dic[word] = float(num / total)
        TF[key] = dic
    return TF


def computeIDF(doc_coll_word, doc_word_num):
    word_doc_num = {}
    for coll_word in doc_coll_word:
        for key, value_dic in doc_word_num.items():

            if coll_word in value_dic:
                if coll_word in word_doc_num:
                    word_doc_num[coll_word] += 1
                else:
                    word_doc_num[coll_word] = 1
    IDF = {}
    for key, value in word_doc_num.items():
        IDF[key] = math.log2(docs_total / value + 1)
    return IDF


def computeTFIDF(TF, IDF):
    tfidf = {}
    for docId, doc in TF.items():
        doc_tfidf = {}
        for word, tfval in doc.items():
            doc_tfidf[word] = tfval * IDF[word]
        tfidf[docId] = doc_tfidf
    return tfidf


print(computeTF(doc_total_word, doc_word_num))
print(computeIDF(doc_coll_word, doc_word_num))

TF = computeTF(doc_total_word, doc_word_num)
IDF = computeIDF(doc_coll_word, doc_word_num)
print(computeTFIDF(TF,IDF))


