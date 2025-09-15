numList = []

row = int(input("Enter row: "))
col = int(input("Enter col: "))

for x in range(row):
    print(f"\nRow {x+1}")
    inner_list = []
    
    for y in range(col):
        num = float(input(f"Enter number {y+1}: "))
        inner_list.append(num) 
    
    numList.append(inner_list)


search = float(input("\nSearch: "))


print("\nThe numbers are:")
for x in range(len(numList)):
    
    for y in range(len(numList[x])):
        print(f"{numList[x][y]:.1f}", end=' ')
        
    print()

found_position = []
for x in range(len(numList)):
    
    for y in range(len(numList[x])):
        if search == numList[x][y]:
            position = f"Row {x}, Col {y}"
            found_position.append(position)
            

print(f"\nNumber {search} found at", end=' ')
final = " and ".join(found_position)
print(final)
print(found_position)