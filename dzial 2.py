
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
 

operacja = input("Wybierz operację arytmetyczną (+, -, *, /, **, %): ")
 

def wykonaj_operacje(operacja):
    if operacja == "+":
        return x + y
    elif operacja == "-":
        return x - y
    elif operacja == "*":
        return x * y
    elif operacja == "/":
        return x / y
    elif operacja == "**":
        return x ** y
    elif operacja == "%":
        return x % y
    else:
        return "Nieprawidłowa operacja"
 

print(f"{x} {operacja} {y} = {wykonaj_operacje(operacja)}")
