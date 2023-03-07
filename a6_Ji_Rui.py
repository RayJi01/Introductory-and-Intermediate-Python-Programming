# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Assignment 6
# Description:
# Describe what this program does.

def main():
    encryp_alphabet = []
    new_word = []
    old_word = []
    new_letter = '0'
    msg = input('Enter a message: ').lower()
    num = int(input('Enter a number to shift by (0-25): '))
    list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
                     , 'u', 'v', 'w', 'x', 'y', 'z']  # Create the original alphabet
    if num in range(25):
        slice = list_alphabet[0:num]
        new_encryp = list_alphabet[num:26]
        encryp_alphabet = new_encryp + slice
# Encrypt the word by using the index manipulations:
    print('Encrypting message....')
    for i in msg:
        if i in list_alphabet:
            index = list_alphabet.index(i)
            new_letter = encryp_alphabet[index]
            new_word.append(new_letter)

        else:
            new_letter = i  # For those not characters elements: space for example, leave them unchanged
            new_word.append(new_letter)

    print('Encrypted message:', ''.join(new_word))  # use the join.fuction to extract elements from list.

    print('\n')

# Decryption:
    print("Decrypting message....")
    for i in new_word:
        if i in encryp_alphabet:
            index = list_alphabet.index(i)
            old_letter = list_alphabet[index-num]
            #To return to the original one, we need to deduct what the users input
            old_word.append(old_letter)
        else:
            old_letter = i
            old_word.append(old_letter)
    print('Decrypted message:', ''.join(old_word))
    print('Original message:', msg)


main()