def collatz(number):
    if number % 2:
        value = 3 * number + 1
        print(value)
        return value
    else:
        value = number // 2
        print(value)
        return value

success = False

while not success:
    print("Enter a number: ")
    number = input()
    try:
        number = int(number)
        success = True
    except:
        print('You must enter an integer')

while number != 1:
    number = collatz(number)

