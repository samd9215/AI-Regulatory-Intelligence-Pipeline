from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def summarize_regulation(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a regulatory analyst. "
                    "Summarize the regulation update "
                    "and classify the risk level."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content

