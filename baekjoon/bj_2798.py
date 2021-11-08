import sys, itertools

n, m = map(int,sys.stdin.readline().split())
i = [] * n

i = list(map(int,sys.stdin.readline().split()))
bignum = 0

for card in itertools.combinations(i, 3):
  result = sum(card)
  if bignum < result <= m:
    bignum = result

print(bignum)
