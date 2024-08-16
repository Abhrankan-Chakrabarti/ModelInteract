import google.generativeai as genai
from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

model = genai.GenerativeModel('gemini-pro')
from stream import *