% function to run KNN classification


function pred_label = cse408_knn(test_feat_set, train_label, train_feat_set, k, DstType)


if DstType == 1 %SSD
    for i = 1:size(train_feat_set,2)

        %get the difference of train and test feat sets

        setX = train_feat_set(:,i) - test_feat_set;

        %find distance

        dist(i) = sum(setX(:).^2);

    end
elseif DstType == 2 %Angle Between Vectors
    for i = 1:size(train_feat_set,2)

        %store row of train feat set to setX

        setX = train_feat_set(:,i);

        %store row of test feat set to setY

        setY = test_feat_set;

        CosTheta = dot(setX,setY)/(norm(setX)norm(setY));

        ThetaInDegrees = acosd(CosTheta);

        %find distance

        dist(i) = ThetaInDegrees;

    end
elseif DstType == 3 %Number of words in common
    %PUT YOUR CODE HERE 
    dist = -dist; % Why minus?
end



%Find the top k nearest neighbors, and do the voting. 

[B,I] = sort(dist);

posCt=0;
negCt=0;
for ii = 1:k
    if train_label(I(ii)) == 1
        posCt = posCt + 1;
    elseif train_label(I(ii)) == 0
        negCt = negCt + 1;
    end    
end

if posCt >= negCt
    pred_label = 1;
else
    pred_label = 0;
end