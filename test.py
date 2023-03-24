string = 'Hello, world!'
substring = 'world'
try:
    pos = string.index(substring)
    print(f'The substring "{substring}" is at position {pos} in the string.')
except ValueError:
    print(f'The substring "{substring}" is not in the string.')
