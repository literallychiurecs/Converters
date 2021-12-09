import sys
while True:
    restart = 0
    x = float(input("Centimeter -> Inch (1) / Celsius -> Fahrenheit (2) / Kilogram -> Pound (3)"))
    if (x == 2):
        a = float(input("Celsius degrees: "))
        M = (a * 9 / 5) + 32
        print(M)
    if (x == 1):
        b = float(input("Centimeters: "))
        N = b / 2.54
        print(N)
    if (x == 3):
        c = float(input("Kilograms: "))
        O = c * 2.205
        print(O)
    if (x > 3 or x < 1):     
        print("Invalid")
        restart = 1
    if (restart == 1):       
        continue
    if (x == 3 or x == 2 or x == 1):           
        restart = 0
        sys.exit()
