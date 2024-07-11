import os
import openai

# Initialize the OpenAI client
openai.api_key = os.getenv("82d7d9dfc84f443d8b2af93e957624bf")

def get_code_analysis(code):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Analyze the following code:\n\n{code}\n\nProvide insights and suggestions:",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    # Read the code from a file or directory (for simplicity, reading from a single file here)
    with open("hello.py", "r") as file:
        code = file.read()

    analysis = get_code_analysis(code)
    print("Code Analysis:")
    print(analysis)

if __name__ == "__main__":
    main()
