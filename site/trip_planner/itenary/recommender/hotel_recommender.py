import google.generativeai as genai
import json
import os


def handleData(file):
    userData = json.load(file)
    def generateResponse():
        genai.configure(api_key="AIzaSyCmg_nFCCMaYJ6tIeQNB-qPRm8YDS8tdbA")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Explain how AI works")

    return generateResponse()

if __name__ == "__main__":
    # response = handleData(file=)
    print("on work")