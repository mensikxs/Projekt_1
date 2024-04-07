""""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Simona Menšíková
email: simensikova@gmail.com
discord: mensikxs@gmail.com

"""
import sys

from task_template import TEXTS as text

separator = 40 * "-"

# dictionary of registred users and their passwords:
logins = {
    "bob": "123",
    "ann": "pass123",
    "mike": "pass",
    "liz": "pass123"
}

# entering username and password:
name = input("Enter username: ")
password = input("Enter password: ")

# 1) wrong username or password:

if not logins.get(name):
    print("Unregistered user, terminating the program..")
    sys.exit()

elif logins.get(name) != password:
    print("Wrong password, terminating the program..")
    sys.exit()

# 2) correct username and password
    # welcome and give options:
print(separator)

available_text = len(text)
print(
    f"Welcome to the app, {name}!",
    f"We have {available_text} texts to be analysed.",
    sep= "\n"
)
print(separator)

# choosing text:
number = input(
    f"Enter a number btw. 1 and {available_text} to select: "
    )
print(separator)

# a) entered symbol is not a number
if not number.isnumeric():
    print("Numbers only, terminating the program..")
    sys.exit()

# b) entered number is not in given range
elif int(number) not in range(1, len(text) + 1):
    print("Wrong text number, terminating the program..")
    sys.exit()

# c) entered number is correct, program continues with analysis
# of the chosen text:

count = 0
titlecase = 0
upper = 0
lower = 0
numeric = []
clean_text = []
word_length = []

for word in text[int(number)-1].split():
    count += 1
    if word[0].isupper(): titlecase += 1
    if word.isupper() and word.isalpha(): upper += 1
    if word.islower(): lower += 1
    if word.isnumeric(): numeric.append(int(word))
    clean_text.append(word.strip(".,;:"))

print(
f"""There are {count} words in the selected text.
There are {titlecase} titlecase words.
There are {upper} uppercase words.
There are {lower} lowercase words. 
There are {len(numeric)} numeric strings.
The sum of all the numbers is {sum(numeric)}."""
)
print(separator)

# d) creating word length vs. frequency graph:

word_length = list(map(len, clean_text))

frequency = []
for value in range(min(word_length), max(word_length) + 1):
    frequency.append(word_length.count(value))

print(
    "LEN|",
    "OCCURENCES".center(max(frequency)),
    "|NR.",
)
print(separator)
    
for index, value in enumerate(frequency, 1):
    print(
    f"{index: >2}.| {value * "*"}{(max(frequency)-value) * " "} |{value}"
    )
sys.exit()
