def multiplyNumbers(numbers):
    numbers_list = []
    for number in numbers:
        numbers_list.append(number * 2)
    return numbers_list

def multiplyNumbers1(numbers):
    return [(number * 2) for number in numbers]


numbers = [33, 66, 99, 111, 333]
print(multiplyNumbers(numbers))
print(multiplyNumbers1(numbers))