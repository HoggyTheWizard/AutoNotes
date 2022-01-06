import wikipedia


with open("terms.txt") as file:
    term_list = []
    for word in file:
        word.replace("\n", "")
        word.replace("\"", "")
        word.replace(",", "")
        term_list.append([word.replace(" ", "_").lower(), word])

    for term in term_list:
        try:
            raw_text = wikipedia.summary(term[0])[:500]
            text = raw_text.split(".")
            text.remove(text[-1])
            text.reverse()
            formatted_text = "".join(text)
            print(f"{term[1]} - {formatted_text}.")
        except:
            continue

    print("Finished!")
