from buildVoc import buildVoc
import os
import re

def cse408_bow(filepath, voc):
    # text_data = scan_folder(filepath)
    feat_vec = []
    text_data = ''
    with open(filepath, 'r') as file:
        text_data = file.read()
        text_data = text_data.lower()
        text_data = re.sub(r'[^\w\s]', '', text_data).replace('\n', '')
        text_data += ' '
    for word in voc:
        feat_vec.append(text_data.count(word + " "))
    #print(text_data.split())
    return feat_vec

if __name__ == "__main__":
    print(cse408_bow('../Data/kNN/testing/neg/cv002_17424.txt', buildVoc('../Data/kNN/training/pos', [], 1)))