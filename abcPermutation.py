a = 'A'
b = 'B'
c = 'C'
for i in range(0,3):
    
    if i == 1:
        temp = a
        a = b
        b = temp
    elif i == 2:
        temp = c
        c = a
        a = temp
    # checking between 1. - 2. characters (if part) and 1 - 3.characters (elif part)
    
    for j in range(0,2):
        print(a + b + c)
        temp = b
        b = c
        c = temp
        # checking for 2. and 3. characters and prints all the permutations of ABC that occurs
