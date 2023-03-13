### Lambdas ###

sum_two_values = lambda first_value, segund_value: first_value + segund_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, segund_value: first_value * segund_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, segund_value: first_value + segund_value + value

print(sum_three_values(5)(2, 4))

