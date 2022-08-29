def agecalculator(n):
    if type(n) == str:
        print("invalid input")
    else:
        a = 100 - n
        b = 2022 + a
        return a,b

print(agecalculator(23))