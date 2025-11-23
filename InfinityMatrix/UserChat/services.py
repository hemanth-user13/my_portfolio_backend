from openai import OpenAI
from django.conf import settings


client = OpenAI(api_key=settings.SECRET_API_KEY)


def generate_api_response(promptdata:str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": promptdata}
        ]
    )
    return response.choices[0].message.content