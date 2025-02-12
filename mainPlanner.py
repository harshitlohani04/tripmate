import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
from django.conf import settings


def handleData(file):
    userData = json.loads(file)
    def generateResponse():
        load_dotenv()
        api = os.getenv("Gem_KEY")
        genai.configure(api_key=api)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Plan an {userData['days']} day trip to {userData['destination']} given that I\
                                          {userData['type_of_group']} type of person")
        return response.text

    return generateResponse()
