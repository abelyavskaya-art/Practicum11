numbers = list(map(int, input().split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f'Сумма четных {sum(even)}')
print(f'Сумма нечетных {sum(odd)}')
