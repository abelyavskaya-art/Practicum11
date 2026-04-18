lst = list(map(int, input().split()))
result = []
task = input().strip()

direction = task[0]
shift = int(task[1:])

if shift == 0:
    result = lst
elif direction == 'R':
    result = lst[-shift:] + lst[:-shift]
elif direction == 'L':
    result = lst[shift:] + lst[:shift]

print(' '.join(map(str, result)))
