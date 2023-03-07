# Name, USC email
# ITP 115, Spring 2021
# Lab 9


def read_files(user_genre, file_name):
    listOfShow = []
    filein = open(file_name, "r")
    for line in filein:
        line = line.strip()
        lineList = line.split(",")
        name_of_show = lineList[0]
        genreOfShow = lineList[1]
        if user_genre in genreOfShow:
            listOfShow.append(name_of_show)

    filein.close()
    return listOfShow


def write_files(genre, showList):
    filename = genre + '.txt'
    fileout = open(filename, "w")  # format of writing a new files.
    for show in showList:
        print(show, file=fileout)
    fileout.close()
    print("The file" + filename + "has the following shows:")
    print(showList)


def main():

    print("TV Shows")
    print("Possible genres are action & adventure, animation, comedy, ")
    print("documentary, drama, mystery & suspense, science fiction & fantasy")

    inputGenre = "default"
    while inputGenre not in "action & adventure, animation, comedy, documentary, drama, mystery & suspense, science " \
                            "fiction & fantasy":
        inputGenre = input("Enter a genre: ")

    listOfShow = read_files(inputGenre, 'shows.csv')
    write_files(inputGenre, listOfShow)


main()