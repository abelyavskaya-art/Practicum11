numbers = []

for i in range(10):
    num = int(input())
    numbers.append(num)

new_list = []

for i in range(1, 9):
    new_num = numbers[i-1] + numbers[i+1]
    new_list.append(new_num)

print(new_list)
