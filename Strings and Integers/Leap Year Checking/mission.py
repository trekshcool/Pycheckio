def is_leap_year(year: int) -> bool:
    # your code here
    return False


print("Example:")
print(is_leap_year(1891))

# These "asserts" are used for self-checking
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
