
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

esc = input("Qual seria a operação a=Soma, b=Substação, c=Multiplicação ou d=divisão: ")

if esc == 'a':
    soma = num1 + num2
    print("dar:", soma)
elif esc == 'b':
    menos = num1 - num2
    print("dar:", menos)
elif esc == 'c':
    vezes = num1 * num2
    print("dar:", vezes)
elif esc == 'd':
    if num2 == 0:
        print("Erro: Divide com zero não fi")
    else:
        esc_div = input("Deseja o resultado i=Inteiro, c=Completo ou r=Resto? ")
        if esc_div == 'i':
            div_int = num1 // num2
            print("dar:", div_int)
        elif esc_div == 'c':
            dividi = num1 / num2
            print("dar::", dividi)
        elif esc_div == 'r':
            resto = num1 % num2
            print("dar:", resto)
        else:
            print("Deu não.")
else:
    print("Opção inválida.")
