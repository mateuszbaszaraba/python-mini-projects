import sys
import requests

no_of_tries = 5
used_letters = []

user_word = []

#################################################################################


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def game_stat():
    print("\n", user_word)
    print("Tries left:", no_of_tries)
    print("Used letters:", used_letters)
    print()


#################################################################################
#################################################################################


response = requests.get('https://random-word-api.herokuapp.com/word?number=1')

if response.status_code != 200:
    print('Something went wrong. Try again later.')
    sys.exit(0)

word = response.json()[0]

# print(word)

for _ in word:
    user_word.append('_')

while True:
    letter = input("Input a letter: ")
    if len(letter) > 1 or not letter.isalpha():
        print("Wrong input! Type a letter.")
        continue
    if used_letters.__contains__(letter):
        print('used that letter before')
        continue

    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is no such letter.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Game over! The word was:", word)
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Well done!")
            sys.exit(0)
    game_stat()
