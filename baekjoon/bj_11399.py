import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort(key=lambda x: -x)

fulltime = 0

for t in range(n):
    fulltime += time[t] * (t+1)

print(fulltime)
