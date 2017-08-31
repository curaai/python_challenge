import re
import zipfile

n = '90052'
history = []
f = zipfile.ZipFile('channel.zip')
print(f.read(n + '.txt'))


def next_zip(n):
    history.append(n)
    text = f.read(n + '.txt').decode()
    m = re.search('\d+', text)
    if m is None: return m
    n = m.group()
    return n

while n: n = next_zip(n)

print(''.join(f.getinfo(n + '.txt').comment.decode() for n in history))


# 이거 너무 어려워서 보고 베꼇어여 ㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜ
# 다음 부턴 안보고 해볼게여
