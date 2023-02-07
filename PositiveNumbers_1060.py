positive = 0
for i in range(1, 7):
    num = float(input())
    if num > 0:
        positive += 1

print(f"{positive} valores positivos")