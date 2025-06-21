
import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



def get_files_info(working_directory, directory=None):
    working_directory_contents = os.listdir(working_directory)

    directory = "." if directory is None else directory # clean input

    if directory not in working_directory_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(os.path.join(working_directory, directory)):
        return f'Error: "{directory}" is not a directory'
    return "hoo-rah"



def initialize_gemini():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    return client, model


def main():
    if len(sys.argv) == 1:
        print("Error: no prompt given")
        sys.exit(1)

    verbose_mode = False
    if len(sys.argv) == 3:
        verbose_mode = sys.argv[2] == "--verbose"
    
    print(get_files_info("calculator/", "."))
    sys.exit(0)
        
    user_prompt = sys.argv[1] 

    client, model = initialize_gemini()

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    content = client.models.generate_content(model=model, contents=messages)

    if verbose_mode:
        print(f"User prompt: {user_prompt}\nPrompt tokens: {content.usage_metadata.prompt_token_count}\nResponse tokens: {content.usage_metadata.candidates_token_count}")
    print(content.text)


if __name__ == "__main__":
    main()