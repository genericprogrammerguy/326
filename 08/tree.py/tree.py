# left = add, right = multiply



def left_to_right(numbers, target, curr_total, depth, res):
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
    numbers = [int(numbers) for numbers in input("Enter numbers:").split()]

    target = input("Target Total:")

    res = ['' for i in range(len(numbers) - 1)]
    if left_to_right(numbers, target, numbers[0], 1, res):
        print(res)

    # res = ['' for _ in range(len(numbers) - 1)]
    # if normal(numbers, target, numbers[0], 0, 1, res):
    #     print(res)

    # if(operation == "N"):
    #     normal()
    # elif(operations == "LR"):
    #     left_to_right()
    # else:
    #     print("Wrong")

if __name__ == "__main__":
    main()
    # numbers = [1, 2, 3, 4, 5]
    # target = 120
    # res = ['' for i in range(len(numbers) - 1)]
    # if left_to_right(numbers, target, numbers[0], 1, res):
    #      print(res)
    #
    # numbers = [4, 6, 7, 8]
    # target = 80
    # res = ['' for _ in range(len(numbers) - 1)]
    # if normal(numbers, target, numbers[0], 0, 1, res):
    #     print(res)

