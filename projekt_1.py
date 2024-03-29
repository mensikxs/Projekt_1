""""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Simona Menšíková
email: simensikova@gmail.com
discord: mensikxs@gmail.com

"""
import string
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

# different situations when entering username and password:

# 1) username and password are correct (registered user):
if logins.get(name) == password:
    print(separator)

    # welcome and give options:
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

    # different situations when choosing text:
    # a) entered symbol is not a number
    if not number.isnumeric():
        print("Numbers only, terminating the program..")
        exit()

    # b) entered number is not in given range
    elif int(number) not in range(1, len(text) + 1):
        print("Wrong text number, terminating the program..")
        exit()

    # c) entered number is correct, program continues with analysis
    # of the chosen text:
    else:
        number = int(number)

        # a) counting words:
        words = len(text[number-1].split())
        print("There are", words, "words in the selected text.")

        # b) counting titlecase words:
        title_case = len(
            [title for title in text[number-1].split() if title.istitle()]
        )
        print("There are", title_case, "titlecase words.")

        # c) counting uppercase words:
        upper_case = len(
            [upper for upper in text[number-1].split()
             if upper.isupper() and upper.isalpha()]
        )
        print("There are", upper_case, "uppercase words.")

        # d) counting lowercase words:
        lower_case = len(
            [lower for lower in text[number-1].split() if lower.islower()]
        )
        print("There are", lower_case, "lowercase words.")

        # e) counting numeric strings + f) their sum:
        numeric_string =[]
        for num_str in text[number-1].split():
            if num_str.isnumeric():
                num_str = int(num_str)
                numeric_string.append(num_str)
        print("There are", len(numeric_string), "numeric strings.")
        print(f"The sum of all the numbers is {sum(numeric_string)}.")

        print(separator)

        # g) creating word length vs. frequency graph:

        # cleaning text from punctuation:
        exclude = (string.punctuation)
        clean_text = ""
        for letter in text[number-1]:
            if letter not in exclude:
                clean_text += letter

        # spliting clean text into words and counting their lengths:
        length = list(map(len, clean_text.split()))

        # counting frequencies:
        frequency = []
        for values in range(min(length), max(length) + 1):
            frequency.append(length.count(values))

        # preparing graph components:
        
        # occurences represented by symbol "*":
        symbol = []
        for j in range(len(frequency)):
            symbol.append(frequency[j] * "*")

        # lenghts of present words:
        sequence = []
        for seq_number in range(1, len(frequency) + 1):
            sequence.append(str(seq_number))

        # assembling graph lines:
        graph = []
        line = []
        for row in range(len(frequency)):
            line = [
                sequence[row].rjust(3),
                "| ",
                symbol[row],
                " " * (max(frequency) - frequency[row]),
                "|".rjust(3),
                str(frequency[row])
            ]
            graph.append("".join(line))

        # printing graph legend and graph:
        print(
            "LEN|",
            "OCCURENCES".center(max(frequency) + 1),
            "|NR.",
        )
        print(separator)
        print("\n".join(graph))

        exit()


# 2 Wrong username or password
elif not logins.get(name):
    print("Unregistered user, terminating the program..")
    exit()

else:
    print("Wrong password, terminating the program..")
