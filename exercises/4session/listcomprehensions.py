# Ex 1: Alphabet List Comprehensions

# 1.
l = [chr(x) for x in range(ord('A'), ord('Z')+1)]
print(l)

# 2. 
l = [chr(x) for x in range(ord('A'), ord('Z')+1) if x not in [70, 75, 80, 85]]
print(l)

# 3. 
l = [chr(x) for x in range(ord('A'), ord('Z')+1) if x not in range(ord('F'), ord('O'), 2)]
print(l)


# Ex 2: Clothes List Comprehension

# 1. 
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
l = [(x,y) for x in colors for y in sizes]
print(l)

# 2. 

# Forstår ikke helt opgaven ...

# Ex 3: List & Tuples exercise



# Ex 4: Sys module exercise

# Create a commandline tool that checks if the required arguments are present when you run the program, 
# and if not tells you what is missing to run the program