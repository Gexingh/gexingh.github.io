#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
corpus = 'article_9k.txt'
FILE = open(corpus,encoding = 'UTF-8').read()
def generate_by_pro(text_corpus, length=20):
    return ''.join(random.sample(text_corpus,length))
import jieba

max_length = 1000000
sub_file = FILE[:max_length]
def cut(string):
    return list(jieba.cut(string))
TOKENS = cut(sub_file)
from collections import Counter

words_count = Counter(TOKENS)
words_count.most_common(10)
words_with_fre = [f for w,f in words_count.most_common()]
import matplotlib.pyplot as plt
import numpy as np

_2_gram_words = [
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]
_3_gram_words = [
    TOKENS[i] + TOKENS[i+1] + TOKENS[i+2] for i in range(len(TOKENS)-2)
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
    probability = 1
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]

        _two_gram_c = get_gram_count(word + next_word,_2_gram_word_counts)
        _one_gram_c = get_gram_count(next_word, words_count)
        pro = _two_gram_c / _one_gram_c

        probability *= pro

    return probability



print(two_gram_model('这个人来自清华大学'))
#2.102784086130036e-06