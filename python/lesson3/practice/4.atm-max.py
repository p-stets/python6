from sys import argv

'''
Банкомат выдает сумму максимально возможными купюрами
'''

summ = int(input('How much money would you like to get (UAH): ')) if len(argv) <= 1 else int(argv[1])

bills_available = sorted([50, 100, 1000])

for i in reversed(bills_available):
    count = summ // i
    if count:
        summ -= count * i
        print(f'{i} UAH bills x{count}')
    else:
        continue
if summ:
    print(f'{summ} UAH left')
