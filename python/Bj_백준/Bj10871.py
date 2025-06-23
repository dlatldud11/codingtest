n, x = map(int, input().split())

# print(f"입력값 {n}, {x}")

list = list(map(int, input().split()))
# print(f"입력된 리스트: {list}")

print(*[list[i] for i in range(n) if list[i] < x])