from buildVoc import buildVoc
from cse408_bow import cse408_bow
from cse408_knn import cse408_knn
import os

posFolder = '../Data/kNN/training/pos'
negFolder = '../Data/kNN/training/neg'

# build lexicon first for positive files and then add the lexicon for
# negative reviews
voc = []; #vocabulary is cell array of character vectors.
voc = buildVoc(posFolder,voc,0)
voc = buildVoc(negFolder,voc,1)
print(voc)


####################################################################
# Compute BOW feature vectors for training files

train_feat_set = []
train_label_set = []

# get the file list for positive reviews folder
files = os.listdir(posFolder)

# compute BOW feature vector for each file
for text_file in files:
    if text_file.__contains__('.txt'):
        train_label_set.append(1)
        #print(f'{posFolder}/{text_file}')
        feat_vec = cse408_bow(f'{posFolder}/{text_file}', voc)
        train_feat_set.append(feat_vec)

# get files for negative reviews
files = os.listdir(negFolder)

# compute BOW feature vector for each file
for text_file in files:
    if text_file.__contains__('.txt'):
        train_label_set.append(0)
        #print(f'{negFolder}/{text_file}')
        feat_vec = cse408_bow(f'{negFolder}/{text_file}', voc)
        train_feat_set.append(feat_vec)

####################################################################
# Compute BOW feature vectors for test files

test_feat_set = []
test_label_set = []

# get the file list for positive reviews folder
files = os.listdir(posFolder)

# compute BOW feature vector for each file
for text_file in files:
    if text_file.__contains__('.txt'):
        test_label_set.append(1)
        #print(f'{posFolder}/{text_file}')
        feat_vec = cse408_bow(f'{posFolder}/{text_file}', voc)
        test_feat_set.append(feat_vec)

# get files for negative reviews
files = os.listdir(negFolder)

# compute BOW feature vector for each file
for text_file in files:
    if text_file.__contains__('.txt'):
        test_label_set.append(0)
        #print(f'{negFolder}/{text_file}')
        feat_vec = cse408_bow(f'{negFolder}/{text_file}', voc)
        test_feat_set.append(feat_vec)

#####################################################################

#####################################################################
correct_ct = 0; # counter for correct classifications
DistType = 3; # test different distance type
K = 7; # test different K.

# Now we go over each test file to compute its label and check for
# correctness
for i in range(len(test_feat_set)):

    pred_label = cse408_knn(test_feat_set[i], train_label_set, train_feat_set, K, DistType)
    if pred_label == test_label_set[i]:
        correct_ct += 1
    print('Document ', i, ' groundtruth ', test_label_set[i], ' predicted as ', pred_label)
accuracy = correct_ct / len(test_label_set)
print(accuracy)