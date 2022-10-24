import re

text = "Hello, my name is John. I am a software engineer. I am from Egypt. I speak Arabic and English."

arabic_text = re.findall(r'[\u0600-\u06FF]+', text)

print(arabic_text)