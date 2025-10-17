# 1️⃣ Add two numbers
add = lambda a, b: a + b
print("Add:", add(5, 3))   # Output: 8

# 2️⃣ Find square of a number
square = lambda x: x * x
print("Square:", square(4))   # Output: 16

# 3️⃣ Check if a number is even
is_even = lambda x: x % 2 == 0
print("Is Even:", is_even(6))  # Output: True

# 4️⃣ Use with map() – square each number in a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# 5️⃣ Use with filter() – get even numbers from a list
nums = [10, 15, 20, 25, 30]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even Numbers:", even_nums)  # Output: [10, 20, 30]

# 6️⃣ Use with sorted() – sort by second value in tuple
data = [(1, 3), (2, 2), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted Data:", sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]

# 7️⃣ Lambda inside another function
def my_func(n):
    return lambda x: x * n

doubler = my_func(2)
print("Doubled Value:", doubler(5))  # Output: 10
