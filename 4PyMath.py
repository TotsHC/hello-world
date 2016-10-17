def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest-lowest
    return lowest, highest, r
if __name__ == '__main__':
    number1 = raw_input("Input first number: ")
    number2 = raw_input("Input second number: ")
    number3 = raw_input("Input third number: ")
    number4 = raw_input("Input fourth number: ")
    number5 = raw_input("Input fith number: ")
    donations = (int(number1), int(number2), int(number3), int(number4), int(number5))
    donations2 = donations
    lowest, highest, r = find_range(donations2)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
