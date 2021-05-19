numbers = [] #an empty list definition for taking the inputs in it

for i in range(0,10):
    element = int(input(f"Enter the {i + 1}.element of your list: "))
    #taking the inputs in a list by using a for loop 
    numbers.append(element) #adding each elements in numbers list

print(f"Your list = {numbers}") 

for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j + 1]:
            t = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = t
#bubble sort algorithm 

print(f"Your list in ascending order : {numbers}")
#prints the sorted list in ascending order
