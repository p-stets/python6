number = int(input("Input  nr: "))

# Ввести число, вывести его разряды и их множители

print('\n Number is: ' + str(number) + '\n')

l = len(str(number))
print('Len is: ', l)

for i in str(number):
    l -= 1
    print(i, '* 10^', l)
