entrance = input()
words = list(entrance.split(' '))
punctuation = '.,!?;:()[]{}"\'-'

result = []
for word in words:
    clean_word = word.strip(punctuation)
    if clean_word.lower() not in result and clean_word not in punctuation:
        result.append(clean_word.lower())

print(' '.join(result))
