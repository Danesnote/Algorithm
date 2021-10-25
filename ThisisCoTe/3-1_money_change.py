#거스름돈 문제

n = 1260 #거스름돈
count = 0

coin_types=[500,100,50,10] #잔돈 종류

for coin in coin_types:
    count += n // coin #동전 개수 세기
    n %= coin

print(count)