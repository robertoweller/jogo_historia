conta = 0.
# Mesma linha vai ser essa
mesma = 23.0

dici_letra = {
    '.':.51,
    ',':.51,
    ' ':.49
}


palavra = 'aaaaaaaaaa aaa.aaaaaaa..'

for c in palavra:
    if c in dici_letra:
        conta += dici_letra[c]
    else:
        conta += 1.0

if conta <= mesma:
    print('\n Mesma linha \n', conta)

else:
    print(' Outra linha\n', conta)




