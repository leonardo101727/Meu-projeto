nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print(" O nome deve ter mais que 3 caracteres.")
    nome = input("Digite seu nome novamente: ")


idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print(" Idade inválida. Deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade novamente: "))


salario = float(input("Digite seu salário: "))
while salario <= 0:
    print(" O salário deve ser maior que zero.")
    salario = float(input("Digite seu salário novamente: "))


genero = input("Digite seu gênero ('f' para feminino, 'm' para masculino): ").lower()
while genero not in ('f', 'm'):
    print(" Gênero inválido. Use apenas 'f' ou 'm'.")
    genero = input("Digite seu gênero novamente: ").lower()


estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil not in ('s', 'c', 'v', 'd'):
    print(" Estado civil inválido. Use apenas 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite seu estado civil novamente: ").lower()

print("\n Dados válidos! Aqui estão suas informações:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Gênero: {genero}")
print(f"Estado Civil: {estado_civil}")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os dois números são iguais.")    

valor = float(input("Digite um número: "))

if valor > 0:
    print("O número é positivo.")
elif valor < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")