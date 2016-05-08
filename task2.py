from string import ascii_letters
from utils.network import get_html_comments

# Input mess is the second comment in the source code
input_text = get_html_comments("http://www.pythonchallenge.com/pc/def/ocr.html")[1]

# Find rare characters in the same occurrence they are in the input text
# Lets generate dictionary with occurrence frequency
# chars = set(input_text)
# chars_occur = {}
#
# for char in chars:
#     chars_occur[char] = input_text.count(char)
#     print(chars_occur)
#
# 'Rare' char in our case is limited to be only ascii letters and occurs only once, so we can very simply our code
result = ''
for char in input_text:
    if char not in result and char in ascii_letters:
        result += char

print(result)
