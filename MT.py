
palavra = input()
inicial = 'q1'
atual = inicial
tamanho = len(palavra)
localCabecote = [inicial]
maquina = {
    'q1' : { '0' : ('q2','D','_'), '_' : ('qr','D','_'),'x' : ('qr','D','x')},
    'q2' : { '0' : ('q3','D','x'), 'x' : ('q2','D','x'), '_' : ('qf','D','_')},
    'q3' : { '0' : ('q4','D','0'), 'x' : ('q3','D','x'), '_' : ('q5','E','_')},
    'q4' : { '0' : ('q3','D','x'), 'x' : ('q4','D','x'), '_' : ('qr','D','_')},
    'q5' : { '0' : ('q5','E','0'), 'x' : ('q5','E','x'), '_' : ('q2','D','_')},
    'qr' : { '0' : ('qr','E','0'), '1' : ('qr','E','1'), 'x' : ('qr','E','x'), '_' : ('qr','E','_')}
}

#  10#10
# [q1,1,0,#,1,0]
palavra = palavra + '_'
for letra in palavra:
    localCabecote.append(letra)
flag = 0
posCabecote = 0
letra = localCabecote[posCabecote+1]
try:
    while flag != 1:
        for i in localCabecote:
            print(i, end=' ')
        print()
        if maquina[atual][letra][1] == 'D':
            localCabecote[posCabecote+1] = maquina[atual][letra][2]
            localCabecote[posCabecote] , localCabecote[posCabecote+1] = localCabecote[posCabecote+1], maquina[atual][letra][0] #movimenta o cabecote
            atual = maquina[atual][letra][0] #proximo caso
            posCabecote = localCabecote.index(atual) #altera estado cabecote
            letra = localCabecote[posCabecote+1]
        elif maquina[atual][letra][1] == 'E':
                localCabecote[posCabecote+1] = maquina[atual][letra][2]
                localCabecote[posCabecote] , localCabecote[posCabecote-1] = localCabecote[posCabecote-1], maquina[atual][letra][0]
                atual = maquina[atual][letra][0]
                posCabecote = localCabecote.index(atual)
                letra = localCabecote[posCabecote+1]
        elif maquina[atual][letra][1] == 'ok':
            flag = 1
        #if maquina[atual][letra][0] == 'qr':
             #posCabecote[4000000]
    print('aceita')
except:
     print("rejeita")
