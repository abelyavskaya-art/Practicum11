number = int(input())
result = []

for num in range(1, number+1):
    if number % num == 0:
        result.append(num)

print(' '.join(map(str, result)))
