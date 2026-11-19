#w (write)
#r (read)
#r+ (ead and write)
#a (append)


'''nome = "Macaco dardo"

with open("arquivo.txt", "w") as arquivo:
    arquivo.write(f"Olá, boa noite meu nome é: {nome}")
    pass



with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    #conteudo = arquivo.read()
    #print(conteudo)

    #conteudo = arquivo.readline()
    print(conteudo)'''


def escrever_txt(parametro):
    with open("arquivo.txt", "w", encoding=utf-8) as file:
            file.write(parametro)

escrever_txt()