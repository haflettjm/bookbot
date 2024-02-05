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
    print(f"--- Begin Report of {book} ---")
    print(f"==== Will return the count of words and the count of characters (sorted by largest to least).===")
    sortedLetterCount = dict(sorted(letterCount.items(), key=lambda item: item[1], reverse=True))
    print(f"There were {totalWords} found in the text file.")
    for letter in sortedLetterCount:
        print(f"The count of this {letter}: {sortedLetterCount[letter]}")
    # printLotsOText(data)

main()
