def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    # split string into list
    # cosplitstringlist = text.split()
    # outputword = ""
    # inwordbool = False
    # # parse though the list
    # for i in splitstringlist:
    #     # prase though the word
    #     for w in i:
    #         if w == start:
    #             inwordbool = True

    return text.partition(start)[2].partition(end)[0]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
