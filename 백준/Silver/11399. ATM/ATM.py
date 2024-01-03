N = int(input())
P = list(map(int, input().split()))
result = 0
P.sort()
list = []

for i in range(N):
    list.append(P[i]*(N-i))

print(sum(list))