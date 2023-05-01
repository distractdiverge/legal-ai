import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

def init_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt4",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def main():
    user_prompt = input("Enter your message for ChatGPT: ")
    response = init_chat_gpt(user_prompt)
    print("ChatGPT response:", response)

if __name__ == "__main__":
    main()
