import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key")

genai.configure(api_key=GOOGLE_API_KEY)

import json

with open('config.json', 'r') as f:
    config = json.load(f)

model = genai.GenerativeModel(config['model'])
from gstream import *
