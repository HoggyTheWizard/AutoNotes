import wikipedia


with open("terms.txt") as file:
    term_list = []
    for word in file.readlines():
        word.replace("\n", "")
        term_list.append([word.replace(" ", "_").lower(), word])

    for term in term_list:
        try:
            print(f"{term[1]} - {wikipedia.page(term[0]).summary[:500]}\n\n")
        except:
            print(f"ERROR > term \"{term[0]}\" not found. Manual labor time.\n\n")

    print("Finished!")
