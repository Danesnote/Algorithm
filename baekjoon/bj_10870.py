import sys

n = int(sys.stdin.readline())  
a = []*n

a.append(0)

if n >= 1:
  a.insert(1,1)

for i in range(2,n+1):
  a.insert(i,a[i-1] + a[i-2])

print(a[n])
print(a)