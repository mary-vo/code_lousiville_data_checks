# A statement that prints "hello world!"
print("hello world!")

# Create a list with several values
# Print one of the values from the list
## Note to self list = [], dictionary = {}
cat_breeds = ["Siamese", "Ragdoll", "Russian Blue", "Munchkin"]
print(f"List of cat breeds: {cat_breeds}")
# Indexing to return Russian Blue from cat_breeds list
print(f"{cat_breeds[2]} is the best cat breed!")


# Create a dictionary with two keys and two values
# Print one of the key-value pair from the dictionary
cat_name_and_age = {"Luna":6, "Sorin":3}
# Print Luna's age from the dictionary
print(cat_name_and_age["Luna"])
# Other print statements
print(cat_name_and_age.keys())
print(cat_name_and_age.values())
# Using unpacking operator
print(*cat_name_and_age.items())
print(*cat_name_and_age.items(), sep='\n')


# Create a tuple with 4 values
# Print one of the values
cat_breeds = ("Siamese", "Ragdoll", "Russian Blue", "Munchkin")
# Print Russian Blue
print(f"{cat_breeds[2]} is the best cat breed!")
#### Did I just confuse myself? What is the difference between Tuple and List? What purpose does Tuple serve?