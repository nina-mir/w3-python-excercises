
example_0 = set(["gabel", "messer", "teller", "loeffel", "artzin"])
example_1 = set((0, 999, 101, 444))
# 1. Write a Python program to create a set. Go to the editor
def prob_1():
    return set()
print(type( prob_1() ))

# 2. Write a Python program to iterate over sets. Go to the editor
def prob_2(set):
    for x in set:
        print(x)


# 3. Write a Python program to add member(s) in a set. Go to the editor
def prob_3(item, set):
    set.add(item)

# 4. Write a Python program to remove item(s) from set Go to the editor
def prob_4(*args, set = set):
    for item in args:
        set.remove(item)


prob_2(example_1)
prob_3("die Ente", example_0)
prob_2(example_0)
print("\n")
prob_4("loeffel", "die Ente", set = example_0)
prob_2(example_0)
