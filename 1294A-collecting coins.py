t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())
    
    max_val = max(a, b, c)
    required = (max_val - a) + (max_val - b) + (max_val - c)
    
    if n < required:
        print("NO")
    else:
        remaining = n - required
        if remaining % 3 == 0:
            print("YES")
        else:
            print("NO")
