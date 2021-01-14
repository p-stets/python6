number = int(input("Input  nr: "))

# Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10.

if (number % 2 != 0 and number % 3 == 0 and number % 5 == 0 and number % 10 != 0):
    print("Value is OK")
else:
    print("Value is not OK")
