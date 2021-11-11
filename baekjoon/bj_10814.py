n = int(input())

a = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    a.append((age, name))

a.sort(key=lambda x: x[0])

for i in range(n):  # 리스트 안의 리스트 깔끔하게 출력하기
    print(*a[i], sep=' ')