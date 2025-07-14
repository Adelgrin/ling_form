palavra = input()
inicial = 'q1'
atual = inicial
tamanho = len(palavra)
localCabecote = [inicial]
maquina = {
    'q1' : { '0' : ('q2','D','x'), '1' : ('q3','D','x'), '#' : ('q8','D','#')},
    'q2' : { '0' : ('q2','D','0'), '1' : ('q2','D','1'), '#' : ('q4','D','#')},
    'q3' : { '0' : ('q3','D','0'), '1' : ('q3','D','1'), '#' : ('q5','D','#')},
    'q4' : { '0' : ('q6','E','x'), 'x' : ('q4','D','x')},
    'q5' : { '1' : ('q6','E','x'), 'x' : ('q5','D','x')},
    'q6' : { '0' : ('q6','E','0'), '1' : ('q6','E','1'), 'x' : ('q6','E','x'), '#' : ('q7','E','#')},
    'q7' : { '0' : ('q7','E','0'), '1' : ('q7','E','1'), 'x' : ('q1','D','x')},
    'q8' : { 'x' : ('q8','D','x'), '_' : ('qf','ok','_')}
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
    print('aceita')
except:
     print("rejeita")
