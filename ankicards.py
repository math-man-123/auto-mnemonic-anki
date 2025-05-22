# use this script to generate anki cards from 
# your .tsv file with mnemonics (out folder)

import genanki, csv, argparse, util


# grab arguments passed in by the user
# --anki: anki note model to use
parser = argparse.ArgumentParser()
parser.add_argument("--anki", default="basic")
parser.add_argument("--file", default="basic")
args = parser.parse_args()


# load anki card style for selected anki model
# load settings from settings.json for selected anki model
style = util.read_file(f"anki/{args.anki}/style.css")
settings = util.load_file(f"anki/{args.anki}/settings.json")


# provides reader for use in prompts
in_file = util.open_file(f"out/{args.file}.tsv", "r")
reader = csv.reader(in_file, delimiter="\t")
header = next(reader)  # reads header


# generates fields description from .tsv file header
def get_fields_desc():
    desc = lambda field: {"name": f"{field}"}
    
    fields_desc = []
    for field in header:
        fields_desc.append(desc(field))

    return fields_desc


# generates template description from anki model files
def get_templs_desc():
    desc = lambda name, que, ans: {"name": name, "qfmt": que, "afmt": ans}

    templs_desc = []
    for card in range(settings["card_num"]):
        # get name, question, and answer according to settings
        name = settings["name"]["card"][card]
        que = util.read_file(f"anki/{args.anki}/card{card}/question.html")
        ans = util.read_file(f"anki/{args.anki}/card{card}/answer.html")
        
        templs_desc.append(desc(name, que, ans))

    return templs_desc


# create anki model according to settings
model = genanki.Model(
    settings["id"]["model"],
    settings["name"]["model"],
    fields=get_fields_desc(),
    templates=get_templs_desc(),
    css=style)

# create anki deck according to settings
deck = genanki.Deck(
    settings["id"]["deck"],
    f"[{args.file}] to [{args.anki}]")


# for each row in the .tsv with mnemonics
# create an anki note and add it to the deck
for count, fields in enumerate(reader, start=1):
        deck.add_note(genanki.Note(model=model, fields=fields))
        print(f"Added note {count}.")


# output anki deck as .apkg ready to import
# manually close files after script is done
genanki.Package(deck).write_to_file(f"[{args.file}-tsv]to[{args.anki}].apkg")
in_file.close(); print("Done generating anki cards!")
