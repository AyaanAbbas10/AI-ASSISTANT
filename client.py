from openai import OpenAI

#client = OpenAI()
#pip install openai
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
       api_key="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",
 )


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistantnamed jarvis skilled in general tasks like Alexa and Siri"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message)