
salary = float(input())

if 0 <= salary <= 400.00:
    percent = 15
    increment = salary*0.15
    current_salary = salary + increment
elif 400.01 <= salary <= 800.00:
    percent = 12
    increment = salary*0.12
    current_salary = salary + increment
elif 800.01 <= salary <= 1200.00:
    percent = 10
    increment = salary*0.10
    current_salary = salary + increment
elif 1200.01 <= salary <= 2000.00:
    percent = 7
    increment = salary*0.07
    current_salary = salary + increment
else:
    percent = 4
    increment = salary*0.04
    current_salary = salary + increment


print(f"Novo salario: {current_salary:.2f}")
print(f"Reajuste ganho: {increment:.2f}")
print(f"Em percentual: {percent} %")
