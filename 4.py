from urllib.request import urlopen
import re

if __name__ == '__main__':
    path = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    num = 66831
    p = re.compile('[0-9]+')

    for i in range(400):
        data = urlopen(path + str(num)).read().decode('utf-8')
        try:
            num = int(p.findall(data)[0])
        except Exception:
            print(data)
