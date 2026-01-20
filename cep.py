def regcep():
    cep = input("Digite o CEP: ")
    if len(cep) != 8 or not cep.isdigit(): #"Se o CEP não tiver 8 caracteres OU não for composto apenas por números, então o CEP é inválido."
        print("CEP inválido. Deve conter exatamente 8 dígitos numéricos.")
        cep = ""
        return regcep()
    else:
        print("CEP válido.")
        arq = open("cep.txt", "a")
        arq.write(cep + "\n")
        arq.close()

    voltar = input("Deseja registrar outro CEP? (s/n): ").lower() #Se o usuario digitar em maiusculo, o .lower() transforma em minusculo
    if voltar == 's':
        return regcep()
    else:

        exit()

regcep()

if __name__ == "__main__":
    regcep()



