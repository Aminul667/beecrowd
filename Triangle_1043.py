
a, b, c = [float(i) for i in input().split()]

if (a + b > c) and (a + c > b) and (b + c) > a:
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = 0.5*(a + b)*c
    print(f"Area = {area:.1f}")
