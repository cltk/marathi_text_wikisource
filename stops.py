import nltk
import string
import re
from nltk.probability import FreqDist
from cltk.tokenize.indian_tokenizer import indian_punctuation_tokenize_regex as i_word
import os

path = "./datasets/dnyaneshwari/"
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
extra_punctuation = '||'
if os.path.isfile("./stop_words.txt"):
    os.remove("./stop_words.txt")
if os.path.isfile(path+"dnyaneshwari.txt"):
    os.remove(path+"dnyaneshwari.txt")
final = ""

for file_name in os.listdir(path):
    full_path = os.path.join(path, file_name)
    file_content = open(full_path).read()
    for char in file_content:
        if char not in punctuation + extra_punctuation:
            final = final + char
    i_words = i_word(final)
    f = open(path+"dnyaneshwari.txt", 'a+')
    word_string = '\n'.join(i_words)
    f.write(word_string)

with open(path + "dnyaneshwari.txt") as f1:
    dnyaneshwari_words = f1.read().splitlines()

os.remove(path+"dnyaneshwari.txt")
path = "./datasets/haripath/"

if os.path.isfile(path+"haripath.txt"):
    os.remove(path+"haripath.txt")
final = ""

for file_name in os.listdir(path):
    full_path = os.path.join(path, file_name)
    file_content = open(full_path).read()
    for char in file_content:
        if char not in punctuation + extra_punctuation:
            final = final + char
    i_words = i_word(final)
    f = open(path + "haripath.txt", 'a+')
    word_string = '\n'.join(i_words)
    f.write(word_string)

with open(path + "haripath.txt") as f1:
    haripath_words = f1.read().splitlines()

os.remove(path+"haripath.txt")
words = dnyaneshwari_words
words = words + haripath_words
fdist = FreqDist(words)
common_words = fdist.most_common(100)
f = open('/home/mahesh/Mahesh/marathi_text_wikisource/stops_words.txt', 'a+')
cw_list = [x[0] for x in common_words]
common_words = '\n'.join(cw_list)
print(common_words)
f. write(common_words)
