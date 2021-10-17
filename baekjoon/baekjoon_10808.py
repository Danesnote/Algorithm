S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz' #string 선언
result = [0]*len(alphabet) # string 길이만큼 리스트 생성

for i in S :
    result[alphabet.index(i)] += 1 # index(i) 함수는 i의 인덱스 값을 리턴해준다.
                                  # 그래서 result 인덱스에 1을 더 해주게끔 함.

print(*result) # *을 이용해 깔끔하게 출력