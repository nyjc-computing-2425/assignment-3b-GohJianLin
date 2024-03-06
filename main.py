stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
Eform = stdform.replace("x10^","E")
print(f"This number in E notation is {Eform}.")
