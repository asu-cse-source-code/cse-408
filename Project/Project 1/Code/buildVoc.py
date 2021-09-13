from collections import Counter
import string
import os
import re

stopword = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', \
    'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', \
    'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', \
    'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', \
    'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', \
    'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', \
    'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', \
    'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', \
    'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', \
    'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', \
    'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', \
    'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', \
    'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', \
    'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', \
    'further', 'was', 'here', 'than', ''}

def buildVoc(folder, voc, finvoc):
#read all files from folder

    all_files = os.listdir(folder)
    file_type = '.txt'
    text_data = ''
    
    for text_file in all_files:
        if text_file.__contains__(file_type):
            with open(f'{folder}/{text_file}') as data:
                text_data += data.read()

    text_data = text_data.lower()
    cleaned = re.sub(r'[^\w\s]', '', text_data).replace('\n', '')
    cleaned = [word for word in cleaned.split() if word not in stopword]
    cleaned += voc
    counts = Counter(cleaned)

    if finvoc:
        prune_val = 50
        pruned = {word:count for word, count in counts.items() if count > prune_val}
        for item, val in pruned.items():
            #print(f'{item}:{val}')
            pass
        return list(pruned)
    else:
        pass
        return list(counts.keys())

if __name__ == "__main__":
    voc = []
    voc = buildVoc('../Data/kNN/training/neg', voc, 0)
    # voc = buildVoc('../Data/kNN/training/pos', voc, 1)
    print(voc)