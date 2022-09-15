#!/usr/bin/env python3
from os import system
from requests_with_cache import get_with_cache

base_url = "https://api.datamuse.com/words"

system("clear") # clear screen before printing

keyword = input("Word to search for meaning like other words: ")
parameters = {"ml":keyword, "max":3}

results = get_with_cache(base_url, parameters)
print("Words with similar meaning are: ")
for couter, result in enumerate(results):
    print(f"{couter+1}.",result['word'].capitalize())
