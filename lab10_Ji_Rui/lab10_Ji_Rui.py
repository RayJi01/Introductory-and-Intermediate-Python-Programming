# Name, USC email
# ITP 115, Spring 2021
# Lab 10

def readFile(filename):
    mapping = {}
    linenumber = 1  # Count the line_number we go through. Line number always start with 1.
    fileIn = open(filename, "r")
    for line in fileIn:
        line = line.strip()
        words = line.split(" ")  # split the text into several words by space
        for word in words:
            word = word.lower()  # ignore the capitalization effects
            word.strip()  # get rid of whitespace
            word = word.strip(".,;:?\'\"")  # get rid of all the punctuation
            if word not in mapping:
                mapping[word] = []
                mapping[word].append(linenumber)  # if the word not in the list, create an emptly list adjoin the
                # linenumber
                # value = dict[key] look up the number
            else:
                mapping[word].append(linenumber)  # add current line number to it.
        linenumber += 1
    fileIn.close()
    return mapping


def sortKeys(dictionary):
    dicListKeys = dictionary.keys()
    listKeys = list(dicListKeys)
    listKeys.sort()
    return listKeys


def main():
    mapping = readFile("story.txt")
    listKey = sortKeys(mapping)
    for key in listKey:
        print(key + ":", mapping[key])


main()
