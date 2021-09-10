
def sentimentAnalysis(filename):
    lexicon = '../Data/SA/wordWithStrength.txt'
    lexicon_dict = {}
    sent_score = 0
    with open(filename, 'r') as file, open(lexicon, 'r') as lexicon_file:
        for line in lexicon_file:
            line = line.strip()
            line_split = line.split('\t')

            if len(line_split) > 1:
                lexicon_dict[line_split[0]] = float(line_split[1])

        # print(lexicon_dict)

        for line in file:
            text_data = line.lower()
            words = text_data.split()
            for word in words:
                if word in lexicon_dict:
                    # print(word)
                    sent_score += lexicon_dict[word]
    
    return sent_score
    

if __name__ == "__main__":
    filename = "../Data/SA/neg/00.txt"

    sent_score = sentimentAnalysis(filename)
    
    if sent_score > 0:
        if sent_score > 0.7:
            print(f'File {filename} \n Sentiment Score: {sent_score:.2f} Highly Positive Sentiment\n',filename,sent_score)
        else:
            print(f'File {filename} \n Sentiment Score: {sent_score:.2f} Positive Sentiment\n',filename,sent_score)

    if sent_score < 0:
        if sent_score < -0.7:
            print(f'File {filename} \n Sentiment Score: {sent_score:.2f} Highly Negative Sentiment\n',filename,sent_score)
        else:
            print(f'File {filename} \n Sentiment Score: {sent_score:.2f} Negative Sentiment\n',filename,sent_score)

    if sent_score == 0:
        print(f'File {filename} \n Sentiment Score: {sent_score:.2f} Neutral Sentiment\n',filename,sent_score)