import re
def count_occurrences(main_str: str, sub_str: str) -> int:
    # your code here
    # does not work, cant find overlapped stuff
    # main_str.lower().count(sub_str.lower())

    # this one works with re
    # without f'(?={sub_str})' it does not find overlapping substrings
    count = len(re.findall(f'(?={sub_str})', main_str, flags=re.IGNORECASE))

    return count


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
