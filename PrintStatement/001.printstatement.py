# Expected o/p: Hi! Selva
print("Hi! Selva")
print('Hi! Selva')

# Expected o/p: you're here to Learn python
print("you're here to Learn Python")

# Expected o/p: "you are here to learn python"
print('"you are here to learn python"')

# Expected o/p: "you're here to learn python"
print('"you\'re here to learn python"')

# Expected o/p: 
# Welcome
# To
# Learn
# Python
print("Welcome\nTo\nLearn\nPython")

# Expected o/p:
    # Name    :   Selva
    # Role    :   DevOps Engineer
print("Name\t:\tSelva")
print("Role\t:\tDevOps")

# Expected o/p:
# Happy Learning
# Happy_Learning
# Happy+Learning
# HappyLearning
print("Happy","Learning")

print("Happy","Learning",sep="_")

print("Happy","Learning",sep=" + ")

print("Happy","Learning",sep="")

# Expected o/p:
# Happy Learning Python Code.
# (Use three print statement to get the above output)
print("Happy",end=" ")
print("Learning",end=" ")
print("Python",end=" ")
print("Code",end=".")