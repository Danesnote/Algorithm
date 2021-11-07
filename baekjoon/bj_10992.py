#10992 별찍기

import sys

N = int(sys.stdin.readline())

for i in range(1, N+1): 
  if i == N:
    print('*'*(2*i-1)) # 이런 규칙을 생각해내는 것이 중요할 듯
  elif i == 1:
    print(' '* (N-i), '*', sep = '') 
  else:
    print(' '*(N-i),'*',' '*(2*i-3),'*',sep = '')