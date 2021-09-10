def convert(num):
    # Dots * 5 = Dashes
    # Dashes * 4 = Dots

    ones = '' # Dots
    fives = '' # Dashes
    twenties = '' # Dots 
    hundreds = '' # Dashes
    four_hundreds = '' # Dots
    two_thousands = '' #  Dashes
    eight_thousands = '' # Dots
    fourty_thousands = '' # Dashes

    zeroes = ''

    if str(num)[-1] == '0' and num % 20 == 0:
        zeroes = '0'

    for _ in range(num):
        ones += '.'

    for _ in range(len(ones)):
        if len(ones) - 5 >= 0:
            fives += '-'
            ones = ones[5:]

    for _ in range(len(fives)):
        if len(fives) - 4 >= 0:
            twenties += '.'
            fives = fives[4:]

    for _ in range(len(twenties)):
        if len(twenties) - 5 >= 0:
            hundreds += '-'
            twenties = twenties[5:]

    for _ in range(len(hundreds)):
        if len(hundreds) - 4 >= 0:
            four_hundreds += '.'
            hundreds = hundreds[4:]
    
    for _ in range(len(four_hundreds)):
        if len(four_hundreds) - 5 >= 0:
            two_thousands += '-'
            four_hundreds = four_hundreds[5:]

    for _ in range(len(two_thousands)):
        if len(two_thousands) - 4 >= 0:
            eight_thousands += '.'
            two_thousands = two_thousands[4:]

    for _ in range(len(eight_thousands)):
        if len(eight_thousands) - 5 >= 0:
            fourty_thousands += '-'
            eight_thousands = eight_thousands[5:]

    print(eight_thousands)
    print(fourty_thousands)
    print(four_hundreds)
    print(two_thousands)
    print(twenties)
    print(hundreds)
    print(ones)
    print(fives)
    print(zeroes)

convert(int(input('Number >>> ')))

# Max 159,999