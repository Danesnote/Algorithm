#filter를 이용해 길이가 4 이상인 이름을 찾기
names = ['Kei','Tonny','Grace','홍길동','허균']

def more_four(n):
  return True if len(n) >= 4 else False

result = filter(more_four, names)

print(list(result))