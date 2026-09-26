name = str(input('enter your name:')).strip()

print('analyzing your name...')
print(f'your name in capital letters is: {name.upper()}')
print(f'your name in lowercase is: {name.lower()}')
print(f'Your full name has: {len(name) - name.count(' ')} letters')
print(f'your first name has: {name.find(' ')} letters')
