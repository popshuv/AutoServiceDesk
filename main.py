import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# load the .env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

def get_gpt4_json_response(prompt):
    response = OpenAI.Completion.create(
        model="gpt-4-turbo",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 256,
        response_format={"type": "json_object"}
    )

    return response.json()

