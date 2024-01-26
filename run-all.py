# Made with ❤️ by Garry
# 26/01/24

import time, csv

from linear_search import linear_search_src
from binary_search import binary_search_src

def getNames():
    file = open("./names.csv", "r")
    reader = csv.reader(file)
    names = []
    for row in reader:
        names.append(row[1])
    names.sort()
    file.close()
    return names

def linear(array, item):
    start = time.time()

    linear_search_src.search(array, item)

    end = time.time()
    timeTaken = end-start

    return timeTaken

def binary(array, item):
    start = time.time()

    binary_search_src.search(array, item)

    end = time.time()
    timeTaken = end-start

    return timeTaken

if __name__ == "__main__":
    array = getNames()

    item = input("What name would you like to search for? ").capitalize()

    print("\nLinear Search:", str(linear(array, item)))
    print("\nBinary Search:", str(binary(array, item)))