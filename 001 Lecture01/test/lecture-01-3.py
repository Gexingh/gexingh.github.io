#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
corpus = 'train.txt'
FILE = open(corpus,encoding = 'UTF-8').read()
FILE2 = open('temp_write.txt', 'w' , encoding = 'UTF-8')

n_line = 0
rules = dict()
for line in FILE.split('\n'):
    if not line: continue
    #0 ++$++ disability-insurance ++$++ 法律要求残疾保险吗？ ++$++ Is Disability Insurance Required By Law?
    # 序号 类型 中文问题 英文问题
    stmt,expr0,expr1,expr2 = line.split(' ++$++ ')
    rules[stmt.strip()] = [expr0, expr1, expr2]
    FILE2.write(expr1)
    n_line = n_line + 1
FILE2.close()
FILE2 = open('temp_write.txt',encoding = 'UTF-8').read()
#print(rules)

def generate_by_pro(text_corpus, length=20):
    return ''.join(random.sample(text_corpus,length))

import jieba

def cut(string):
    return list(jieba.cut(string))
TOKENS = cut(FILE2)
from collections import Counter

words_count = Counter(TOKENS)
words_count.most_common(10)

words_with_fre = [f for w,f in words_count.most_common()]
import numpy as np

_2_gram_words = [
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]
_2_gram_word_counts = Counter(_2_gram_words)

def get_1_gram_count(word):
    if word in words_count: return words_count[word]
    else:
        return words_count.most_common()[-1][-1]
def get_2_gram_count(word):
    if word in _2_gram_word_counts: return _2_gram_word_counts[word]
    else:
        return _2_gram_word_counts.most_common()[-1][-1]
def get_gram_count(word, wc):
    if word in wc:return wc[word]
    else:
        return wc.most_common()[-1][-1]

def two_gram_model(sentence):
    tokens = cut(sentence)
    #print(tokens)
    probability = 1
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]

        _two_gram_c = get_gram_count(word + next_word,_2_gram_word_counts)
        _one_gram_c = get_gram_count(next_word, words_count)
        pro = _two_gram_c / _one_gram_c

        probability *= pro

    return probability

#print(two_gram_model('什么是关键人寿保险？'))
#6.856268842094055e-06

ans = []
for i in range(10) :
    r = str(random.randint(0,n_line))
    ans.append((r,two_gram_model(rules[r][1])))
    print(r,rules[r][1], two_gram_model(rules[r][1]))
ans2 = []
ans2 = sorted(ans , key=lambda x:x[1], reverse=True)
print("\n随机的10项中最合理句子为：")
print("序号：",ans2[0][0])
print("中文：",rules[ans2[0][0]][1])
print("合理度：",ans2[0][1])


