# Made with ❤️ by Garry
# 25/01/24

def search(array, item):
    low, high = 0, len(array) - 1 # Define our search scope, from lowest to highest value

    while low <= high: 
        mid = (low + high) // 2 # Find the middle of the current scope
        mid_value = array[mid] # Find the value of the middle

        if mid_value == item: 
            return mid  # Item found, return its index
        elif mid_value < item:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # If the array is checked entirely and the item is not found, return -1 to signal an error

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