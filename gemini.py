import google.generativeai as genai
from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

import json

with open('config.json', 'r') as f:
    config = json.load(f)

model = genai.GenerativeModel(config['model'])
from gstream import *