from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    # api_key="",
)
def call_openai(prompt='Write a Python function that returns the square of a number'):
    # Call the OpenAI API with the prompt
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    return chat_completion


# Summarize the diagnosis as you would to a 5 year old.
# Stats Finder 