from time import sleep as sl

ad = 0
lista = ['oi', 'tudo bem?', 'kkk', 'oi', 'vida boaaa']
conta = []


while True:
    sl(2)
    ad += 1
    if ad <= len(lista):
        for m in range(ad):
            if m not in conta:

                print(lista[m])
                conta.append(m)

    else:
        break
print('Obrigada, por sua atenção ^.^ S2')

