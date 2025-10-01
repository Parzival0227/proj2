def string_frequency(input):
   
    nList = []
    for i in range(len(input)):
        new = list(input[i].strip())
        nList.append(new)
   
    for i in range(len(nList)):
        letters = {}
        
        for j in range(len(nList[i])):
            letter = nList[i][j]
            if nList[i][j] not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        for k, v in letters.items():
            print(f"{k}={v}", end=', ')
        print()
    
def main():
    input_string = input("Enter string: ").lower().strip()
    string_frequency(input_string.split(","))
main()