A = "hello"
B = "goodfellow"

C = ["hello", "goodbye", "hola", "hello hellen", "helmet", "hellorheaven", "hillsboro", "say hello", "myfellow"]


def getExactMatch(string, arr):
    print(len([i for i in arr if i == string]))

def getNonExactMatch(string, arr):
    print(len([i for i in arr if string in i]))

def getIntersection(string, arr):
    mostSimilar = ''
    currentRes = ''
    result = ''
    
    for word in arr:
        for char in string:
            if char in word and not char in result:
                result += char
        if len(result) > len(currentRes):
            currentRes = result
            mostSimilar = word
        result = ''

    print(mostSimilar)


def main():
    getExactMatch(A, C)
    getNonExactMatch(A, C)
    getIntersection(B, C)



if __name__ == "__main__":
    main()