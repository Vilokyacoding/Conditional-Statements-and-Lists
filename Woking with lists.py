lst = ['Mango', 'Guava', 'Apple', 'Banana', 'Kiwi']
print("Length of list:", len(lst))
print("First element :", lst[0])
print("Last element :", lst[-1])

lst.append('Orange')
print("Updated list:", lst)

if 'Apple' in lst:
    lst.remove('Apple')
print("Updated list:", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop()
print("Updated list :", lst)

lst.reverse()
print("Reversed list:", lst)

print("Multiplication on list:", lst * 2)

lst =lst[:4]
print("Sliced list:", lst)

lst.clear()
print("Updated list:", lst)