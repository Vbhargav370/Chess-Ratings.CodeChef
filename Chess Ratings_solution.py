"""
https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/C_RATING
"""
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    count = 0
    if x >= y:
        print(x - y)
    else:
        while x < y:
            x += 8
            count += 1
        print(count)
