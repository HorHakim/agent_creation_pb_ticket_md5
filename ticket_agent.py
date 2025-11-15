from groq import Groq
from dotenv import load_dotenv
import random
import os

load_dotenv()

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


client = Groq(api_key=os.environ["GROQ_KEY"])

def generate_ticket_mail():

    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role": "system",
                "content": read_file(file_path="context.txt")
            },
            {
                "role": "user",
                "content": read_file(file_path="prompt.txt")
            }
        ],
        temperature=0.5,
        response_format={"type": "json_object"},
        model="llama-3.3-70b-versatile" if random.randint(0, 1) else "openai/gpt-oss-20b"
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    ticket_response = generate_ticket_mail()
    print(ticket_response)
