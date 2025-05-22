# Overview
This project allows you to generate effective mnemonics using OpenAI GPT models for your Anki cards. The project consists of two scripts:
* mnemonics.py: adds mnemonics to given .tsv file representing your anki cards
* ankicards.py: creates anki cards from given .tsv file with given anki model

# Setup
First you will need an OpenAI API key. To create one head to [platform.openai.com/api-keys](platform.openai.com/api-keys). Make sure to add sufficient funds for the AI model you are going to use (default is gpt-4.1). While not free you can easily create about 1000 mnemonics for less than a single dollar using gpt-4.1. Once you are done open api_key.py and paste it in there. `api_key = "PASTE YOUR API KEY HERE"`

# Step By Step Guide
Once your setup you need to follow these three simple steps to create your anki cards with AI mnemonics.
* Create a new .tsv file in the data folder and input your anki cards.
* Run mnemonics.py from your terminal passing in your .tsv file.
* Run ankicards.py from your terminal passing in the newly created .tsv file.

# Data File
Before creating a new .tsv file in the data folder choose the anki model you want to use. For this example we are going to use jp-vocab. Opening the fields.txt file we can see that the model expects four fields: `Kanji, Kana, Meaning, Mnemonic`. The last field `Mnemonic` will be created automatically by mnemonic.py once we run it, i.e. our .tsv file should look as follows (we will look at the lesson.tsv file for all examples).
```
Kanji	Kana	Meaning
聞いて下さい	きいてください	please lisen
書いて下さい	かいてください	please write
読んで下さい	よんでください	please read
...
```

# Mnemonics
Once we created our .tsv file in the data folder we are ready for the next step. Open your terminal and navigate to the auto-mnemonic-anki folder. Now simply run mnemonic.py passing in `--ai --file --cols` arguments as needed. `--ai` chooses the OpenAI GPT model to use (default: gpt-4.1, cheaper: gpt-4.1-mini). `--file` chooses the .tsv data file to use and should be passed. Make sure to only pass in the filename not the extension e.g. `--file lesson` not --file lesson.tsv. `--cols` chooses wich columns will be used when creating the mnemonic and should be passed. Columns are indexed starting with 0 and diffrent columns should be seperated with a dash (-) e.g. `--cols 0-1-2`.
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
