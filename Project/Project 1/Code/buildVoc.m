% function to create a vocabulary from multiple text files under folders

function voc = buildVoc(folder, voc, finvoc)

stopword = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', ...
    'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', ...
    'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', ...
    'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', ...
    'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', ...
    'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', ...
    'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', ...
    'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', ...
    'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', ...
    'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', ...
    'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', ...
    'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', ...
    'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', ...
    'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', ...
    'further', 'was', 'here', 'than', ''}; % define English stop words, from NLTK



files = dir(fullfile(folder,'*.txt'));

for file = files'
    [fid, msg] = fopen(fullfile(folder,file.name), 'rt');
    error(msg);
    line = fgets(fid); % Get the first line from
     % the file.
    while line ~= -1

        %PUT YOUR IMPLEMENTATION HERE
    end
    fclose(fid);
    if finvoc
        n = 3; % count threshold -- here you can try 1, 2, 3, etc.
        
        %PUT YOUR IMPLEMENTATION HERE
        % this code is just to make your computation faster
        % Include code to drop words with low count, and make the voc an array
        % of unique words (use function "unique")
        % the first time you call buildvoc is with voc as and empty cell array
        % The second time you call it with voc from the first call:
        % voc = [];
        % voc = buildVoc('**path to neg data dir**', voc, 0)
        % voc = buildVoc('**path to pos data dir**', voc, 1)
        % notice the argument finvoc, is 0 the first time around,
        % 1 the second time to finish voc: make it unique and remove low count
        % words.
    end
end
