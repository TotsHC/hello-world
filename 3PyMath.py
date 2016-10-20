from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]
if __name__=='__main__':
    number1 = raw_input("Input first number: ")
    number2 = raw_input("Input second number: ")
    number3 = raw_input("Input third number: ")
    number4 = raw_input("Input fourth number: ")
    number5 = raw_input("Input fith number: ")
    number6 = raw_input("Input sixth number: ")
    number7 = raw_input("Input seventh number: ")
    number8 = raw_input("Input eighth number: ")
    number9 = raw_input("Input ninth number: ")
    number10 = raw_input("Input tenth number: ")
    scores = (int(number1), int(number2), int(number3), int(number4), int(number5), int(number6), int(number7), int(number8), int(number9),int(number10))
    scores2 = scores
    mode = calculate_mode(scores2)
    print('The mode of the list of numbers is: {0}'.format(mode))
