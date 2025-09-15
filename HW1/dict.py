numDict = {}

row = int(input("Enter row: "))
col = int(input("Enter col: "))

for x in range(row):
    print(f"Row {x+1}")
    
    for y in range(col):
        num_value = float(input(f"Enter number {y+1}: "))
        numDict[(x, y)] = num_value

#Searching for the number
search_number = float(input("\nSearch number: "))

#Printing the stored values of dictionary
print("\nThe numbers are:")
for x in range(row):              
    for y in range(col):      
        print(f"{numDict[(x, y)]}",end=' ')
    print()  

foundAt = []
print(f"Number {search_number} found at",end=' ')

for x in range(row):
    for y in range(col):
        if search_number == numDict[(x, y)]:
            position = f"Row {x}, Col {y}"
            foundAt.append(position)
            
final = " and ".join(foundAt)
print(final)