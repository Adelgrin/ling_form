estados = []
alfabeto = []
inicial = ''
aceitacao = []
funcao = {
    
}
#tempfunc = []
estados_entrada = input().split()
for estado in estados_entrada:
    estados.append(estado)

alfabeto_entrada = input().split()
for alfa in alfabeto_entrada:
    alfabeto.append(alfa)


inicial = input()
atual = inicial
aceitacao_entrada = input().split()
for aceita in aceitacao_entrada:
    aceitacao.append(aceita)


for i in range(len(estados)):
    func_entrada = input().split()
    func = []
    for f in func_entrada:
        if f == "vazio":
            func.append("")
            continue
        func_temp = []
        for item in f.split(","):
            func_temp.append(item)
        func.append(func_temp)
    
    funcao[func[0][0]] = {alfabeto[0]: set(func[1]), alfabeto[1]: set(func[2]), "": set(func[3])}
    #tempfunc = []

entrada = input()
estados_ativos = [inicial]
palavras = entrada.split()
for palavra in palavras:
    atual = inicial
    for caractere in palavra:
        for k in estados_ativos:
            for l in funcao[k][caractere]:
                estados_ativos.append(l)
                estados_ativos = list(dict.fromkeys(estados_ativos))
                estados_ativos[estados_ativos.index(k)] = next(iter(funcao[atual][caractere]))
                if len(funcao[k]['']) != 0:
                    for m in funcao[k]['']:
                        estados_ativos.append(m)
                        estados_ativos = list(dict.fromkeys(estados_ativos))
                    #estados_ativos.append(funcao[k][''])
            print(estados_ativos)
            print(caractere)
            if len(funcao[l][caractere]) == 0:
                    estados_ativos.remove(l)
                    break
            
