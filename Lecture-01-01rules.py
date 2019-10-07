#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import random
'add = number + number'

def get_generation_by_gram(grammar_str: str, target, stmt_split='=',or_split='|'):
    rules = dict()
    for line in grammar_str.split('\n'):
        if not line: continue
        stmt,expr = line.split(stmt_split)
        rules[stmt.strip()] = expr.split(or_split)
    generated = generate(rules, target=target)
    #print(rules)
    return generated

def generate(grammar_rule, target):
    if target in grammar_rule: #names
        candidates = grammar_rule[target]
        candidate = random.choice(candidates)
        return ''.join(generate(grammar_rule,target=c.strip()) for c in candidate.split())
    else:
        return target

simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => Adj | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的"""

print(get_generation_by_gram(simple_grammar, target='sentence', stmt_split='=>'))