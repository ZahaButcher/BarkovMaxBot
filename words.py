from deep_translator import GoogleTranslator
#
text = "Hello, how are you?"

translated = GoogleTranslator(
    source="en",
    target="ru"
).translate(text)

print(translated)
# ------------------------------------------

# from ollama import chat
#
# response = chat(
#     model="qwen3",
#     messages=[
#         {
#             "role": "user",
#             "content": """
#             Придумай слово для викторины и 5 вопросов,
#             по которым игрок сможет его угадать.
#             """
#         }
#     ]
# )
#
# print(response.message.content)
# ------------------------------------------

from searchx import Client

client = Client()
results = client.search("Кот")
print(results)