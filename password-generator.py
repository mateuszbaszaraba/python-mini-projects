import sys
import random
import string

password = []
characters_left = -1

#################################################################################


def update_char_left(number_of_char):
    global characters_left
    if number_of_char < 0 or number_of_char > characters_left:
        print("Not in range 0,", characters_left)
        sys.exit(0)

    else:
        characters_left -= number_of_char
        print(characters_left, "characters left")


#################################################################################

password_length = int(input("Password length: "))
if password_length < 5:
    print("Password must be at least 5-characters long")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input("How many lowercase letters?: "))
update_char_left(lowercase_letters)


uppercase_letters = int(input("How many uppercase letters?: "))
update_char_left(uppercase_letters)


special_characters = int(input("How many special characters?: "))
update_char_left(special_characters)


digits = int(input("How many digits?: "))
update_char_left(digits)

if characters_left > 0:
    print("Did not use all characters, lowercase will be used to fill the gap")
    lowercase_letters += characters_left

print()
print("Password length: ", password_length)
print("Lowercase letters: ", lowercase_letters)
print("Uppercase letters: ", uppercase_letters)
print("Special characters: ", special_characters)
print("Digits: ", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Generated password: ", "".join(password))
