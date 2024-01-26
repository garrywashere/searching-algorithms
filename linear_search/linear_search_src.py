# Made with ❤️ by Garry
# 25/01/24

def search(array, item):
    index = 0

    found = False
    for element in array: # Iterate over the array
        if array[index] == item: # Check if the item we're currently on is what we're looking for
            found = True
            return index # If so, break the loop and return the index
            break
        else:
            index +=1 # If not, look for the next item
    if not found:
        return -1 # If the array is checked entirely and the item is not found, return -1 to signal an error

def getNames(): # Parse a large dataset to search through
    file = open("../names.csv", "r")
    reader = csv.reader(file)
    names = []
    for row in reader:
        names.append(row[1])
    names.sort()
    file.close()
    return names

if __name__ == "__main__":
    import csv

    names = getNames()

    name = input("What name would you like to search for? ")
    foundIndex = search(names, name.capitalize())
    print(foundIndex, names[foundIndex])