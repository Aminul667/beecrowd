
ihour, imin, fhour, fmin = [int(i) for i in input().split()]

itotal = ihour*60 + imin
ftotal = fhour*60 + fmin

if itotal >= ftotal:
    duration = (24*60 - itotal) + ftotal
    hour = int(duration/60)
    minute = duration % 60
else:
    duration = ftotal - itotal
    hour = int(duration/60)
    minute = duration % 60

print(f"O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)")
