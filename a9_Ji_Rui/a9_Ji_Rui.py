def getLanguages(fileName="languages.csv"):
    list_languages = []
    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        line_clean = line.split(",")
        list_languages = line_clean
        break  # Only run the loops for one time and then break it to get the header rows.
    return list_languages


def getSecondLanguage(langList):  # the langList shall be the list_languages that grabbed in the first functions.
    print('Language Translator')
    print('Translate English words to one of the following languages:')
    print(langList)

    userInput = input("Enter a language: ")
    while userInput not in 'Danish, Dutch, Finnish, French, German, Indonesian, Italian, ' \
                           'Japanese, Latin, Norwegian, Portuguese, Spanish, Swahili, Swedish':
        print("This program does not support " + userInput)
        userInput = input("Enter a language: ")

    return userInput  # Get the chosen languages user want to translate.


def readFile(langList, langStr="English", fileName="languages.csv"):
    fileIn = open(fileName, "r")
    next(fileIn)  # help us skip the header row of CSV
    loc = langList.index(langStr)  # get the columns index of languages that the user chose.
    result_list = []
    for line in fileIn:
        line = line.strip()
        line_clean = line.split(",")
        loc_list = line_clean
        needed = loc_list[loc]
        result_list.append(needed)
    fileIn.close()
    return result_list


def createResultsFile(language):
    resultsFile = language + ".txt"
    fileOut = open(resultsFile, "w")
    print("Words translated from English to " + language, file=fileOut)
    fileOut.close()
    return resultsFile


def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    userchoice = 'kkk'
    while userchoice != "n":
        userInput = input('\n' + "Enter a word to translate:")
        if userInput not in englishList:
            print(userInput + " is not in the English list.")
        else:
            index = englishList.index(userInput)
            translated = secondList[index]
            if translated != "-":
                print(userInput + " is translated to " + translated)
                print(userInput + " = " + translated, file=fileOut)
            else:
                print(userInput + " did not have a translation.")
        userchoice = input("Another word (y or n)?").lower()
        while userchoice != "y" and userchoice != "n":
            userchoice = input("Another word (y or n)?").lower()

    print("Translated words have been saved to " + resultsFile)
    fileOut.close()
    return


def main():
    langList = getLanguages()  # Select all the languages that store on the header rows
    english_list = readFile(langList)  # Find the columns for the English rows
    second_language = getSecondLanguage(langList)  # Get the language that the user want to translate
    second_list = readFile(langList, second_language)  # Get the column where the user"s language stored
    resultfiles = createResultsFile(second_language)  # create the result file where we can write the result
    translateWords(english_list, second_list, resultfiles)


main()
