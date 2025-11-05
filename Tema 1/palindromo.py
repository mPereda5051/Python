number = input("select a number with at least two digits: ")
print(number)

chain_number = str(number)

inverted_chain = chain_number[::-1]

print(int(chain_number))
print(int(inverted_chain))
if chain_number == inverted_chain:
    print("is palindrome")
else:
    print("is not palindrome")
