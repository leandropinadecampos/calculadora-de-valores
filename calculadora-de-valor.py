while True:
    try:
        valor = float (input ('Valor do produto: '))
        if valor > 0:
            break
        else:
            print ('Digite um valor maior que zero')
    except ValueError:
        print ('Digite um número válido')

o1 = valor - (valor * 10/100)
o2 = valor - (valor * 5/100)
o3 = valor
o4 = valor + (valor * 20/100)

while True:
    print()
    print ('=-=' * 20)
    print ('Formas de Pagamento'.center(60))
    print ('=-=' * 20)
    print()
    print ('1 - Á vista dinheiro/cheque')
    print ('2 - Á vista no cartão')
    print ('3 - Em até 2x no cartão')
    print ('4 - 3x ou mais no cartão')
    print()

    fp = input ('Escolha a forma de pagamento: ')
    print()

    if fp == '1':
        print (f'O valor pago será de R${o1:.2f}')
        break
    elif fp == '2':
        print (f'O valor pago será de R${o2:.2f}')
        break
    elif fp == '3':
        print (f'O valor pago será de R${o3:.2f} em 2 parcelas de R${o3/2:.2f}')
        break
    elif fp == '4':
        try:
            vezes = int (input ('Quantidade de parcelas: '))
            if vezes >= 3:
                print (f'O valor pago será de R${o4:.2f} em {vezes} parcelas de R${o4 / vezes:.2f}.')
                break
            else:
                print ('Para essa opção o mínimo de parcelas é 3, escolha novamente.')
        except ValueError:
            print ('Digite um número válido')
    else:
        print ('Opção inválida, selecione uma opção válida.')
