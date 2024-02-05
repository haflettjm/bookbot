import os

def readBookText(path):
    with open(path, 'r') as f:
        text = f.read()
        return text

def printLotsOText(text):
    for line in text:
        print(line, end='')

def main():
    book = "./books/frankenstein.txt"
    data = readBookText(book)
    printLotsOText(data)

main()
