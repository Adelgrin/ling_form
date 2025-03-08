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

input = input()
palavras = input.split()
for palavra in palavras:
    atual = inicial
    for caractere in palavra:
        if caractere in funcao[atual]:
            #print(list(funcao[atual][caractere]))
            #print(caractere)
            atual = next(iter(funcao[atual][caractere]))
            
        else:
            atual = None
            break
    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")