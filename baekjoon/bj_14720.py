input()
store = list(input().split())
cnt = 0
milk_state = 0

for i in store:
    if int(i) == milk_state:
        milk_state += 1
        cnt += 1
        if milk_state > 2:
            milk_state = 0

print(cnt)