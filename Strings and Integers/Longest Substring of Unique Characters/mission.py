def longest_substr(s: str) -> int:
    # your code here
    # if string is empty return 0
    if len(s) == 0: return 0

    # Define the lower bound and upper bound for the set
    low,up = 0,1

    # the max bounds giving the longest unique char set length in the string
    maxbound = (0,1)

    # the set of used chars, adding the first char from the start
    used = {s[low]}

    # loop as long as up is less than the lentgh of the string
    while up < len(s):
        # if the up number char in string is already in used
        if s[up] in used:
            # remove the lower bound char from the used set
            used.remove(s[low])
            # adding one to low to move the lower bound up
            low += 1
        # if the char is unique and not in used
        else:
            # add the char in the upper bound to used
            used.add(s[up])
            # move the upper bound up by one
            up += 1
        # Check if current bounds are longer than max bounds, if so update it
        if up - low > maxbound[1] - maxbound[0]:
            maxbound = (low,up)
    return maxbound[1] - maxbound[0]


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
