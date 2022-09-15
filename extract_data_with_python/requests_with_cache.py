#!/usr/bin/env python3
import requests, csv
import json

def create_full_url(base_url, params):
    params_value = [(key, params[key]) for key in params]
    full_url = base_url + "?"
    length = len(params)
    for data in params_value:
        if type(data[1]) == int:
            full_url += data[0] + "=" + str(data[1])            
        else:
            full_url += data[0] + "="+ "+".join(data[1].split(' '))
        length -= 1
        if length >= 1:
            full_url += "&"
    return full_url

def get_with_cache(base_url, params):
    """
    Check if the URL fetch content already in cache, return them. Else fetch them again.
    """
    full_url = create_full_url(base_url, params)

    try:
        with open("request_cache.txt") as infile:
            for line in infile:
                if full_url in json.loads(line):
                    print("Serving from cache...")
                    return json.loads(line)[full_url]
            result = {}
            response = requests.get(full_url).json()
            result[full_url] = response
            print("Adding new word to cache!")
            with open("request_cache.txt", "a") as outfile:
                outfile.write(json.dumps(result))
                outfile.write("\n")
            return response
    except:
        result = {}
        response = requests.get(full_url).json()
        result[full_url] = response
        print("Creating new file, adding key!")
        with open("request_cache.txt", "w") as outfile:
            outfile.write(json.dumps(result))
            outfile.write("\n")
        return response