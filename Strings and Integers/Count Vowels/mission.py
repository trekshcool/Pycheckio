def count_vowels(text: str) -> int:
    # your code here
    vovelcount = 0
    for i in text:
        if i == "a":
            vovelcount = vovelcount + 1
        if i == "e":
            vovelcount = vovelcount + 1
        if i == "i":
            vovelcount = vovelcount + 1
        if i == "o":
            vovelcount = vovelcount + 1
        if i == "u":
            vovelcount = vovelcount + 1
        if i == "A":
            vovelcount = vovelcount + 1
        if i == "E":
            vovelcount = vovelcount + 1
        if i == "I":
            vovelcount = vovelcount + 1
        if i == "O":
            vovelcount = vovelcount + 1
        if i == "U":
            vovelcount = vovelcount + 1
    return vovelcount


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
