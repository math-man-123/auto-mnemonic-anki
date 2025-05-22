# use this script to generate mnemonics to be 
# added to your .tsv file (data folder)

from openai import OpenAI
from api_key import api_key
import argparse, csv, util


# grab arguments passed in by the user
# --ai: open ai (gpt) model to use 
# --file: path to .tsv file to edit
# --cols: columns to use seperated by "-"
parser = argparse.ArgumentParser()
parser.add_argument("--ai", default="gpt-4.1")
parser.add_argument("--file", default="basic")
parser.add_argument("--cols", default="0-1")
args = parser.parse_args()


# provides reader for use in prompts
in_file = util.open_file(f"data/{args.file}.tsv", "r")
reader = csv.reader(in_file, delimiter="\t")
header = next(reader) # reads header

# provides writer for outputing result
out_file = util.open_file(f"out/{args.file}.tsv", "w")
writer = csv.writer(out_file, delimiter="\t")
writer.writerow(header + ["Mnemonic"]) # writer header


# create OpenAI client with given API-key
# and read in general prompt instructions
client = OpenAI(api_key=api_key)
inst = util.read_file("instructions.txt")

# generates mnemonic from given data
# data: full row from .tsv file
def gen_mnemonic(data):
    prompt = gen_prompt(data); print(f"Generating mnemonic for: [{prompt}]")
    response = client.responses.create(
        model=args.ai, instructions=inst, input=prompt)
    
    return response.output_text

# generates prompt for ai from data
# data: full row from .tsv file
def gen_prompt(data):
    cols = list(map(int, args.cols.split("-")))
    prompt = ""
    for col in cols:
        prompt += f"{header[col]}: {data[col]} | "

    return prompt.strip(" | ")


# work through each row of given .tsv file, 
# generate mnemonic, and add it to out file
for row in reader:
    writer.writerow(row + [gen_mnemonic(row)])

# manually close files after script is done
in_file.close(); out_file.close()
print("Done generating mnemonics!")
