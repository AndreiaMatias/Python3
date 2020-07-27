primeiroNumero = int(input("Informe o primeiro número: "))
segundoNumero = int(input("Informe o segundo número: "))

if primeiroNumero > segundoNumero:
    print("O primeiro número é MAIOR.")
elif segundoNumero > primeiroNumero:
    print("O segundo número é MAIOR.")
else:
    print("Os dois números são IGUAIS.")