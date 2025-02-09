import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
from django.conf import settings


def handleData(file):
    userData = json.load(file)
    def generateResponse():
        api = os.getenv("Gem_KEY")
        genai.configure(api_key=api)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Plan an {userData["days"]} day trip to {userData["location"]} given that I 
                                          {userData["type of person"]} type of person. The mode of travel that I
                                          would prefer is {userData["transport"]}")
        return response

    return generateResponse()

if __name__ == "__main__":
    load_dotenv()
    final_response = handleData(file=os.path.join(settings.BASE_DIR, "user_preferences.json"))