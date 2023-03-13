### Higher Order Functions ###

from functools import reduce
print("Higher Order Functions\n")

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_value_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_value_and_add_value(5,2, sum_one))
print(sum_two_value_and_add_value(5,2, sum_five))

### Closures ###

print("\nClosures\n")

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built_in Higher Order Functions ###

print("\nBuilt_in Higher Order Functions\n")

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2,numbers)))

# Filter

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

### Reduce ###
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values,numbers))