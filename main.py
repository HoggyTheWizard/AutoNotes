import wikipedia


def insert_newlines(string, every):  # function taken from stackoverflow
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))


with open("terms.txt") as file:
    term_list = []
    for word in file.readlines():
        word.replace("\n", "")
        term_list.append([word.replace(" ", "_").lower(), word])

    for term in term_list:
        try:
            print(f"{term[1]} - {insert_newlines(wikipedia.page(term[0]).summary[:500], every=200)}\n\n")
        except:
            print(f"ERROR > term \"{term[0]}\" not found. Manual labor time.\n\n")

    print("Finished!")
