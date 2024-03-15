"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Simona Menšíková
email: simensikova@gmail.com
discord: mensikxs@gmail.com

"""

#list of texts for analysis
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#dictionary of registred users and their passwords:
logins = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "pass",
    "liz": "pass123"
}

separator = 50 * "-"

#starting of program with welcome:
print("Welcome!")
print(separator)
print('''
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+'''
)

#entering username and password:
name = input("Enter username: ")
password = input("Enter password: ")

#different situations when entering username and password:
#1 username and password are correct (registered)
if logins.get(name) == password:
    print(separator)

    #welcome and giving options:
    print(
        "Welcome to the app,", name,
        "\nWe have 3 texts to be analyzed."
    )
    print(separator)

    #choosing number of text:
    number = int(input(
        "Enter a number btw. 1 and 3 to select: "
    ))
    
    print(separator)

    #different situations when choosing text:
    #a) entered number is not in given range
    if number not in range(1, 4):
        print("Wrong text number, terminating the program..")
        exit()

    #b) entered symbol is not a number
    elif not str(number).isnumeric():
        print("Numbers only, terminating the program..")
        exit()

    #c) entered number is correct, program continues with chosen text analysis:
    else:
        #counting words in text
        words = len(TEXTS[number-1].split())
        print("There are", words, "words in the selected text.")

        #counting titlecase words
        title_case = len(
            [title for title in TEXTS[number-1].split() if title.istitle()]
        )
        print("There are", title_case, "titlecase words.")

        #counting uppercase words
        upper_case = len(
            [upper for upper in TEXTS[number-1].split() if upper.isupper()]
        )
        print("There are", upper_case, "uppercase words.")

        #counting lowercase words
        lower_case = len(
            [lower for lower in TEXTS[number-1].split() if lower.islower()]
        )
        print("There are", lower_case, "lowercase words.")

        #counting numeric strings
        numeric_string = len(
            [numer for numer in TEXTS[number-1].split() if numer.isnumeric()]
        )
        print("There are", numeric_string, "numeric strings.")

        #turning numeric string into int and counting their sum
        numbers = [numer for numer in TEXTS[number-1].split() if numer.isnumeric()]
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        
        print("The sum of all the numbers", sum(numbers))
        print(separator)

        #entering scheme part of program
        print("LEN|  OCCURENCES  |NR.")
        print(separator)


        











#2 Wrong username or password
else:
    print("Unregistered user, terminating the program..")
    exit()


    