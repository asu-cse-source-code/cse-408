import sentimentAnalysis
import os


def implementation_test():
    posFolder = '../Data/SA/pos'
    negFolder = '../Data/SA/neg'

    files = os.listdir(posFolder)

    highest_file = ""
    lowest_file = ""
    highest_score = 0
    lowest_score = 0

    for file in files:
        sent_score = sentimentAnalysis.sentimentAnalysis(f'{posFolder}/{file}')
        print(file)
        print(f'Groundtruth: Positive, sentiment score: {sent_score}')
        if sent_score > highest_score:
            highest_score = sent_score
            highest_file = file

    files = os.listdir(negFolder)

    for file in files:
        sent_score = sentimentAnalysis.sentimentAnalysis(f'{negFolder}/{file}')
        print(file)
        print(f'Groundtruth: Negative, sentiment score: {sent_score}')
        if sent_score < lowest_score:
            lowest_score = sent_score
            lowest_file = file

    print(f'Highest file: {highest_file}')
    print(f'Lowest file: {lowest_file}')


if __name__ == "__main__":
    implementation_test()