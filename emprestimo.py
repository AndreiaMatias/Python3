valorCasa = float(input("Qual o valor da casa? R$"))
salarioComprador = float(input("Qual o salário do comprador? R$"))
prazoFinanciamento = int(input("Qual o prazo do financiamento?"))

prazoMeses = prazoFinanciamento * 12
prestacaoFinanciamento = valorCasa/prazoMeses

if prestacaoFinanciamento < (salarioComprador*0.3):
    print(f"Para pagar uma casa de R${valorCasa:.2f} em {prazoFinanciamento} a prestação será de {prestacaoFinanciamento:.2f}.")
    print("Empréstimo \033[1;32m CONCEDIDO")
else:
    print("Empréstimo \033[1;31m NEGADO")
