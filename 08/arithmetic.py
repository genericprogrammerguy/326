# left = add, right = multiply
import sys
def left_to_right(numbers, target, curr_total, depth, res):
    """
    Recursive method which does left to right arithmetic

    :param numbers: given input of numbers to calculate
    :param target: is the value we are looking for
    :param curr_total: Holds values of current calculation
    :param depth: The level of recursion
    :param res:  weather the target value has been found or not
    :return: weather the target value has been found or not
    """
    if(curr_total > target):
        return False
    if depth == len(numbers):
        return curr_total == target
    if left_to_right(numbers, target, curr_total + numbers[depth], depth + 1, res):
        res[depth-1] = "+"
        return True
    if left_to_right(numbers, target, curr_total * numbers[depth], depth + 1, res):
        res[depth - 1] = "*"
        return True

def normal(numbers, target, curr_total, temp, depth, res):
    """

    :param numbers: given input of numbers to calculate
    :param target: is the value we are looking for
    :param curr_total: Holds values of current calculation
    :param temp: holding addition value total until verification
    :param depth: The level of recursion
    :param res:  weather the target value has been found or not
    :return: weather the target value has been found or not
    """

    if temp > target or curr_total > target:
        return False
    if depth == len(numbers):
        return curr_total + temp == target
    if normal(numbers, target, numbers[depth], curr_total + temp, depth + 1, res):
        res[depth - 1] = "+"
        return True
    if normal(numbers, target, curr_total * numbers[depth], temp, depth + 1, res):
        res[depth - 1] = "*"
        return True


def main():
    """
    Main driver control of program. Prompts user for input
    Control flow of program is


    :return:
    """
    # numbers = [1, 2, 3, 4, 5]
    # target = 120
    #
    # print("Enter Numbers:")
    # for nums in sys.stdin:
    # res = ['' for i in range(len(numbers) - 1)]
    # if left_to_right(numbers, target, numbers[0], 1, res):
    #     print(res)
    #
    # numbers = [4, 6, 7, 8]
    # target = 80
    # res = ['' for _ in range(len(numbers) - 1)]
    # if normal(numbers, target, numbers[0], 0, 1, res):
    #     print(res)
    numbers = []
    res = []
    line_non = 0
    for group in sys.stdin:
        if line_non == 0:
            numbers = group.split()
            numbers = [int(i) for i in numbers]
            res = ['' for _ in range(len(numbers) - 1)]
            line_non += 1
        else:
            order = group.split()[1]
            target = int(group.split()[0])
            line_non = 0
            if order == "L":
                if left_to_right(numbers, target, numbers[0], 1, res):
                    print(order, target, numbers[0], end=' ')
                    for i, o in enumerate(res):
                        print(o, numbers[i+1], end=' ')
                    print()
                else:
                    print(order, target, "impossible")
            else:
                if normal(numbers, target, numbers[0], 0, 1, res):
                    print(order, target, numbers[0], end=' ')
                    for i, o in enumerate(res):
                        print(o, numbers[i + 1], end=' ')
                    print()
                else:
                    print(order, target, "impossible")


main()