import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    m = int(sys.stdin.readline())
    a.append(m)

b = sorted(a)

for i in b:
    print(i)