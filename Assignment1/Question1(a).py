input_string = list(input("Enter a string: "))
if len(input_string) >= 2:
    del input_string[:2]
    reversed_string = ''.join(input_string[::-1])
    print("Reversed string:", reversed_string)
else:
    print("Enter the input string with minimum of three letters")
