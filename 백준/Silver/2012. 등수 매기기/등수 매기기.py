import sys
input = sys.stdin.readline

N = int(input())
values = [int(input()) for _ in range(N)]
values.sort()

s = 0
for i in range(N):
    s += abs(values[i] - (i+1))
print(s)