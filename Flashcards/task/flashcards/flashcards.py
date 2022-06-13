import os
import random

cards = {}
exit_program = False
while not exit_program:
    print("Input the action (add, remove, import, export, ask, exit):")
    action = input()
    if action == "add":
        print("The card:")
        term = input()
        while term in cards.keys():
            print("The term already exists. Try again:")
            term = input()
        print("The definition of the card:")
        definition = input()
        while definition in cards.values():
            print("The definition already exists. Try again:")
            definition = input()
        cards[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.')
    elif action == "remove":
        print("Which card?")
        to_remove = input()
        if to_remove in cards.keys():
            cards.pop(to_remove)
            print("The card has been removed.")
        else:
            print(f"Can't remove \"{to_remove}\": there is no such card.")
    elif action == "import":
        print("File name:")
        file = input()
        if file in os.listdir():
            n = 0
            with open(file, "r") as infile:
                for couple in infile.readlines():
                    term, definition = couple.removesuffix("\n").split("|")
                    cards[term] = definition
                    n += 1
            print(f"{n} cards have been loaded.")
        else:
            print("File not found.")
    elif action == "export":
        print("File name:")
        file_name = input()
        with open(file_name, "a+") as outfile:
            for term, definition in cards.items():
                outfile.write(f"{term}|{definition}\n")
        print(f"{len(cards)} cards have been saved.")
    elif action == "ask":
        print("How many times to ask?")
        n_times = int(input())
        j = 0
        while j < n_times:
            term = random.choice(list(cards.keys()))
            definition = cards[term]
            print(f'Print the definition of {term}')
            answer = input()
            if answer == definition:
                print("Correct!")
            elif answer in cards.values():
                print(f"Wrong. The right answer is \"{definition}\", but your definition is correct for \"{[v for k, v in cards.items() if v == answer]}\".")
            else:
                print(f"Wrong. The right answer is \"{definition}\".")
            j += 1

    elif action == "exit":
        exit_program = True
        print("bye bye")
