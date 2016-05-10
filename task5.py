import requests
import pickle

dump = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").content
data = pickle.loads(dump)

for row in data:
    for column in row:
        print("{}".format(column[0]) * column[1], end="")
    print()
