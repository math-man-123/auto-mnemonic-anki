# Overview
This project allows you to generate effective mnemonics using OpenAI GPT models for your Anki cards. The project consists of two scripts:
* mnemonics.py: adds mnemonics to given .tsv file representing your anki cards
* ankicards.py: creates anki cards from given .tsv file with given anki model

# Setup
First you will need an OpenAI API key. To create one head to [platform.openai.com/api-keys](platform.openai.com/api-keys). Make sure to add sufficient funds for the AI model you are going to use (default is gpt-4.1). While not free you can easily create about 1000 mnemonics for less than a single dollar using gpt-4.1. Once you are done open api_key.py and paste it in there.
`api_key = "PASTE YOUR API KEY HERE"`
