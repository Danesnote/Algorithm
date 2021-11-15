T = int(input())

for _ in range(T):
    word = list(input().split())
    word_reverse = []
    for i in word:
        word_reverse.append(i[::-1])
    print(*word_reverse)
