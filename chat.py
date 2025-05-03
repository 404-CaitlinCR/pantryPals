# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

# set up API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # api key

model = genai.GenerativeModel(
    model_name = "gemini-1.5-pro-latest",
    system_instruction = "you are an amazing chef who can make a recipe out of any ingredients. your task is to generate recipes given ingredients. you are kind, understanding, but objective and straightforward when giving recipes and instructions."
)

# chatbot
def generate_recipe():

    # user input
    ingredients = input("Enter ingredients (comma separated): ")

    # define prompt
    prompt = f"Create a recipe using: {ingredients}. " \
                "Include a title, ingredients list, and step-by-step instructions."
    
    # output gemini AI response
    print("\nHere is your recipe:\n")
    response = model.generate_content(prompt, stream=True)

    for chunk in response:
        print(chunk.text, end="")

# run chatbot
if __name__ == "__main__":
    generate_recipe()
    