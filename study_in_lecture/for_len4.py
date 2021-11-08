#for문을 이용해 길이가 4 이상인 이름을 찾기
names = ['Kei','Tonny','Grace','홍길동','허균']
a=[]*5

for name in names:
  if len(name) >= 4:
    a.append(name)

print(a)