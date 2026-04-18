entrance = input()
words = list(entrance.split(' '))
punctuation = '.,!?;:()[]{}"\''

result = []
for word in words:
    clean_word = word.strip(punctuation)
    result.append(clean_word)

print(' '.join(result))
