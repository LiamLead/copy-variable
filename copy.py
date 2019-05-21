def copy():
    name = True

    # if the value entered is empty, keep asking the user for input.
    while name:
        s = str(input("Name: "))
        t = s
        if t:
            t = t[0] + t[1:].capitalize()       # capitalize the second letter in the name
            return f"{s}\n{t}"

print(copy())