def factorial(n: int) -> int:
    # your code here
    countdownnum = n
    outputdigit = 1
    while True:
        if countdownnum == 0:
            return 1

        outputdigit = outputdigit * countdownnum

        print(outputdigit)

        countdownnum = countdownnum - 1
        if countdownnum == 1:
            break

    return outputdigit


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")
