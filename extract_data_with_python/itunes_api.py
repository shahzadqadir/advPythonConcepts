#!/usr/bin/env python3
import requests
from requests_with_cache import get_with_cache

base_url = "https://itunes.apple.com/search"
params = {"term": "sex with emily", "media": "podcast"}

results = get_with_cache(base_url, params=params)
# result_json = results.json()
for result in results['results']:
    print(result['artistName'], "\t", result['collectionName'], "\t", result['trackName'])

# print(results.json()['results'][0].keys())