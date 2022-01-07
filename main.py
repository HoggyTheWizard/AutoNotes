import wikipedia
import argparse

parser = argparse.ArgumentParser(description="Automatically search Wikipedia for provided terms")
parser.add_argument("--input", "-i", type=str, help="Input file containing terms to search for", required=True)
parser.add_argument("--output", "-o", type=str, help="Output file to write results to", required=True)
parser.add_argument("--interactive", "-I", action="store_true", help="Interactive mode")
args = parser.parse_args()


def interactive_try_until_found(initial_error, initial_term):
    new_term = initial_term
    print(f"{new_term} - {initial_error}")
    while True:
        new_term = input("Try to find a new term: ")
        try:
            new_term = new_term.replace("\"", "").replace(",", "").replace("\n", "")
            search_term = new_term.replace(" ", "_").lower()
            input_text = wikipedia.summary(search_term)[:500]
            new_text = input_text.rsplit(".", 1)[0]
            print(f"{term[1]} - {new_text}.")
            return f"{new_term} - {new_text}.\n"
        except wikipedia.exceptions.PageError:
            print(f"{new_term} - Not found.")
        except wikipedia.exceptions.DisambiguationError:
            print(f"{new_term} - Too ambiguous.")


with open(args.input) as file:
    term_list = []
    for word in file:
        word = word.replace("\n", "").replace("\"", "").replace(",", "")
        term_list.append([word.replace(" ", "_").lower(), word])

output_text = ""

for term in term_list:
    try:
        raw_text = wikipedia.summary(term[0])[:500]
        text = raw_text.rsplit(".", 1)[0]
        print(f"{term[1]} - {text}.")
        output_text += f"{term[1]} - {text}.\n\n"
    except wikipedia.exceptions.PageError:
        if args.interactive:
            output_text += interactive_try_until_found("Not found.", term[1])
    except wikipedia.exceptions.DisambiguationError:
        if args.interactive:
            output_text += interactive_try_until_found("Too ambiguous.", term[1])
print("Finished!")

with open(args.output, "w", encoding="utf-8") as file:
    file.write(output_text)
