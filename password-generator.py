import random
import string

password = []
characters_left = -1

#################################################################################


def valid_char_left(name):
    global characters_left

    while True:
        try:
            input_chars = int(input("How many " + name + "?: "))
        except ValueError:
            print("invalid character (enter a number)")
            continue

        if input_chars < 0 or input_chars > characters_left:
            print("Not in range 0,", characters_left)
            continue
        else:
            characters_left -= input_chars
            print(characters_left, "characters left")
            break
    return input_chars


def valid_pass():
    global characters_left

    while True:
        try:
            input_chars = int(input("Password length: "))
        except ValueError:
            print("invalid character (enter a number)")
            continue

        if input_chars < 0:
            print("Password length cannot be negative")
            continue
        else:
            characters_left = input_chars
            break
    return input_chars


#################################################################################
#################################################################################

password_length = valid_pass()


lowercase_letters = valid_char_left("lowercase letters")
uppercase_letters = valid_char_left("uppercase letters")
special_characters = valid_char_left("special characters")
digits = valid_char_left("digits")


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
