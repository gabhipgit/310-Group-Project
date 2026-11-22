import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

tracks = """Ariana Grande - imagine
Justin Bieber - YUKON
Charli xcx - party 4 u
Alaina Castillo - pocket locket
The Weeknd - Is There Someone Else?"""

prompt = (
    "Here are someone's recent songs:\n" + tracks +
    "\n\nGive 3 concrete imagery words (like rain, moon, road, fire) "
    "that capture the vibe and would appear in poems. "
    'Reply only as JSON: {"vibe": "one sentence", "words": ["a","b","c"]}'
)

resp = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)
print(resp.text)