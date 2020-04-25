conta = 0.
# Mesma linha vai ser essa
mesma = 23.0

dici_letra = {
    '.':.88,
    ',':.88,
    ' ':.49
}


palavra = ' sfusufsoadjugaaaaaaaa aaau..............aaaaaaaaaaaaaaaa............................'

for c in palavra:
    if c in dici_letra:
        conta += dici_letra[c]
    else:
        conta += 1.0

linhas = str(conta/mesma)
# Dependendo da quantidades da linha top terá um valor diferente
top = 1.5
dimi = -0.2
ll = dimi * (float(linhas[0])-3)

top = top + ll

linhas = float(linhas) + .3

if conta <= mesma:
    print('\n Mesma linha \n', f'Apenas {str(linhas)[0]} linha', '\n top: 1.2')

else:
    print(f' Outra linha\n', f'São {float(linhas)} linhas', f'\n top: {top}')

