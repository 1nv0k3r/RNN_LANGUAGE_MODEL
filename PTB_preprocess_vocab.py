# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:35:36 2018

@author: acer
"""

import codecs
import collections
from operator import itemgetter

RAW_DATA = "./simple-examples/data/ptb.train.txt"
VOCAB_OUTPUT = "ptb.vocab"

#Frequency of words
counter = collections.Counter()
with codecs.open(RAW_DATA,"r","utf-8") as f:
    for line in f:
        for word in line.strip().split():
            counter[word] += 1

#sort words with frequency
sorted_word_to_cnt = sorted(counter.items(),key = itemgetter(1),reverse=True)
sorted_words = [x[0] for x in sorted_word_to_cnt]
sorted_words = ["<eos>"] + sorted_words

with codecs.open(VOCAB_OUTPUT,'w','utf-8') as file_output:
    for word in sorted_words:
        file_output.write(word + "\n")
        
        

