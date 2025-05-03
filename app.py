from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="You are an amazing chef who can make a recipe out of any ingredients. "
                       "Be kind, creative, and clear when giving recipes and instructions."
)

# Create the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recipe = None
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        prompt = f"Create a recipe using these ingredients: {ingredients}. Include a title, ingredients list, and clear step-by-step instructions."
        response = model.generate_content(prompt)
        recipe = response.text

    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)