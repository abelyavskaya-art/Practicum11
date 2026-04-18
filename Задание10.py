lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

start = int(input())
end = int(input())

# New index for Python.
start_idx = start - 1
end_idx = end - 1

elements_lst1 = lst1[start_idx:end_idx + 1]

# Extend element of first list to second.
lst2.extend(elements_lst1[::-1])

# Delete elements from first list.
del lst1[start_idx:end_idx + 1]

print(lst1)
print(lst2)
