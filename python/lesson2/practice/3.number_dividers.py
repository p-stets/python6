number = int(input("Input  nr: "))

# Ввести число, вывести все его делители.

print('\n Number is: ' + str(number))

i = 1

while (i <= number):
    if (number % i == 0):
        print(str(i) + ' is OK for dividing')
    i += 1
