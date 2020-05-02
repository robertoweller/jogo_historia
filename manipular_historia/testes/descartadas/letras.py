conta = 0.
# Mesma linha vai ser essa
mesma = 23.0

dici_letra = {
    '.':.88,
    ',':.88,
    ' ':.49
}

top = {
    0:1.2,
    1:1.2,
    2:1.5,
    3:1.5,
    4:1.3
}

palavra = ' sfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
palavra = ' akkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'

for c in palavra:
    if c in dici_letra:
        conta += dici_letra[c]
    else:
        conta += 1.0

linhas = str(conta/mesma)

# Procura na biblioteca o primeiro numero inteiro e devolve qual valor de top
acha = top[int(linhas[0])]

# Dependendo da quantidades da linha top terá um valor diferente
print(f'Tem {linhas} linha(s) \ntop: {acha}')



