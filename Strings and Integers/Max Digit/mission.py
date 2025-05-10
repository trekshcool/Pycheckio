def max_digit(value: int) -> int:
    # your code here
    valstring = str(value)
    maxnum = 0
    # Split the string into each letter then compare them with the max, then send max
    for i in valstring:
      j = int(i)
      if j >= maxnum:
        maxnum = j

    return maxnum


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
