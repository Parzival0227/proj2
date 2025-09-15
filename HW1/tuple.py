numTuple = ()

row = int(input("Enter row: "))
col = int(input("Enter col: "))


for x in range(row): 
    print(f"\nRow {x+1}:")
    inner_list = []
    
    for y in range(col):
        num = float(input(f"Enter number {y+1}: "))
        inner_list.append(num) 
    inner_tuple = tuple(inner_list)
    numTuple += (inner_tuple,)


search_num = float(input("\nSearch: "))


print("\nThe numbers are:")
for x in range(len(numTuple)):
    
    for y in range(len(numTuple[x])):
        print(f"{numTuple[x][y]:.1f}", end=' ')
        
    print()


found_position = []
for x in range(len(numTuple)):
    
    for y in range(len(numTuple[x])):
        if search_num == numTuple[x][y]:
            position = f"Row {x}, Col {y}"
            found_position.append(position)
            
print(f"\nNumber {search_num} found at", end=' ')
final = " and ".join(found_position)
print(final)