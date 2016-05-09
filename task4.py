import requests

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
nothing = 37278

while True:
    # response from linkedlist.php -> "and the next nothing is 45439"
    response = requests.get(base_url.format(nothing))
    if "and the next nothing is " not in response.text:
        print(base_url.format(nothing))
        print(response.text)
        break
    nothing = int(response.text[24:])

