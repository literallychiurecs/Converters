import sys
while True:
    chooseInput = float(input("Decimal -> Binary (1), Binary -> Decimal (2)"))
    restart = 0
    if (chooseInput > 2 or chooseInput < 1):
        print("Invalid")
        restart = 1
    if (restart == 1):
        continue
    if (chooseInput == 1):
        x = int(input("Decimal number: "))


        def decimalToBinary(n):
            if n > 1:
                decimalToBinary(n // 2)
            print(n % 2, end='')


        decimalToBinary(x)
    #
    if (chooseInput == 2):
        y = list(input("Binary number: "))
        value = 0
        for i in range(len(y)):
            digit = y.pop()
            if digit == '1':
                value = value + pow(2, i)
        print(value, end='')

    if (chooseInput == 1 or chooseInput == 2):
        restart = 0
        sys.exit()


