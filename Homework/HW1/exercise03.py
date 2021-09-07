import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "review-1.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# 3.1
# Using regex
import re

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
cell_array = []
def read_input():
    with open(abs_file_path, 'r') as input_file:
        for line in input_file:
            lowered_line = line.lower()
            # no_new_line = lowered_line.rstrip()
            removed_punctuation = re.sub(r'[^\w\s]', '', lowered_line)
            removed_stop_words = [word for word in removed_punctuation.split() if word not in stop_words]
            # removed_stop_words = ' '.join(removed_stop_words)
            cell_array.append(removed_stop_words)

    # print(cell_array)

    #3.4
    lexicon_array = set()
    for line in cell_array:
        for word in line:
            lexicon_array.add(word)

    # print(lexicon_array)

    #3.5
    column_vector = dict()
    for word in lexicon_array:
        column_vector[word] = 0
    
    for line in cell_array:
        for word in line:
            column_vector[word] += 1
    # print(column_vector)
    for item, val in column_vector.items():
        print(f"Term: {item} Value: {val}")

    compressed_dict = dict()

    for item, val in column_vector.items():
        if val > 1:
            compressed_dict[item] = val

    print(compressed_dict)


def main():
    read_input()


if __name__ == "__main__":
    main()