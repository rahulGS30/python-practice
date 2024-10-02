def binoperations(str):
    if str is None:
        return -1
    result = int(str[0])
    for i in range(1,len(str),2):
        operator = str[i]
        operand = int(str[i+1])
        if operator =='A':
            result = result and operand
        elif operator =='B':
            result = result or operand
        elif operator =='C':
            result = result ^ operand
    return result

str = "1C0C1C1A0B1"
print(binoperations(str))