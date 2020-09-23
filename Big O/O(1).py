five_numbers = [0, 1, 2, 3, 4, 5]
three_numbers = [0, 1, 2]
ten_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def grabFirstTwoNumbers(numbers):
    print(numbers[0]) # O(1)
    print(numbers[1]) # O(1)

# Irrespective of the number of inputs (5, 3 or 10) to the function grabFirstTwonumbers it always performs only 2 operations hence it is O(1)
# O(1) means the number of operations remain same irrespective of the number of inputs
grabFirstTwoNumbers(five_numbers)
grabFirstTwoNumbers(three_numbers)
grabFirstTwoNumbers(ten_numbers)