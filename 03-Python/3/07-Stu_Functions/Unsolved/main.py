# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number 
    return total/length
# Test your function with the following:

def listcomp_average(numbers):
    length = len(numbers)
    total = 0.0
    [total := total+number for number in numbers]
    return total / length

print(average([1, 5, 9]))
print(average(range(11)))
print("-" * 50)
print("List comprehension")
print(listcomp_average([1, 5, 9]))
print(listcomp_average(range(11)))
