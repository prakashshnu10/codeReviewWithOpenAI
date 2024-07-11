import os
import openai

# Initialize the Azure OpenAI client
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")

def get_code_analysis(code):
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code analysis assistant."},
            {"role": "user", "content": f"Analyze the following code:\n\n{code}\n\nProvide insights and suggestions."}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def main():
    # Read the code from a file or directory (for simplicity, reading from a single file here)
    with open("hello.py", "r") as file:
        code = file.read()

    analysis = get_code_analysis(code)
    print("Code Analysis:")
    print(analysis)

if __name__ == "__main__":
    main()
