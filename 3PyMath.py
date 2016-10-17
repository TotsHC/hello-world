from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]
if __name__=='__main__':
    scores = raw_input("Input Scores: ")
    mode = calculate_mode(scores)
    print('The mode of the list of numbers is: {0}'.format(mode))
