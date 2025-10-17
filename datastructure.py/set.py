# Creating a set
numbers = {1, 2, 3, 3, 2}

print(numbers)  # {1, 2, 3} - duplicates removed

# Add and remove
numbers.add(4)
numbers.remove(2)

# Set operations
even = {2, 4, 6}
print(numbers.union(even))        # {1, 2, 3, 4, 6}
print(numbers.intersection(even)) # {4}
