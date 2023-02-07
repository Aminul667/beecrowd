
a, b = [int(i) for i in input().split()]

if a >= b:
    duration = (24 - a) + b
else:
    duration = b - a

print(f"O JOGO DUROU {duration} HORA(S)")
