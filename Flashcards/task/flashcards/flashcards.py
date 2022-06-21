import os
import random
import argparse

logs = []
parser = argparse.ArgumentParser(description="My program")
parser.add_argument("--import_from")
parser.add_argument("--export_to")

args = parser.parse_args()


def print_and_log(phrase):
    print(phrase)
    logs.append(phrase)


def input_and_log():
    user_entry = input()
    logs.append(user_entry)
    return user_entry


def import_from(file, cards_input, fails_input):
    if file in os.listdir():
        n = 0
        with open(file, "r") as infile:
            for couple in infile.readlines():
                term, definition, n_errors = couple.removesuffix("\n").split("|")
                cards_input[term] = definition
                fails_input[term] = int(n_errors)
                n += 1
        print_and_log(f"{n} cards have been loaded.")
        return cards_input, fails_input
    else:
        print_and_log("File not found.")


def export_to(file, cards_input, fails_input):
    with open(file, "a+") as outfile:
        for term, definition in cards_input.items():
            outfile.write(f"{term}|{definition}|{fails_input[term]}\n")
    print_and_log(f"{len(cards)} cards have been saved.")


cards = {}
fails = {}
exit_program = False


if args.import_from:
    import_from(args.import_from, cards, fails)


while not exit_program:
    print_and_log("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats)")
    action = input_and_log()
    if action == "add":
        print_and_log("The card:")
        term = input_and_log()
        while term in cards.keys():
            print_and_log("The term already exists. Try again:")
            term = input_and_log()
        print_and_log("The definition of the card:")
        definition = input_and_log()
        while definition in cards.values():
            print_and_log("The definition already exists. Try again:")
            definition = input_and_log()
        cards[term] = definition
        fails[term] = 0
        print_and_log(f'The pair ("{term}":"{definition}") has been added.')
    elif action == "remove":
        print_and_log("Which card?")
        to_remove = input_and_log()
        if to_remove in cards.keys():
            cards.pop(to_remove)
            print_and_log("The card has been removed.")
        else:
            print_and_log(f"Can't remove \"{to_remove}\": there is no such card.")
    elif action == "import":
        print_and_log("File name:")
        file = input_and_log()
        if import_from(file, cards, fails):
            cards, fails = import_from(file, cards, fails)
    elif action == "export":
        print_and_log("File name:")
        file = input_and_log()
        export_to(file, cards, fails)
    elif action == "ask":
        print_and_log("How many times to ask?")
        n_times = int(input_and_log())
        j = 0
        while j < n_times:
            term = random.choice(list(cards.keys()))
            definition = cards[term]
            print_and_log(f'Print the definition of {term}')
            answer = input_and_log()
            if answer == definition:
                print_and_log("Correct!")
            elif answer in cards.values():
                print_and_log(f"Wrong. The right answer is \"{definition}\", but your definition is correct for"
                      f"\"{[v for k, v in cards.items() if v == answer]}\".")
                fails[term] += 1
            else:
                print_and_log(f"Wrong. The right answer is \"{definition}\".")
                fails[term] += 1
            j += 1
    elif action == "exit":
        exit_program = True
        if args.export_to:
            export_to(args.export_to, cards, fails)
        print_and_log("bye bye")
    elif action == "log":
        print_and_log("File name:")
        with open(input_and_log(), "w") as outfile:
            for line in logs:
                outfile.write(line)
        print_and_log("The log has been saved.")
    elif action == "hardest card":
        max_v = 0
        for v in fails.values():
            if v >= max_v:
                max_v = v
        if max_v > 0:
            hardest_terms = []
            for k, v in fails.items():
                if v == max_v:
                    hardest_terms.append(k)

            if len(hardest_terms) == 1:
                print(f'The hardest card is "{hardest_terms[0]}". You have {max_v} errors answering it')
            else:
                terms = '", "'.join(hardest_terms)
                print(f'The hardest cards are "{terms}"')
        else:
            print_and_log("There are no cards with errors.")
    elif action == "reset stats":
        for k in fails.keys():
            fails[k] = 0
        print_and_log("Card statistics have been reset.")

