
def sentimentAnalysis(filename):
    lexicon = '../Data/SA/wordWithStrength.txt'
    lexicon_dict = {}
    total_val = 0
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
                    total_val += lexicon_dict[word]
    
    
    print(total_val)
    

if __name__ == "__main__":
    filename = "../Data/SA/neg/00.txt"
    sent_score = sentimentAnalysis(filename)