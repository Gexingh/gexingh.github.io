#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
hello_to_someone = '''
say_hello = name hello tail
name = Jhon | Mike | 老梁 | 老刘
hello = 你好 | 您来啦 | 快请进
tail = 呀 | !
'''
def name():
    return random.choice('Jhon | Mike | 老梁 | 老刘 '.split('|'))
def hello():
    return random.choice('你好 | 您来啦 | 快请进'.split('|'))
def say_hello():
    return name() + ' ' + hello()
print(say_hello())