from sys import argv

'''
Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
'''

summ = int(input('How much money would you like to get (UAH): ')) if len(argv) <= 1 else int(argv[1])

bills_available = sorted([1, 2, 5, 10, 20])
max_bills = 10

for i in reversed(bills_available):
    count = summ // i
    if count:
        if count <= max_bills:
            summ -= count * i
        else:
            count = max_bills
            summ -= i * max_bills
        print(f'{i} UAH bills x {count}')
    else:
        continue
if summ:
    print(f'{summ} UAH left')
