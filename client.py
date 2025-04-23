from openai import OpenAI

client = OpenAI(
  #api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
print(completion.choices[0].message["content"])
