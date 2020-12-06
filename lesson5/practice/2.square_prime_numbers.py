'''
Задание 2
Написать функцию которая будет простое число возводить в квардрат.

Необходимо возвести в квадрат все простые числа в списке используя функцию map
'''


# Number to square
def to_square(number):
    return number * number


# Check whether the number is a prime
def nubmer_is_natural(number):
    # Обработка для числа 1 и менее
    if number <= 1:
        return False

    for i in range(2, number + 1):
        if not number % i and i != number:
            return False
            break
    return True


# Square all primes
def prime_to_square(list_of_numbers, to_square=to_square, nubmer_is_natural=nubmer_is_natural):
    # results = [number for number in list_of_numbers if nubmer_is_natural(number)]
    results = list(map(lambda x: to_square(x) if nubmer_is_natural(x) else x, list_of_numbers))
    return results


# Test
print(prime_to_square([2, 3, 4, 53, 54]))

# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
