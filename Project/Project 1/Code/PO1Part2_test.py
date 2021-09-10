import sentimentAnalysis
import os


def implementation_test():
    posFolder = '../Data/SA/pos'
    negFolder = '../Data/SA/neg'

    files = os.listdir(posFolder)

    for file in files:
        sent_score = sentimentAnalysis.sentimentAnalysis(f'{posFolder}/{file}')
        print(file)
        print(f'Groundtruth: Positive, sentiment score: {sent_score}')

    files = os.listdir(negFolder)

    for file in files:
        sent_score = sentimentAnalysis.sentimentAnalysis(f'{negFolder}/{file}')
        print(file)
        print(f'Groundtruth: Negative, sentiment score: {sent_score}')



if __name__ == "__main__":
    implementation_test()