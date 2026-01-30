subjects = ["Math", "Physics", "Chemistry", "Computer Science"]

# append() - add an item to the end
subjects.append("Biology")
print(subjects)

# pop() - remove the last item
removed = subjects.pop()
print(removed)
print(subjects)

# remove() - remove the first occurrence of a value
subjects.remove("Physics")
print(subjects)

# del - delete an item by index
del subjects[1]
print(subjects)

# sort() - sort the list permanently
subjects.sort()
print(subjects)

# sorted() - sort temporarily
print(sorted(subjects, reverse=True))
print(subjects)

# reverse() - reverse the order
subjects.reverse()
print(subjects)

# len() - get length of list
print(len(subjects))