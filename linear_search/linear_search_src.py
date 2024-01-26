# Made with ❤️ by Garry
# 25/01/24

def search(array, item):
    index = 0

    found = False
    for element in array:
        if array[index] == item:
            found = True
            return index
            break
        else:
            index +=1
    if not found:
        return "Not Found"

def getNames():
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
    print(search(names, name.capitalize()))