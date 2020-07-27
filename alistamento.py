#importando biblioteca
from datetime import datetime

#solicita ao cliente o ano de nascimento.
anoNascimento = int(input("Ano de Nascimento: "))

#captura o ano atual
anoAtual = datetime.now().year

#calcula a idade
idade = anoAtual - anoNascimento

#saída para o usuário
print(f"Quem nasceu em {anoNascimento} tem {idade} anos.")
if idade < 18:
    print("Você ainda não precisa se alistar.")
elif idade == 18:
    print("Está na hora de você se alistar.")
else:
    atraso = idade - 18
    print(f"Você deveria ter se alistado há {atraso} anos.")
    print(f"Seu alistamento foi em {anoAtual - atraso}")