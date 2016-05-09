from string import ascii_lowercase, ascii_uppercase
from utils.network import get_html_comments

# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
input_text = get_html_comments("http://www.pythonchallenge.com/pc/def/equality.html")[0].strip()

for index in range(len(input_text)-10):
    if all((input_text[index] in ascii_lowercase,
            input_text[index+1] in ascii_uppercase,
            input_text[index+2] in ascii_uppercase,
            input_text[index+3] in ascii_uppercase,
            input_text[index+4] in ascii_lowercase,
            input_text[index+5] in ascii_uppercase,
            input_text[index+6] in ascii_uppercase,
            input_text[index+7] in ascii_uppercase,
            input_text[index+8] in ascii_lowercase)):
        print(input_text[index+4], end='')

