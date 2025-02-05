import google.generativeai as genai
import json
import os
from dotenv import load_dotenv


def handleData(file):
    userData = json.load(file)
    def generateResponse():
        api = os.getenv("Gem_KEY")
        genai.configure(api_key=api)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Plan an {userData["days"]} day trip to {userData["location"]}")

    return generateResponse()

if __name__ == "__main__":
    # response = handleData(file=)
    load_dotenv()
    print("on work")