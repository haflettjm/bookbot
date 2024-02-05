import os

data_read = ""
with open('./books/frankenstein.txt', 'r') as f:
    data_read = f.read()
    f.close()

for line in data_read:
    print(line, end='')
