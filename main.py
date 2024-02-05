import string

def readBookText(path):
    with open(path, 'r') as f:
        text = f.read()
        return text

def printLotsOText(text):
    for line in text:
        print(line, end='')

def letterCounter(someString, letterCount):
    splitString = list(someString.lower())
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        for char in splitString:
            if char == letter:
                if letter in letterCount:
                    letterCount[letter] += 1
                else:
                    letterCount[letter] = 1
        if letter not in letterCount:
            letterCount[letter] = 0
    return letterCount


def countWords(text):
    words = text.split()
    return len(words)
def main():
    book = "./books/frankenstein.txt"
    data = readBookText(book)
    letterCount = {}
    totalWords = countWords(data)
    letterCount = letterCounter(data, letterCount)

    for letter in letterCount:
        print(f"The count of this {letter}:\n {letterCount[letter]}\n")
    print(f"The length of letterCount is {len(letterCount)}")
    # printLotsOText(data)

main()
