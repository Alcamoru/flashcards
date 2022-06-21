def startswith_capital_counter(names):
    i = 0
    name: str
    for name in names:
        if name[0].isupper():
            i += 1
    return i
