
def convert_dollar_yen(dollar):
    yen_rate = 146.67
    yen = []
    
    for x in dollar:
        convert = x * yen_rate
        yen.append(convert)
        
    return yen



def convert_dollar_peso(dollar):
    peso_rate = 57.17
    peso = []
    
    for x in dollar:
        convert = x * peso_rate
        peso.append(convert)
        
    return peso


def main():
    dollar_yen = []
    dollar_peso = []
    currency_text = ["Dollar($)", "Phil Peso(P)", "Jpn Yen (Y)"]
    
    dollar = input("Enter currency ($): ").split(",")
    
    for x in range(len(dollar)):
        dollar[x] = float(dollar[x])
        
    dollar_peso = convert_dollar_peso(dollar)
    dollar_yen = convert_dollar_yen(dollar)
    
    
    for currency in currency_text:
        print(f"{currency:<15}", end='')
    print()
    
    for x in range(len(dollar)):
        print(f"{dollar[x]:<15.0f} {dollar_peso[x]:<15.2f} {dollar_yen[x]:<15.2f}")
        
main()
    
    