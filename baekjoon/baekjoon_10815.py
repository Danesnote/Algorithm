import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()

def binary_search(array,target,start,end):
  while start <= end: # 첫 인덱스 값이 마지막 값 인덱스보다 작거나 같다는 가정하에
    mid = (start + end) // 2 # 중간 인덱스 값은 두 합의 절반이고

    if array[mid] == target: # 만약 배열의 중간 값이 타겟 값과 같으면 mid로 리턴
      return mid
    elif array[mid] > target: # 배열의 중간 값이 타겟 값보다 크면 
      end = mid - 1           # 마지막 인덱스 값을 중간 인덱스 값 - 1 로 해서 반복
    else:
      start = mid + 1         # 작으면, 시작 인덱스 값을 중간 + 1로 해서 반복
  return None 

for i in range(m):
  if binary_search(card,check[i],0,n-1) is not None: # while문을 잘 돌아서 중간 값이 타겟 값과 만나면
    print(1,end=' ') # end=''는 개행하지 않을 때 쓴다
  else: # None이면,
    print(0,end=' ')