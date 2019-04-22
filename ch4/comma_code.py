spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(arr):
    return ', '.join(arr[:-1]) + ', and ' + arr[-1]

print(comma_code(spam))
