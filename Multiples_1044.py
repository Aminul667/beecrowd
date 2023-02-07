
a, b = [int(i) for i in input().split()]

display = "Sao Multiplos" if b % a == 0 or a % b == 0 else "Nao sao Multiplos"
print(display)
