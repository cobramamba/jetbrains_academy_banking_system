word = input()
fixed_word = [word[0].lower()]

for char in word[1:]:
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        fixed_word.append('_')
        fixed_word.append(char.lower())
    else:
        fixed_word.append(char)

print(''.join(fixed_word))
