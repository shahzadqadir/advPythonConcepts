#!/usr/bin/evn python3

import requests
from requests.api import request
import os

base_url = "https://api.datamuse.com/words"

def get_synonyms(word, word_count=3):
    params = {}
    params['ml'] = word
    params['max'] = word_count
    response = requests.get(base_url, params=params)
    words = [key['word'] for key in response.json()]
    return (words, response.url)

def get_sounds_like(word, word_count=3):
    params = {}
    params['sl'] = word
    params['max'] = word_count
    response = requests.get(base_url, params=params)
    words = [key['word'] for key in response.json()]
    sent_url = response.url
    return (words, sent_url)

def find_related_words(word, word_count=3):
    params = {}
    params['rel_syn'] = word
    params['max'] = word_count
    response = requests.get(base_url, params=params)
    words = [key['word'] for key in response.json()]
    sent_url = response.url
    return (words, sent_url)

words, sent_url = find_related_words("cute")
print(words)
print(sent_url)

