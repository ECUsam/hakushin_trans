with open('po1_event.dat', 'r', encoding='utf16') as f:
    contents = f.read()

search_string = 'event po1_op2'
index = contents.find(search_string)

if index == -1:
    print('The search string was not found.')
else:
    offset = len(contents[:index].encode('utf16'))
    print(f'The search string was found at offset {offset}.')

print('tset')
