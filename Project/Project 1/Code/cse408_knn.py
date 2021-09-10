import numpy as np

def cse408_knn(test_feat_set, train_label, train_feat_set, k, DstType):
    print(train_feat_set)
    print("\n\n\n")
    print(test_feat_set)
    dist = {}
    if DstType == 1: # SSD
        dist = np.sum((train_feat_set[:,:,0:3]-test_feat_set[:,:,0:3])**2)
    elif DstType == 2: # Angle Between Vectors
        # %PUT YOUR CODE HERE
        unit_vector_1 = test_feat_set / np.linalg.norm(test_feat_set)
        unit_vector_2 = train_feat_set / np.linalg.norm(train_feat_set)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        dist = np.arccos(dot_product)
    elif DstType == 3: # Number of words in common
        # %PUT YOUR CODE HERE
        dist = {k: test_feat_set.get(k, 0) + train_feat_set.get(k, 0) for k in set(test_feat_set) & set(train_feat_set)}
        print(dist)
    
    # sorted_d = sorted(dist.items(), key=lambda x: x[1])

    # sorted_d = np.argsort(dist)
    # print(sorted_d)

    posCt = 0
    negCt = 0

    # while (k > 0):
    #     if train_label[I[k]] == 1:
    #         posCt = posCt + 1
    #     elif train_label[I[k]] == 0:
    #         negCt = negCt + 1
    #     k -= 1
    


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
    