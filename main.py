
import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


if len(sys.argv) == 1:
    print("Error: no prompt given")
    sys.exit(1)

verbose_mode = False
if len(sys.argv) == 3:
    verbose_mode = sys.argv[2] == "--verbose"

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"
user_prompt = sys.argv[1] 

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

content = client.models.generate_content(model=model, contents=messages)

if verbose_mode:
    print(f"User prompt: {user_prompt}\nPrompt tokens: {content.usage_metadata.prompt_token_count}\nResponse tokens: {content.usage_metadata.candidates_token_count}")
print(content.text)