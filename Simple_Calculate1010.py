# In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

# Input
# The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

# Output
# The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

product1 = [float(i) for i in input().split()]
product2 = [float(i) for i in input().split()]

total1 = 1
total2 = 1

for i in range(1, 3):
    total1 = total1 * product1[i]
    total2 = total2 * product2[i]

total = total1 + total2

print(f'VALOR A PAGAR: R$ {total:.2f}')
