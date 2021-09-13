import numpy as np

def cse408_knn(test_feat_set, train_label, train_feat_set, k, DstType):
    ##print(train_feat_set)
    ##print("\n\n\n")
    ##print(test_feat_set)
    dist = []
    if DstType == 1: # SSD
        for train_feat in train_feat_set:
            SSD = set(train_feat) - set(test_feat_set)
            dist.append(sum(SSD))
    elif DstType == 2: # Angle Between Vectors
        # %PUT YOUR CODE HERE
        for train_feat in train_feat_set:
            unit_vector_1 = test_feat_set / np.linalg.norm(test_feat_set)
            unit_vector_2 = train_feat / np.linalg.norm(train_feat)
            dot_product = np.dot(unit_vector_1, unit_vector_2)
            dist.append(np.arccos(dot_product))
    elif DstType == 3: # Number of words in common
        # %PUT YOUR CODE HERE
        for train_feat in train_feat_set:
            count = 0
            for index in range(len(train_feat)):
                if train_feat[index] == test_feat_set[index] == 1:
                    count -= 1
            dist.append(count)
        ##print(dist)
    
    # sorted_d = sorted(dist.items(), key=lambda x: x[1])

    sorted_d = list(np.argsort(dist))
    #print(f'train_label:{len(train_label)}\train_feat_set:{len(train_feat_set)}\nk:{k}\n{sorted_d[k]}')

    posCt = 0
    negCt = 0

    while (k > 0):
        if train_label[sorted_d[k]] == 1:
            posCt = posCt + 1
        elif train_label[sorted_d[k]] == 0:
            negCt = negCt + 1
        k -= 1
    


    if posCt >= negCt:
        return 1
    else:
        return 0



if __name__ == "__main__":
    test_feat_set = {'one': 2, 'two': 2, 'three': 4}
    train_feat_set = {'one': 1, 'three': 2}
    # {'three': 6, 'one': 3}
    train_label = []
    k = 1
    DstType = 3
    pred_label = cse408_knn(test_feat_set, train_label, train_feat_set, k, DstType)
    