import stringdist

# Exercise One

# 1.1
A = "hello"

# 1.2
C = ["hello", "goodbye", "hola", "hello hellen", "helmet", "hellorheaven", "hillsboro", "say hello", "myfellow"]

# 1.3 part 1
def exact_match(string, arr):
    print(len([i for i in arr if i == string]))

#1.3 part 2
def non_exact_match(string, arr):
    print(len([i for i in arr if string in i]))

# 1.4
def intersection(string, arr):
    most_similar = ''
    current_res = ''
    result = ''
    
    for word in arr:
        for char in string:
            if char in word and not char in result:
                result += char
        if len(result) > len(current_res):
            current_res = result
            most_similar = word
        print(f"Term: {word} similarity: {result}")
        result = ''

    print(most_similar)

# 1.5
def improved_scheme(string, arr):
    most_similar = ''
    current_res = ''
    result = ''
    
    for word in arr:
        char_count = 0
        for char in string:
            if char_count > (len(word) - 1):
                break
            if char == word[char_count] and not char in result:
                result += char
            char_count += 1
        if len(result) > len(current_res):
            current_res = result
            most_similar = word
        print(f"Term: {word} similarity: {result}")
        result = ''

    print(most_similar)


# 2
def string_dist(string, arr):
    result = ''
    
    for word in arr:
        result = stringdist.levenshtein(string, word)
        print(f"Term: {word} similarity: {result}")
        result = ''


def main():
    exact_match(A, C)
    non_exact_match(A, C)
    intersection(string="goodfellow", arr=C)
    improved_scheme(string="goodfellow", arr=C)
    string_dist(string="goodfellow", arr=C)



if __name__ == "__main__":
    main()