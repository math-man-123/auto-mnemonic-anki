# Overview
This project allows you to generate effective mnemonics using OpenAI GPT models for your Anki cards. The project consists of two scripts:
* mnemonics.py: adds mnemonics to given .tsv file representing your Anki cards
* ankicards.py: creates Anki cards from given .tsv file with given Anki model

# Setup
First you will need an OpenAI API key. To create one head to [platform.openai.com/api-keys](https://platform.openai.com/api-keys). Make sure to add sufficient funds for the AI model you are going to use (default is gpt-4.1). While not free you can easily create about 1000 mnemonics for less than a single dollar using gpt-4.1. Once you are done open api_key.py and paste it in there. `api_key = "PASTE YOUR API KEY HERE"`

# Step By Step Guide
Once you are setup you need to follow these three simple steps to create your Anki cards with AI mnemonics.
* Create a new .tsv file in the data folder and input your Anki cards.
* Run mnemonics.py from your terminal passing in your .tsv file.
* Run ankicards.py from your terminal passing in the newly created .tsv file.

# Data File
Before creating a new .tsv file in the data folder choose the Anki model you want to use. For this example we are going to use jp-vocab. Opening the fields.txt file we can see that the model expects four fields: `Kanji, Kana, Meaning, Mnemonic`. The last field `Mnemonic` will be created automatically by mnemonic.py once we run it, i.e. our .tsv file should look as follows (we will look at the lesson.tsv file for all examples).
```
Kanji	Kana	Meaning
聞いて下さい	きいてください	please lisen
書いて下さい	かいてください	please write
読んで下さい	よんでください	please read
...
```

# Mnemonics
Once we created our .tsv file in the data folder we are ready for the next step. Open your terminal and navigate to the auto-mnemonic-anki folder. Now simply run mnemonic.py passing in `--ai --file --cols` arguments as needed. `--ai` chooses the OpenAI GPT model to use (default: gpt-4.1, cheaper: gpt-4.1-mini). `--file` chooses the .tsv data file to use and should be passed. Make sure to only pass in the filename not the extension e.g. `--file lesson` not --file lesson.tsv. `--cols` chooses which columns will be used when creating the mnemonic and should be passed. Columns are indexed starting with 0 and different columns should be separated with a dash (-) e.g. `--cols 0-1-2`.
```
python mnemonics.py --file lesson --cols 0-1-2
```
We now created a new .tsv file in the out folder. In our example the AI generated the following mnemonics. Keep in mind that you can always tweak the instructions for the AI to change how the mnemonics turn out. Simply open instructions.txt and change them as you desire.
```
Kanji	Kana	Meaning	Mnemonic
聞いて下さい	きいてください	please lisen	Keen ears (きいて) please! Listen up when you see 聞いてください.
書いて下さい	かいてください	please write	Imagine a kite (かい) writing (書) a note—please write (ください) it down!
読んで下さい	よんでください	please read	Imagine a librarian saying, “Please read (yawn) the book” — よんでください.
...
```

# Anki Cards
Finally we can create our desired Anki cards. To do so open your terminal and run ankicards.py passing in `--file --anki` arguments as needed. `--file` chooses the .tsv out file to use and should be passed. As before make sure to only pass in the filename not the extension e.g. `--file lesson`. `--anki` chooses the Anki model to use and should be passed as well e.g. `jp-vocab`. Make once again sure that your .tsv out file matches its header to the required Anki model fields. In our example we need `Kanji, Kana, Meaning, Mnemonic` which we correctly have.
```
python ankicards.py --file lesson --anki jp-vocab
```
After this script finishes there will be a ready to import .apkg file. Once imported to Anki you can sort the cards away how you like.

# New Anki Models
With this project are 4 models provided, 2 of which are kinda specific to my personal needs, and 2 of which are very basic. If you wish to create your own model, you can do so by adding a folder with your model name into the Anki folder e.g. `anki/my-model`. You now need to create 3 files inside your model folder as well as at least one further subfolder.
* my-model/settings.json: Needs to contain an object with the following properties. `id.model, id.deck` unique integer - ids for your model and deck (hardcoded). `name.model` string - how your model is called. `name.card` array of strings - how each of your models cards are called. `card_num` integer - the number of cards of your model.
* my-model/style.css: Needs to be there, even if you dont use any css on your cards. Should contain all css to apply to your models cards. 
* my-model/fields.txt: Optional but highly recommended. Simply write down the exact field names and order for your model. This makes it easier to create proper .tsv data files.

Finally you need to create a subfolder called `my-model/cardN` where N is a integer starting with 0, for each card (template) your model produces. Inside of each cardN folder you should create 2 .html files that describe that Anki card (template) - just as you do in Anki.
* my-model/cardN/question.html: Has to be there and should contain the html that describes that anki cards (template) front side.
* my-model/cardN/answer.html: Has to be there and should contain the html that describes that Anki cards (template) back side.
