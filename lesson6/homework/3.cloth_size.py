'''
Написать функцию перевода размеров женского белья из международного во все остальные.
Внтри функции нужно просто обращаться к правильно составленному словарю.
'''

LINGERIE_SIZES = {
    'International': ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'],
    'Russia': ['42', '44', '46', '48', '50', '52', '54', '56'],
    'Germany': ['36', '38', '40', '42', '44', '46', '48', '50'],
    'USA': ['8', '10', '12', '14', '16', '18', '20', '22'],
    'France': ['38', '40', '42', '44', '46', '48', '50', '52'],
    'GB': ['24', '26', '28', '30', '32', '34', '36', '38']
}


# Universal solution that could be user for all the size types
def find_size(size_table):

    # Creating integer alias for each size type
    numbers = [i for i in size_table]
    print('\nInput size type number, use one of the following ones:')

    # Printing nice output of size types, +1 is to start numbering from 1 instead of 0
    for key, value in enumerate(numbers):
        print(' ', key + 1, value)

    # Trying to handle some of the obvious errors
    try:
        # Get number for size type, -1 is to use the value as an index
        size_type = int(input('\n So, your type is: ')) - 1

        # Getting the exact size and converting it to an apropriate index
        size_index = size_table[numbers[size_type]].index(str(input(' And the size is: ')).upper())

        # Creating the dict with results
        results = {key: size_table[key][size_index] for key in size_table if key != numbers[size_type]}
        # # An altrnative option without dict comprehention
        # results = {}
        # for key in size_table:
        #     if key != numbers[size_type]:
        #         results[key] = size_table[key][size_index]

    except(IndexError, ValueError, UnicodeTranslateError):
        print('Whoops, someting went wrong, terminating')
        exit()
    return results


# Pretty output instead of dict output
def pretty_output(dict_with_sizes):
    print('\nGreat, you will fit the follwong sizes:')
    for key, value in dict_with_sizes.items():
        print(f' {key}: {value}')


# Exectuting all from above (main solution)
pretty_output(find_size(LINGERIE_SIZES))

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Текущее решение более универсальное чем требуемое по заданию.
А вот что, наверное, требовалось:
'''


def expected_solution():
    EXPECTED_DICT = {
        'XXS': {
            'Russia': '42',
            'Germany': '36',
            'USA': '8',
            'France': '38',
            'GB': '24'
        },
        'XS': {
            'Russia': '44',
            'Germany': '38',
            'USA': '10',
            'France': '40',
            'GB': '26'
        },
        'S': {
            'Russia': '46',
            'Germany': '40',
            'USA': '12',
            'France': '42',
            'GB': '28'
        },
        'M': {
            'Russia': '48',
            'Germany': '42',
            'USA': '14',
            'France': '44',
            'GB': '30'
        },
        'L': {
            'Russia': '50',
            'Germany': '44',
            'USA': '16',
            'France': '46',
            'GB': '32'
        },
        'XL': {
            'Russia': '52',
            'Germany': '46',
            'USA': '18',
            'France': '48',
            'GB': '34'
        },
        'XXL': {
            'Russia': '54',
            'Germany': '48',
            'USA': '20',
            'France': '50',
            'GB': '36'
        },
        'XXL': {
            'Russia': '56',
            'Germany': '50',
            'USA': '22',
            'France': '52',
            'GB': '38'
        }
    }
    return EXPECTED_DICT[str(input('Input the size: ')).upper()]


# Executing expected solution
# print(expected_solution())
