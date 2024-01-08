import textwrap
import time

import google.generativeai as genai


genai.configure(api_key='***')#https://makersuite.google.com/

#####################TO CHECK AVAILABLE MODELS
"""for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)"""

############################################################################## FOR  IMAGE TO TEXT
import PIL.Image
def anaylyze(path,query):
    img = PIL.Image.open(f"{path}")

    a = time.time()
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([f"{query} ,explain under 20 words",img])
    b = time.time()

    return response.text
############################################################################## FOR CHATTING




