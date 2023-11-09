def number_length(value: int) -> int:
    digitcount = 0
    value = str(value)
    for i in value:
        digitcount = digitcount + 1
    return digitcount


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")
