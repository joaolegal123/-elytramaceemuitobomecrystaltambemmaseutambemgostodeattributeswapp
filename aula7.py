#globais
#locais

def saudacoes():
    print("Olá! Boa noite, Henrique")
lista = [1,2,3,4,5,6,7,8,9,10]

def e_par(n):
    if i %2 ==0:
        return True
    else:
        return False

for i in lista:
    print(e_par(i))

print()
print()
print(f"O número 2 é par? {e_par(2)}")

 
for i in range(10):
    lista.append(int(input("Digite um numero: ")))
n = 0

for i in lista:
    if n < i:
        n = i

print(n)