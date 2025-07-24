from together import Together
from dotenv import load_dotenv

load_dotenv()
client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=[
      {
        "role": "user",
        "content": "Best linux distro for daily use in brief"
      }
    ]
)
print(response.choices[0].message.content)