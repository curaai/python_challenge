import pickle
from urllib.request import urlopen

if __name__ == '__main__':
    data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
    for i in data:
        print("".join([a * b for a, b in i]))