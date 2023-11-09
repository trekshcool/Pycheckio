def checkio(number: int) -> str:
    # your code here
    outPutString = ""
    divibythree = False
    divibyfive = False

    if number % 3 == 0:
        divibythree = True
    if number % 5 == 0:
        divibyfive = True

    if divibythree:
        outPutString = outPutString + "Fizz"
    if divibyfive & divibythree:
        outPutString = outPutString + " "
    if divibyfive:
        outPutString = outPutString + "Buzz"
    if (divibyfive == False) & (divibythree == False):
        return str(number)
    return outPutString


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
